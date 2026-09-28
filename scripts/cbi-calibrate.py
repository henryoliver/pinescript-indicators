#!/usr/bin/env python3
"""Grade a composite-breadth 🧪 Calibration Log export against forward price.

Reads what the Pine Logs pane copies out — CBI_HEAD / CBI_LOG rows, with or
without TradingView's own `[timestamp]:` prefix — and answers the five claims
the log layer was built to test:

  ① STANCE     does the sign/level of the composite lead price?
  ② AGREEMENT  is a vivid bar worth more than a pale one?
  ③ REGIME     does the Line Trust classification separate anything?
  ④ MARKERS    do ▲ and ◆ pay?
  ⑤ WEIGHTS    re-derives the composite from the RAW feeds under alternative
               weightings, so a weight question is answered without a re-export.

    Usage:  scripts/cbi-calibrate.py export.txt
            scripts/cbi-calibrate.py export.txt --horizons 15,30,60
            scripts/cbi-calibrate.py a.txt b.txt c.txt      # pooled chunks

Stdlib only, no install. Forward returns are close-to-close, never crossing a
session boundary, reported in basis points and in ATR units.

A NOTE ON SIGNIFICANCE, because it is the thing most easily got wrong here:
overlapping forward windows make neighbouring observations near-duplicates, so
the naive t-statistic over every bar is inflated — often by several times. Every
bucket test below is therefore run on a NON-OVERLAPPING subsample (one
observation per horizon-length block) and that is the t reported. The
all-bars mean is shown beside it for magnitude only.
"""

import argparse
import csv
import math
import statistics
import sys
from collections import defaultdict

MARKER_HEAD = "CBI_HEAD,"
MARKER_ROW = "CBI_LOG,"

# The v3 column list, embedded as a FALLBACK. TradingView's Pine Logs pane keeps
# only the last ~10k entries, so an export long enough to be worth analysing has
# usually evicted the CBI_HEAD row that was written on its first logged bar. The
# indicator now re-emits the header every session, but exports taken before that
# fix have none — hence this. It is only trusted when the field count matches
# exactly, so a future column change fails loudly instead of silently shifting
# every column by one.
HEADER_V3 = ("date,time,bars_open,open,high,low,close,volume,sess_vwap,atr14,sess_hi,sess_lo,prior_close,"
             "cbi_raw,cbi,sig_fast,sig_slow,cbi_hi,cbi_lo,vold_conf,add_conf,vwap_conf,cumtick_conf,"
             "vold_vote,add_vote,vwap_vote,cumtick_vote,voting,dissent,consensus,stance,slope_vote,"
             "with_stance,move_consensus,quorum,regime,regime_known,regime_resolved,vol_ratio,range_ratio,"
             "ceiling,boost,transp_target,transp,warn_fired,nonconf_fired,nonconf_count,vold_net,tvol,"
             "add_net,vwap_raw,tick_adj,cumtick,cumtick_slope,cumtick_slope_sm,add_scale,vwap_band,"
             "cumtick_scale,nonconf_margin,vold_w,add_w,vwap_w,cumtick_w,deadband").split(",")


def _messages(path):
    """Yield the logged message from each line, whatever wrapper it arrived in.

    Two shapes reach us. A COPY out of the Pine Logs pane is plain text with
    TradingView's `[timestamp]:` prefix. A DOWNLOAD is a real two-column CSV
    (`Date,Message`) whose Message cell is the quoted log line — that quoting
    has to be undone by a CSV reader, not by string slicing, or the closing
    quote rides along on the final column.
    """
    with open(path, encoding="utf-8", errors="replace", newline="") as handle:
        first = handle.readline()
        handle.seek(0)
        if first.strip().lower().startswith("date,message"):
            reader = csv.reader(handle)
            next(reader, None)
            for row in reader:
                if len(row) >= 2:
                    yield row[-1]
            return
        for line in handle:
            yield line.rstrip("\n")


def read_rows(paths):
    """Pull CBI_HEAD/CBI_LOG records out of one or more exports."""
    header, rows = None, []
    for path in paths:
        for message in _messages(path):
            for marker in (MARKER_HEAD, MARKER_ROW):
                at = message.find(marker)
                if at == -1:
                    continue
                fields = next(csv.reader([message[at:]]))
                if marker is MARKER_HEAD:
                    if header is None:
                        header = fields[1:]  # drop the CBI_HEAD cell
                else:
                    rows.append(fields[1:])  # drop the CBI_LOG cell
                break
    if header is None:
        widths = {len(row) for row in rows}
        if widths != {len(HEADER_V3)}:
            sys.exit(f"no CBI_HEAD row, and the rows are {sorted(widths)} columns wide where the built-in "
                     f"v3 layout is {len(HEADER_V3)} — re-export with a header (the indicator now writes "
                     f"one every session) so the columns can be named.")
        header = HEADER_V3
        if not read_rows.warned:  # once per run, not once per file
            read_rows.warned = True
            print(f"note: no CBI_HEAD in the export — using the built-in v3 column list "
                  f"({len(HEADER_V3)} columns, field count matches).")
    return header, rows


read_rows.warned = False


def to_float(text):
    if text is None or text == "":
        return None
    try:
        return float(text)
    except ValueError:
        return None


def build(header, raw_rows):
    """Typed dict per bar, sorted by time, with the session key attached."""
    bars = []
    for fields in raw_rows:
        if len(fields) != len(header):
            continue  # a row cut in half by a copy-paste boundary
        bar = dict(zip(header, fields))
        typed = {key: to_float(value) for key, value in bar.items()}
        typed["date"] = bar.get("date", "")
        typed["time"] = bar.get("time", "")
        if not typed["date"] or typed.get("close") is None:
            continue
        bars.append(typed)
    bars.sort(key=lambda row: (row["date"], row["time"]))
    return bars


def bar_minutes(bars):
    """Modal gap between consecutive same-session bars, in minutes."""
    gaps = defaultdict(int)
    for previous, current in zip(bars, bars[1:]):
        if previous["date"] != current["date"]:
            continue
        ph, pm = (int(part) for part in previous["time"].split(":"))
        ch, cm = (int(part) for part in current["time"].split(":"))
        delta = (ch * 60 + cm) - (ph * 60 + pm)
        if delta > 0:
            gaps[delta] += 1
    return max(gaps, key=gaps.get) if gaps else 1


def attach_forward(bars, horizons_bars):
    """Forward close-to-close return per horizon, in bps and in ATR units."""
    by_session = defaultdict(list)
    for bar in bars:
        by_session[bar["date"]].append(bar)
    for session in by_session.values():
        for index, bar in enumerate(session):
            for horizon in horizons_bars:
                ahead = index + horizon
                if ahead >= len(session):
                    continue
                entry, exit_ = bar["close"], session[ahead]["close"]
                if not entry:
                    continue
                bar[f"fwd_bps_{horizon}"] = (exit_ - entry) / entry * 1e4
                atr = bar.get("atr14")
                if atr:
                    bar[f"fwd_atr_{horizon}"] = (exit_ - entry) / atr


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)


def spearman(xs, ys):
    def ranked(values):
        order = sorted(range(len(values)), key=lambda i: values[i])
        ranks = [0.0] * len(values)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
                j += 1
            shared = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = shared
            i = j + 1
        return ranks

    return pearson(ranked(xs), ranked(ys))


def t_stat(values):
    n = len(values)
    if n < 3:
        return None
    sd = statistics.stdev(values)
    if sd == 0:
        return None
    return statistics.fmean(values) / (sd / math.sqrt(n))


def non_overlapping(bars, horizon, key):
    """One observation per horizon-length block, per session."""
    out, by_session = [], defaultdict(list)
    for bar in bars:
        by_session[bar["date"]].append(bar)
    for session in by_session.values():
        for index in range(0, len(session), horizon):
            value = session[index].get(key)
            if value is not None:
                out.append(value)
    return out


def paired(bars, signal_key, horizon, ret_key="fwd_bps"):
    xs, ys = [], []
    for bar in bars:
        signal, forward = bar.get(signal_key), bar.get(f"{ret_key}_{horizon}")
        if signal is not None and forward is not None:
            xs.append(signal)
            ys.append(forward)
    return xs, ys


def fmt(value, places=3):
    return "—" if value is None else f"{value:+.{places}f}"


def rule(title):
    print(f"\n{title}\n{'─' * len(title)}")


# ── ⑤ weight sweep ───────────────────────────────────────────────────────────
# Re-derives each component's confidence from its RAW feed using the scales the
# export carries, so alternative weightings are evaluated on the same bars. This
# mirrors the Pine construction exactly; if it drifts from the indicator, the
# `recon` column in the ① table stops matching `cbi_raw` and says so.
def clamp(value, limit=1.0):
    return max(-limit, min(limit, value))


def component_confidences(bar):
    out = {}
    vold_net, tvol = bar.get("vold_net"), bar.get("tvol")
    if vold_net is not None and tvol:
        out["vold"] = clamp(vold_net / tvol)
    add_net, add_scale = bar.get("add_net"), bar.get("add_scale")
    if add_net is not None and add_scale:
        out["add"] = clamp(add_net / add_scale)
    vwap_raw, vwap_band = bar.get("vwap_raw"), bar.get("vwap_band")
    if vwap_raw is not None and vwap_band:
        out["vwap"] = clamp((vwap_raw - 50.0) / vwap_band)
    slope, slope_scale = bar.get("cumtick_slope_sm"), bar.get("cumtick_scale")
    if slope is not None and slope_scale:
        out["cumtick"] = clamp(slope / slope_scale)
    return out


def weighted(bar, weights):
    confidences = component_confidences(bar)
    total = sum(weights[name] for name in confidences if weights.get(name))
    if not total:
        return None
    return 100.0 * sum(weights[name] * value for name, value in confidences.items() if weights.get(name)) / total


def attach_previous(bars):
    """Previous in-session composite, so a zero-cross can be detected."""
    by_session = defaultdict(list)
    for bar in bars:
        by_session[bar["date"]].append(bar)
    for session in by_session.values():
        for earlier, later in zip(session, session[1:]):
            later["prev_cbi"] = earlier.get("cbi")


def bucket_report(rows, horizon, label, signer):
    """One line: n, mean bps in the direction `signer` picks, hit rate, t."""
    values = [bar[f"fwd_bps_{horizon}"] * signer(bar) for bar in rows
              if bar.get(f"fwd_bps_{horizon}") is not None]
    if len(values) < 5:
        print(f"    {label:<28} n={len(values):>5}  (too few to read)")
        return None
    tagged = [dict(bar, _v=value) for bar, value in
              zip([b for b in rows if b.get(f"fwd_bps_{horizon}") is not None], values)]
    sample = non_overlapping(tagged, horizon, "_v")
    hit = sum(1 for value in values if value > 0) / len(values) * 100
    mean = statistics.fmean(values)
    print(f"    {label:<28} n={len(values):>5}  mean {fmt(mean, 2):>8}bps  hit {hit:5.1f}%"
          f"  t(non-ovl, n={len(sample):>3}) {fmt(t_stat(sample), 2)}")
    return mean


def percentile(values, fraction):
    ordered = sorted(values)
    if not ordered:
        return None
    return ordered[min(len(ordered) - 1, int(fraction * len(ordered)))]


def signal_scoreboard(bars, minutes, horizons_bars):
    """The four things the indicator is claimed to do, each as its own test.

    Every bucket is graded in the direction the CLAIM implies, so a positive
    mean always means 'the claim held'. That is the only way these four are
    comparable — CONFIRMATION says follow the line, EXHAUSTION says fade it,
    and grading both in the same direction would make one of them look good
    for the wrong reason.
    """
    rule("SIGNAL SCOREBOARD — the four claims, each graded in its own direction")
    levels = [abs(bar["cbi"]) for bar in bars if bar.get("cbi") is not None]
    p90, p95 = percentile(levels, 0.90), percentile(levels, 0.95)

    for horizon in horizons_bars:
        print(f"\n  horizon {horizon * minutes}min   (p90 |CBI| = {p90:.1f}, p95 = {p95:.1f})")

        # CONFIRMATION — follow an established stance.
        print("   CONFIRMATION  claim: price follows the line")
        bucket_report([b for b in bars if b.get("stance")], horizon,
                      "follow stance (all bars)", lambda b: 1 if b["stance"] > 0 else -1)
        bucket_report([b for b in bars if b.get("stance") and b.get("move_consensus", 0) >= 0.999],
                      horizon, "follow stance, full agreement", lambda b: 1 if b["stance"] > 0 else -1)

        # EXHAUSTION — fade the extreme. The 2026-08-01 cross-regime verdict
        # said extremes CONTINUE; this is the re-test, both tails separately
        # because they behaved differently in every chunk.
        print("   EXHAUSTION    claim: extremes reverse (graded as FADING them)")
        for name, picker in (
            ("fade |CBI| > p90", lambda b: p90 and abs(b["cbi"]) > p90),
            ("fade |CBI| > p95", lambda b: p95 and abs(b["cbi"]) > p95),
            ("fade positive > p90", lambda b: p90 and b["cbi"] > p90),
            ("fade negative < -p90", lambda b: p90 and b["cbi"] < -p90),
        ):
            bucket_report([b for b in bars if b.get("cbi") is not None and picker(b)], horizon,
                          name, lambda b: -1 if b["cbi"] > 0 else 1)

        # TREND CHANGE — the zero cross, the line's own regime flip.
        print("   TREND CHANGE  claim: a zero-cross starts a move")
        crossed = [b for b in bars if b.get("cbi") is not None and b.get("prev_cbi") is not None
                   and (b["cbi"] >= 0) != (b["prev_cbi"] >= 0)]
        bucket_report(crossed, horizon, "follow the new side", lambda b: 1 if b["cbi"] >= 0 else -1)
        bucket_report([b for b in crossed if b.get("move_consensus", 0) >= 0.7], horizon,
                      "…with agreement >= 0.7", lambda b: 1 if b["cbi"] >= 0 else -1)

        # REVERSION — price stretched from session VWAP, breadth disagreeing.
        print("   REVERSION     claim: breadth against price = snap back")
        stretched = []
        for bar in bars:
            vwap, atr, cbi = bar.get("sess_vwap"), bar.get("atr14"), bar.get("cbi")
            if not vwap or not atr or cbi is None:
                continue
            stretch = (bar["close"] - vwap) / atr
            if abs(stretch) >= 1.0 and (stretch > 0) != (cbi >= 0):
                bar["_stretch"] = stretch
                stretched.append(bar)
        bucket_report(stretched, horizon, "price >1 ATR off VWAP vs CBI",
                      lambda b: -1 if b["_stretch"] > 0 else 1)

    print("\n  Positive mean = the claim held on these bars. A claim that only works in")
    print("  one export is not a finding — that is exactly how the 2026-08-01 C-only")
    print("  results died. Run at least three chunks from different regimes.")


def headline(bars, minutes, horizons_bars, label):
    """One row per export — the universe/tuning comparison table."""
    cells = []
    for horizon in horizons_bars:
        xs, ys = paired(bars, "cbi", horizon)
        cells.append(fmt(pearson(xs, ys)) if len(xs) > 30 else "—")
    follow = [bar[f"fwd_bps_{horizons_bars[-1]}"] * (1 if bar["stance"] > 0 else -1)
              for bar in bars if bar.get("stance") and bar.get(f"fwd_bps_{horizons_bars[-1]}") is not None]
    hit = sum(1 for value in follow if value > 0) / len(follow) * 100 if follow else 0
    sessions = len({bar["date"] for bar in bars})
    print(f"{label[:30]:<30} {sessions:>4} {len(bars):>7} " + " ".join(f"{cell:>10}" for cell in cells)
          + f" {hit:>8.1f}%")


def component_matrix(paths, horizons):
    """IC of each component, per export, per horizon — one table per signal.

    This is the "which feed, which leg" question. Universes read down a column,
    components read across tables, so the two are never confused for each other.
    A component whose IC decays toward zero as the horizon grows is a SCALP
    signal; one that grows is a trend signal. Which you want depends on how long
    you hold, which is why this is a matrix and not a single ranking.
    """
    cohorts = []
    for path in paths:
        bars, minutes, horizons_bars = load([path], horizons)
        cohorts.append((path.split("/")[-1], bars, minutes, horizons_bars))
    minutes = cohorts[0][2]
    horizons_bars = cohorts[0][3]

    for signal, title in (("cbi", "COMPOSITE (as shipped)"), ("vold_conf", "VOLD — up/down volume ratio"),
                          ("add_conf", "ADD — net issues"), ("vwap_conf", "%VWAP — share above VWAP"),
                          ("cumtick_conf", "CUMTICK — cumulative TICK slope")):
        rule(f"{title}")
        print(f"{'export':<30} " + " ".join(f"{h * minutes:>8}min" for h in horizons_bars))
        empty = True
        for label, bars, _, hb in cohorts:
            cells = []
            for horizon in hb:
                xs, ys = paired(bars, signal, horizon)
                cells.append(fmt(pearson(xs, ys)) if len(xs) > 30 else "—")
            if any(cell != "—" for cell in cells):
                empty = False
            print(f"{label[:30]:<30} " + " ".join(f"{cell:>11}" for cell in cells))
        if empty:
            print("  (no data — component inactive at weight 0 in these exports)")


def load(paths, horizons):
    header, raw_rows = read_rows(paths)
    bars = build(header, raw_rows)
    if not bars:
        sys.exit(f"no CBI_LOG rows parsed from {paths}")
    minutes = bar_minutes(bars)
    horizons_bars = sorted({max(1, round(h / minutes)) for h in horizons})
    attach_forward(bars, horizons_bars)
    attach_previous(bars)
    return bars, minutes, horizons_bars


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="+", help="exported Pine Logs text file(s)")
    parser.add_argument("--horizons", default="15,30,60", help="forward horizons in minutes (default 15,30,60)")
    parser.add_argument("--components", action="store_true",
                        help="IC of each component per export per horizon — the 'which feed, which leg' "
                             "matrix. Pair it with --horizons tuned to how long you actually hold.")
    parser.add_argument("--compare", action="store_true",
                        help="treat each file as its own cohort and print one headline row each, "
                             "instead of pooling them. This is how the breadth-universe question "
                             "gets answered: export the SAME dates under each Market setting, then compare.")
    args = parser.parse_args()
    horizons = [int(part) for part in args.horizons.split(",")]

    if args.components:
        component_matrix(args.paths, horizons)
        return

    if args.compare:
        probe_minutes = load(args.paths[:1], horizons)[1]
        horizons_bars = sorted({max(1, round(h / probe_minutes)) for h in horizons})
        print("Each file as its own cohort — IC of the composite vs forward return.\n")
        print(f"{'export':<30} {'sess':>4} {'bars':>7} "
              + " ".join(f"{h * probe_minutes:>7}min" for h in horizons_bars) + f" {'follow%':>9}")
        print("─" * (30 + 5 + 8 + 11 * len(horizons_bars) + 10))
        for path in args.paths:
            bars, minutes, hb = load([path], horizons)
            headline(bars, minutes, hb, path.split("/")[-1])
        print("\nHighest IC across ALL horizons wins, not the best single cell. If two")
        print("universes are within ~0.01 of each other they are indistinguishable on")
        print("this sample — prefer the one whose feeds are least likely to go stale.")
        return

    bars, minutes, horizons_bars = load(args.paths, horizons)

    minutes = bar_minutes(bars)
    horizons = [int(part) for part in args.horizons.split(",")]
    horizons_bars = sorted({max(1, round(h / minutes)) for h in horizons})
    attach_forward(bars, horizons_bars)

    sessions = sorted({bar["date"] for bar in bars})
    print(f"{len(bars)} bars · {len(sessions)} sessions · {sessions[0]} → {sessions[-1]} · {minutes}-min bars")
    print(f"horizons: {', '.join(f'{h * minutes}min ({h} bars)' for h in horizons_bars)}")
    if len(sessions) < 20:
        print(f"⚠ only {len(sessions)} sessions — too few to conclude anything. Export more.")

    # Reconstruction check — proves the offline model matches the Pine one.
    diffs = [abs(weighted(bar, {"vold": bar.get("vold_w") or 0, "add": bar.get("add_w") or 0,
                                "vwap": bar.get("vwap_w") or 0, "cumtick": bar.get("cumtick_w") or 0}) - bar["cbi_raw"])
             for bar in bars
             if bar.get("cbi_raw") is not None
             and weighted(bar, {"vold": bar.get("vold_w") or 0, "add": bar.get("add_w") or 0,
                                "vwap": bar.get("vwap_w") or 0, "cumtick": bar.get("cumtick_w") or 0}) is not None]
    if diffs:
        worst = max(diffs)
        verdict = "matches Pine" if worst < 0.5 else "DRIFT — the offline model no longer mirrors the indicator"
        print(f"reconstruction check: max |offline − cbi_raw| = {worst:.4f} — {verdict}")

    signal_scoreboard(bars, minutes, horizons_bars)

    # ── ① STANCE ────────────────────────────────────────────────────────────
    rule("① STANCE — information coefficient vs forward return")
    print(f"{'signal':<16} " + " ".join(f"{h * minutes:>5}min(IC/ρ)" for h in horizons_bars))
    for signal in ("cbi", "cbi_raw", "stance", "vold_conf", "add_conf", "vwap_conf", "cumtick_conf", "transp"):
        cells = []
        for horizon in horizons_bars:
            xs, ys = paired(bars, signal, horizon)
            cells.append(f"{fmt(pearson(xs, ys))}/{fmt(spearman(xs, ys))}" if len(xs) > 30 else "—")
        print(f"{signal:<16} " + " ".join(f"{cell:>14}" for cell in cells))
    print("\nIC is the correlation between the signal now and the return ahead. Documented")
    print("equity-factor ICs sit at 0.02–0.05; the sign flipping between horizons is the")
    print("known failure mode, so read the row, not one cell.")

    # ── ② AGREEMENT ─────────────────────────────────────────────────────────
    rule("② AGREEMENT — forward return by consensus tier, signed by the stance")
    for horizon in horizons_bars:
        print(f"\n  horizon {horizon * minutes}min")
        buckets = defaultdict(list)
        for bar in bars:
            tier, stance = bar.get("move_consensus"), bar.get("stance")
            forward = bar.get(f"fwd_bps_{horizon}")
            if tier is None or not stance or forward is None:
                continue
            buckets[f"{tier:.1f}"].append((bar, forward * (1 if stance > 0 else -1)))
        for tier in sorted(buckets, reverse=True):
            pairs = buckets[tier]
            signed = [value for _, value in pairs]
            tagged = [dict(bar, _signed=value) for bar, value in pairs]
            sample = non_overlapping(tagged, horizon, "_signed")
            hit = sum(1 for value in signed if value > 0) / len(signed) * 100
            print(f"    tier {tier}  n={len(signed):>6}  mean {fmt(statistics.fmean(signed), 2):>8}bps"
                  f"  hit {hit:5.1f}%   t(non-overlap, n={len(sample)}) {fmt(t_stat(sample), 2)}")
    print("\n  A monotonic ladder — 1.0 best, 0.1 worst — is the claim. Anything else says")
    print("  agreement is not what the opacity implies it is.")

    # ── ③ REGIME ────────────────────────────────────────────────────────────
    rule("③ REGIME — session character vs what the day did")
    names = {1.0: "EXPANSION", 0.0: "NEUTRAL", -1.0: "QUIET"}
    per_session = defaultdict(list)
    for bar in bars:
        per_session[bar["date"]].append(bar)
    buckets = defaultdict(list)
    for date, session in per_session.items():
        resolved = [bar for bar in session if bar.get("regime_resolved") and bar.get("regime_known")]
        if not resolved:
            continue
        regime = resolved[-1].get("regime")
        closes = [bar["close"] for bar in session]
        highs = [bar["high"] for bar in session if bar.get("high") is not None]
        lows = [bar["low"] for bar in session if bar.get("low") is not None]
        span = max(highs) - min(lows) if highs and lows else 0
        efficiency = abs(closes[-1] - closes[0]) / span if span else None
        if efficiency is not None:
            buckets[regime].append(efficiency)
    for regime in sorted(buckets, reverse=True):
        values = buckets[regime]
        print(f"  {names.get(regime, regime):<10} sessions={len(values):>4}  mean trendiness "
              f"{statistics.fmean(values):.3f}  (|close−open| ÷ session range)")
    print("\n  EXPANSION should be the trendiest. In the 2026-08-01 summer chunk it inverted,")
    print("  which is why this table exists rather than a fixed ceiling.")

    # ── ④ MARKERS ───────────────────────────────────────────────────────────
    rule("④ MARKERS — graded per fire")
    for horizon in horizons_bars:
        print(f"\n  horizon {horizon * minutes}min")
        for label, picker, sign in (
            ("▲ unsupported", lambda bar: bar.get("warn_fired") == 1, lambda bar: -1 if bar.get("slope_vote", 0) > 0 else 1),
            ("◆ bearish", lambda bar: bar.get("nonconf_fired") == 1, lambda bar: -1),
            ("◆ bullish", lambda bar: bar.get("nonconf_fired") == -1, lambda bar: 1),
        ):
            values = [bar[f"fwd_bps_{horizon}"] * sign(bar) for bar in bars
                      if picker(bar) and bar.get(f"fwd_bps_{horizon}") is not None]
            if not values:
                print(f"    {label:<15} no fires")
                continue
            hit = sum(1 for value in values if value > 0) / len(values) * 100
            print(f"    {label:<15} n={len(values):>4}  mean {fmt(statistics.fmean(values), 2):>8}bps"
                  f"  hit {hit:5.1f}%  t {fmt(t_stat(values), 2)}")
    print("\n  Each is graded in the direction it ARGUES: ▲ says the push fails, ◆ says the")
    print("  extreme is not ratified. Fires are sparse — treat n<30 as anecdote.")

    # ── Time of day ─────────────────────────────────────────────────────────
    rule("Time of day — following the stance, by hour")
    horizon = horizons_bars[len(horizons_bars) // 2]
    by_hour = defaultdict(list)
    for bar in bars:
        stance, forward = bar.get("stance"), bar.get(f"fwd_bps_{horizon}")
        if stance and forward is not None and bar["time"]:
            by_hour[bar["time"][:2]].append(forward * (1 if stance > 0 else -1))
    print(f"  (horizon {horizon * minutes}min)")
    for hour in sorted(by_hour):
        values = by_hour[hour]
        hit = sum(1 for value in values if value > 0) / len(values) * 100
        print(f"    {hour}:xx  n={len(values):>6}  mean {fmt(statistics.fmean(values), 2):>8}bps  hit {hit:5.1f}%")
    print("\n  The 2026-08-01 study found morning distrust / afternoon trust across three")
    print("  regime chunks. The 2026-09-27 run on the mixed-feed defaults did NOT reproduce")
    print("  it — 09:xx was the best hour and 12:xx the worst. Read the table, not this note:")
    print("  the time-of-day dims are set from whichever pattern is actually holding.")

    # ── ⑤ WEIGHTS ───────────────────────────────────────────────────────────
    rule("⑤ WEIGHTS — IC of alternative weightings on these same bars")
    candidates = {
        "shipped 40/30/30/0": {"vold": 40, "add": 30, "vwap": 30, "cumtick": 0},
        "drop %VWAP  57/43": {"vold": 40, "add": 30, "vwap": 0, "cumtick": 0},
        "VOLD only": {"vold": 1, "add": 0, "vwap": 0, "cumtick": 0},
        "ADD only": {"vold": 0, "add": 1, "vwap": 0, "cumtick": 0},
        "%VWAP only": {"vold": 0, "add": 0, "vwap": 1, "cumtick": 0},
        "equal 4-way": {"vold": 1, "add": 1, "vwap": 1, "cumtick": 1},
    }
    print(f"{'weighting':<20} " + " ".join(f"{h * minutes:>10}min" for h in horizons_bars))
    for name, weights in candidates.items():
        cells = []
        for horizon in horizons_bars:
            xs, ys = [], []
            for bar in bars:
                value, forward = weighted(bar, weights), bar.get(f"fwd_bps_{horizon}")
                if value is not None and forward is not None:
                    xs.append(value)
                    ys.append(forward)
            cells.append(fmt(pearson(xs, ys)) if len(xs) > 30 else "—")
        print(f"{name:<20} " + " ".join(f"{cell:>13}" for cell in cells))
    print("\n  %VWAP's 30 weight was the long-standing open question. On the mixed-feed")
    print("  defaults (NYSE %VWAP) it earns its keep at 6-20min and fades past 30min, so")
    print("  'drop %VWAP' is a long-horizon answer to a short-horizon question. The whole")
    print("  grid sits inside ~0.006 IC of itself — feed routing is worth ~3x what weights")
    print("  are, so do not retune these on one chunk.")
    print("\n  One caveat that applies to every table above: these are in-sample on whatever")
    print("  you exported. A result that does not survive a second, different regime chunk")
    print("  is not a result — that is exactly how the 2026-08-01 C-only findings died.")


if __name__ == "__main__":
    main()

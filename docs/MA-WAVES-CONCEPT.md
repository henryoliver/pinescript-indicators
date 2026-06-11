# MA & Waves

This indicator implements Barry Burns' Top Dog Trading price-wave method.

It is **not** Elliott Wave. There is no required 5-wave structure. A trend can have 3, 5, 7, 9, or more waves. The purpose of the count is to measure **trend maturity**, not to force price into a predefined pattern.

## Core Concepts

### Trend
- Trend has 3 states: `UP`, `DOWN`, `FLAT`.
- Trend is defined by the **50-period simple moving average slope**.
- It is **not** defined by higher highs / higher lows or lower lows / lower highs.
- `UP`: 50 SMA is clearly angling up.
- `DOWN`: 50 SMA is clearly angling down.
- `FLAT`: 50 SMA is effectively horizontal.

### Cycles
- Cycles are defined from **Stochastic %D** using the `45 / 55` zone.
- **High cycle**:
  - Starts when `%D` crosses above `45`, or crosses back above `55` while a low cycle is active.
  - The **highest high** made while `%D` remains above `45` is the cycle high.
  - The cycle ends when the opposite low cycle begins.
- **Low cycle**:
  - Starts when `%D` crosses below `55`, or crosses back below `45` while a high cycle is active.
  - The **lowest low** made while `%D` remains below `55` is the cycle low.
  - The cycle ends when the opposite high cycle begins.
- When a new cycle is recognized, the true extreme can still be the **previous bar** if that bar is the highest high or lowest low for the cycle.
- If multiple bars in the same half cycle print the exact same high or low, break the tie by the **close**:
  - high-side tie: prefer the bar with the **higher close**
  - low-side tie: prefer the bar with the **lower close**
- If both price and close are equal, the later bar wins.
- Every wave extreme is a cycle extreme, but **not every cycle extreme is a wave**.
- A new cycle must not start plotting on the same bar that already holds the confirmed plot from the previous half cycle.

### Waves
- Odd numbers are **with-trend impulse waves**: `1, 3, 5, 7, 9...`
- Even numbers are **counter-trend retrace waves**: `2, 4, 6, 8...`
- In an `UP` trend:
  - Odd waves are cycle highs.
  - Even waves are cycle lows.
- In a `DOWN` trend:
  - Odd waves are cycle lows.
  - Even waves are cycle highs.

## Anchor Rules

### Wave 1
- `Wave 1 DOWN` = first **cycle low** after the 50 SMA starts angling down.
- `Wave 1 UP` = first **cycle high** after the 50 SMA starts angling up.
- Wave 1 has nothing to do with prior highs or lows.
- If the trend starts while the correct cycle is already active, wave 1 starts **immediately on that bar close** inside the current cycle.
- Wave 1 only qualifies if the first impulse cycle gets a bar where **more than 50% of the real body** is on the correct side of the 50 SMA:
  - `UP`: more than 50% of the real body must be **above** the 50 SMA
  - `DOWN`: more than 50% of the real body must be **below** the 50 SMA
- This rule applies in realtime as well: the first impulse should not start plotting until the body-majority condition is met.
- If that first with-trend cycle never gets a bar that meets this condition, it does not count as wave 1.
- If the first cycle after a reset is the wrong direction, it gets no wave number.

### Wave 2
- Wave 2 is the first valid retrace after wave 1.
- It does **not** need to compare against a prior retrace wave.

## Impulse Wave Qualification

This is the main qualification rule, and it applies to **odd waves after wave 1**.

### In an UP trend
- A cycle high can become wave `3`, `5`, `7`, etc. only if:
  - the cycle makes a **higher high** than the prior confirmed odd wave high, and
  - **at least one bar inside that cycle** has its real body above the prior confirmed odd wave high.

### In a DOWN trend
- A cycle low can become wave `3`, `5`, `7`, etc. only if:
  - the cycle makes a **lower low** than the prior confirmed odd wave low, and
  - **at least one bar inside that cycle** has its real body below the prior confirmed odd wave low.

### Real Body Rule
- Use the **real body**, not the wick alone.
- “Real body past” means both:
  - `open` is on the trend-confirming side of the prior odd-wave extreme
  - `close` is on the trend-confirming side of the prior odd-wave extreme
- Equality is not enough for a confirmed odd wave. It must be **past** the prior odd-wave extreme.
- The qualifying real-body bar does **not** need to be the final cycle extreme bar.
- The wave label still belongs on the **final extreme of the cycle**.

## Failed Waves

Failed waves apply to **odd waves only**.

- A failed wave happens when price pushes past the prior confirmed odd-wave extreme with the wick, but the **real body** does not confirm.
- In other words, the cycle made the required higher high / lower low, but **no bar in the cycle** achieved the required real-body break.
- Label format: `F3`, `F5`, `F7`, etc.
- Failed waves do **not** advance the wave count.
- There is no `F1` or `F2`.

## Complex Retraces

Even waves are **not** separately validated against prior even waves. There is no independent “higher low / lower high retrace qualification” rule in the Barry Burns description.

Instead:

- A **retrace zone** is everything between two confirmed odd waves.
- Inside that zone, multiple counter-trend cycles can print.
- Those cycles are labeled `a`, `b`, `c`, `d`, `e`, ... in time order.
- The **most extreme retrace cycle** in that zone becomes the even wave.

That means:
- In an `UP` trend, the even wave is the **lowest cycle low** between two confirmed odd highs.
- In a `DOWN` trend, the even wave is the **highest cycle high** between two confirmed odd lows.

Examples:
- Wave 2 = most extreme retrace between waves 1 and 3.
- Wave 4 = most extreme retrace between waves 3 and 5.
- Wave 6 = most extreme retrace between waves 5 and 7.

So the even-wave rule is:
- **wave 2/4/6/8 = most extreme counter-trend cycle inside the active retrace zone**

## Labeling Model

- Odd confirmed waves show their number only.
- Failed odd waves show `F` + the attempted number.
- For wave-number placement, the immediately previous bar can take the wave label if it is more extreme than the current half-cycle extreme bar:
  - higher high for high-side waves
  - lower low for low-side waves
- This previous-bar override can apply even if that bar is not the bar chosen as the formal cycle extreme.
- In live plotting, a wave/F-wave number stays on the current best higher high / lower low inside the active cycle.
- It only moves when a later bar in that same cycle makes a more extreme price.
- There should never be two active plots of the same wave number in the same trend. When ownership changes, the prior live label must be cleared.
- Complex retrace cycles can show letters `a-z`.
- Retrace letters use a different anchor rule from waves:
  - the label bar must be a bar that **closes back inside** the cycle high or cycle low
  - the letter does not have to sit on the cycle extreme bar
- A retrace letter should not print before that inside-close anchor exists.
- The first retrace letter `a` stays hidden until `b` is confirmed.
- As soon as `b` is confirmed, `a` is backfilled onto the first retrace in its correct earlier place.
- After that, `b`, `c`, `d`, ... must plot in realtime as their own retrace cycles confirm.
- Before `b` exists, the live best retrace shows only its even-wave number.
- After `b` exists, the current best retrace can show letter + even number, and non-best retraces show letter-only.
- If a later retrace becomes more extreme, the even-wave label moves to that later cycle and the previous owner falls back to letter-only.

## Reset Rule

- The count resets on the **confirmed bar close** where the 50 SMA state changes.
- If the active cycle already matches the new trend direction, wave 1 is seeded immediately on that same bar close.
- If trend becomes `FLAT`, counting pauses until `UP` or `DOWN` returns.

## Trend Maturity Interpretation

- `3` waves: minimum real trend
- `5` waves: average trend
- `7` or `9` waves: extended trend
- `> 9` waves: mega trend

The count is a maturity gauge, not a standalone signal.

## Practical Summary

The clean logic is:

1. Determine trend from the 50 SMA: `UP`, `DOWN`, or `FLAT`.
2. Build cycles from `%D` using the `45 / 55` zone.
3. Start wave 1 from the first with-trend cycle after the SMA turns.
4. Confirm later odd waves only when wick + **real body** break the prior odd-wave extreme.
5. Mark wick-only failures as `F` waves.
6. Treat all in-between counter-trend cycles as retrace-zone members.
7. Assign the even wave to the most extreme retrace in that zone.

That is the model the indicator should follow.

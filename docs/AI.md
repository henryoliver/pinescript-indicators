# AI Assistant Instructions for Pine Script Indicators

This document provides comprehensive guidance for AI assistants (LLMs) working with Pine Script indicators in this repository.

---

## 🎯 Repository Overview

This repository contains **Pine Script v6 indicators** for TradingView that display fundamental and technical analysis metrics. All indicators follow strict coding conventions and share a consistent architecture and Nord color theme.

**Key Characteristics:**
- **Language**: Pine Script v6
- **Platform**: TradingView
- **Purpose**: Overlay indicators with customizable table/label displays
- **Theme**: Nord color palette (NORD0-NORD15)
- **Style**: Emoji-prefixed sections, explicit parameter naming, meaningful variable names

---

## 📚 Essential Documentation References

### ⚠️ MANDATORY - Read Before ANY Code Changes

**You MUST consult these references BEFORE making any changes to `.pine` files:**

1. **Pine Script v6 LLM-Optimized Documentation**
   - Repository: https://github.com/codenamedevan/pinescriptv6
   - Master Index: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/LLM_MANIFEST.md
   - **Purpose**: AI-optimized Pine Script v6 documentation designed to prevent hallucinations

2. **Official Pine Script Documentation**
   - Guide: https://www.tradingview.com/pine-script-docs/welcome/
   - v6 Reference: https://www.tradingview.com/pine-script-reference/v6/
   - **Critical**: Use for verifying function signatures and parameter names

3. **Repainting Concepts**
   - https://www.tradingview.com/pine-script-docs/concepts/repainting/
   - **Critical**: Understanding bar-by-bar recalculation and data accuracy

---

## 🗺️ LLM Documentation Navigation Strategy

### Primary Entry Point
**Always start with**: [`LLM_MANIFEST.md`](https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/LLM_MANIFEST.md)

This is the master navigation map for Pine Script v6 documentation optimized for AI consumption.

### Modular Retrieval Protocol

**CRITICAL**: Do NOT attempt to load entire documentation at once. Use **targeted retrieval** based on query type.

#### Query-to-Documentation Routing

| Query Type | Primary Files to Fetch |
|-----------|------------------------|
| **Technical Indicators** (RSI, EMA, SMA, MACD) | `reference/functions/ta.md` |
| **Backtesting/Strategies** | `reference/functions/strategy.md` |
| **Financial Data** (earnings, fundamentals) | `reference/functions/request.md` |
| **Drawing/Plotting** (lines, labels, tables, shapes) | `reference/functions/drawing.md` |
| **Arrays/Collections** | `reference/functions/collections.md` |
| **Built-in Variables** (bar_index, close, volume) | `reference/variables.md` |
| **Constants** (colors, styles, positions) | `reference/constants.md` |
| **Execution Issues** (var keyword, bar execution) | `concepts/execution_model.md` |
| **Repainting/Multi-timeframe** | `concepts/timeframes.md` |
| **Footprint/Volume Profile** | `reference/functions/request.md` |
| **Compile/Runtime Errors** | `concepts/common_errors.md` |

#### Example Fetch URLs

```
# Technical analysis functions
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/ta.md

# Financial data (request.financial, request.earnings)
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/request.md

# Table/plotting functions
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/drawing.md

# Execution model (var keyword, bar-by-bar)
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/concepts/execution_model.md
```

### When to Fetch Documentation

Fetch documentation when:
- User asks about a specific Pine Script function you're unsure about
- Compilation errors occur that might be related to v6 syntax
- User asks "how do I..." questions about functionality
- You need to verify parameter names or function signatures
- **Before suggesting ANY function or syntax pattern**

---

## 🏗️ Repository Architecture & Patterns

### Standard File Structure

Every indicator follows this structure:

```pine
// Mozilla Public License 2.0 header
// © henry_oliver

//@version=6
indicator(title = "Full Name", shorttitle = "🎯 ABC", overlay = true)

// ═════════════════════════════════════════════════════════════════════════════
// 🧱 CONSTANTS
// Shared immutable values used by the indicator, including the Nord palette.
// ═════════════════════════════════════════════════════════════════════════════
// Nord Theme Color
// Polar Night
const color NORD0  = #2E3440
const color NORD1  = #3B4252
const color NORD2  = #434C5E
const color NORD3  = #4C566A
// Snow Storm
const color NORD4  = #D8DEE9
const color NORD5  = #E5E9F0
const color NORD6  = #ECEFF4
// Frost
const color NORD7  = #8FBCBB
const color NORD8  = #88C0D0
const color NORD9  = #81A1C1
const color NORD10 = #5E81AC
// Aurora
const color NORD11 = #BF616A
const color NORD12 = #D08770
const color NORD13 = #EBCB8B
const color NORD14 = #A3BE8C
const color NORD15 = #B48EAD

// ═════════════════════════════════════════════════════════════════════════════
// 🧩 TYPE DEFINITIONS
// Custom Pine types live here when a file needs them.
// ═════════════════════════════════════════════════════════════════════════════
type CustomType
    int field1
    float field2
    color field3

// ═════════════════════════════════════════════════════════════════════════════
// ⚙️ GENERAL
// Shared controls used across multiple inner indicators or the overall render
// system.
// ═════════════════════════════════════════════════════════════════════════════
const string GROUP_GENERAL = "⚙️ General"

// ═════════════════════════════════════════════════════════════════════════════
// 📈 EXAMPLE SECTION
// Section-specific inputs, constants, state, helpers, calculations, and
// exported values all live here.
// ═════════════════════════════════════════════════════════════════════════════
const string GROUP_EXAMPLE = "1. 📈 Example"

// ═════════════════════════════════════════════════════════════════════════════
// 🧮 SHARED CALCULATIONS
// Shared helpers and orchestration only.
// ═════════════════════════════════════════════════════════════════════════════

// ═════════════════════════════════════════════════════════════════════════════
// 🎨 RENDER ENGINE
// Shared render state and final render orchestration live here.
// ═════════════════════════════════════════════════════════════════════════════
if barstate.islastconfirmedhistory or barstate.islast
    // Create and populate table/labels/lines
```

### Section Markers (Emoji Headers)

Every major section must use:
- an emoji
- an uppercase strong name
- a full-width divider block above it
- a one- or two-line purpose description under the title when useful
- divider lines of exactly `// ` followed by 77 `═` characters (80 columns
  total) — this is the width every banner in the repo uses; do not eyeball it

Examples:
- `// 🧱 CONSTANTS`
- `// 🧩 TYPE DEFINITIONS`
- `// ⚙️ GENERAL`
- `// 🌀 FIBONACCI`
- `// 📍 FLOOR PIVOTS`
- `// 🧲 CLUSTER`
- `// 🧮 SHARED CALCULATIONS`
- `// 🎨 RENDER ENGINE`

Do not use weak subsection names like `Inputs` as the primary section header.
Inputs belong inside the owning section, not in a separate global inputs area.

Use this exact strong banner pattern:

```pine
// ═════════════════════════════════════════════════════════════════════════════
// ⚙️ GENERAL
// Shared controls used across multiple inner indicators or the overall render
// system.
// ═════════════════════════════════════════════════════════════════════════════
```

Use the same strong banner style for top-level sections like `CONSTANTS` and
`TYPE DEFINITIONS`, not only for inner indicator sections.

Use this exact Nord color separation:

```pine
// Nord Theme Color
// Polar Night
const color NORD0 = #2E3440
const color NORD1 = #3B4252
const color NORD2 = #434C5E
const color NORD3 = #4C566A
// Snow Storm
const color NORD4 = #D8DEE9
const color NORD5 = #E5E9F0
const color NORD6 = #ECEFF4
// Frost
const color NORD7 = #8FBCBB
const color NORD8 = #88C0D0
const color NORD9 = #81A1C1
const color NORD10 = #5E81AC
// Aurora
const color NORD11 = #BF616A
const color NORD12 = #D08770
const color NORD13 = #EBCB8B
const color NORD14 = #A3BE8C
const color NORD15 = #B48EAD
```

### Section-Local Organization Rule

For indicators that contain multiple logical subsystems or inner indicators, use
the section headers as **strict ownership boundaries**, not just comments.

#### Core Rule

If a constant, input, variable, calculation, helper function, render helper,
plotting preparation, or section group name belongs to only one section, it
must live **inside that section**.

Do **not** place section-local code in shared/global areas for convenience.

Only place code outside a section when it is genuinely shared by **more than one
section**.

#### Hard Rules

- No section-local constants in global/shared areas.
- No section-local `GROUP_*` constants in global/shared areas.
- No section-local inputs in global/shared areas.
- No section-local helper functions in global/shared areas.
- No section-local state or derived values in global/shared areas.
- No section-local render prep in global/shared areas.
- No section should reach into another section's internal implementation
  details.
- No generic section-local variable names.

Section-local declarations must use a section prefix in their names so
ownership is obvious at a glance.

Examples:
- Good: `murreyAtrValue`, `fibPivotHighBar`, `clusterToleranceValue`
- Bad: `atrValue`, `value`, `count`, `level`

Examples of section-local constants that must stay in their section:
- `MAX_SWINGS_STORED`
- `MAX_PROFILE_ROWS`
- `MAX_SWING_DRAW_BARS`
- `LEFT_TO_RIGHT_EXTEND_BARS`
- `RIGHT_TO_LEFT_LEFT_BARS`
- `RIGHT_TO_LEFT_RIGHT_BARS`

Examples of section-local group constants that must stay in their section:
- `GROUP_FIB`
- `GROUP_PIVOTS`
- `GROUP_PDH`
- `GROUP_SWINGS`
- `GROUP_CLUSTER`

If a constant is only used by one section, it belongs in that section.

#### Cross-Section Dependency Rule

All sections must be architected as independent modules.

If one section needs data from another section:
- The provider section must define an explicitly named exported value intended
  for consumption.
- The exported name must make the dependency obvious.
- The consumer section should only read that exported value, not reuse internal
  intermediate variables from the provider section.

If a section depends on another section's engine, the engine must live in the
provider section, not in the consumer section.

Examples:
- Good: a Value Area section defines `valueAreaPrevSessionPocForCluster`
- Bad: a Cluster section directly reads a temporary row accumulator created
  inside Value Area logic

This makes dependencies explicit and keeps section internals encapsulated.

#### Plotting Rule

Plotting follows the same ownership rule:
- Section-specific drawing code should live inside its section whenever Pine
  allows it.
- If a `plot()` call must remain at the bottom of the file due to Pine
  constraints or repository style, only the final `plot()` statement should
  live there.
- The series, colors, widths, visibility flags, and all other plot-prep inputs
  must still be computed in the owning section.

#### Render Engine Rule

A centralized `Render Engine` block is allowed only when it is truly shared
infrastructure.

It is not required as a repository pattern.

If rendering belongs to one section, keep it in that section.

If a central render block exists:
- it should orchestrate shared drawing infrastructure only
- it should consume explicitly exported section values
- it should not become a dumping ground for section-specific inline logic

If a central render block contains large per-section branches, that is usually a
sign the code should be pushed back into the owning sections.

#### Preferred Layout

- Shared/global area:
  - truly shared constants
  - truly shared helpers
  - shared infrastructure only
- Each section:
  - its constants
  - its inputs
  - its calculations
  - its section-local helpers
  - its render-prep state
  - its section-local rendering, when possible
  - its exported values for other sections, when needed
- Bottom of file:
  - only Pine constructs that must remain there, such as final `plot()` calls

#### Anti-Pattern To Avoid

Do not organize files like this:
- inputs for all sections at the top
- calculations for all sections in the middle
- render prep for all sections near the bottom

Instead, organize by ownership:
- everything for Fibonacci in Fibonacci
- everything for Previous Day in Previous Day
- everything for Value Area in Value Area
- etc.

The only exceptions are code paths that are truly reused across multiple
sections or Pine-language placement constraints.

#### Sanctioned Exception: a Global 🎛️ Inputs Section

A single global `🎛️ USER INPUT SETTINGS` section is permitted ONLY when a real
Pine constraint forces it — the settings-dialog ordering must not follow the
section order, or helpers consumed by multiple sections must be declared below
the inputs they read. When a file uses this layout, it must document the
constraint in a comment at the top of the section (ma-waves.pine does this).
For any file without such a constraint, inputs stay section-local per the
rules above.

### Group Constants Pattern

**Always define group constants** for organizing inputs:

```pine
const string GROUP_GENERAL = "⚙️ General"
const string GROUP_TABLE = "📋 Table"
const string GROUP_LABEL = "🏷️ Label"
const string GROUP_VALUE = "🔢 Value"
const string GROUP_STRENGTH = "💪 Strength"
const string GROUP_MKT_CAP = "🏦 Market Capitalization"
const string GROUP_FLOAT = "🧊 Float Shares Outstanding"
```

**Emoji Prefix Guidelines:**
- ⚙️ General settings
- 📋 Table settings
- 🏷️ Label settings
- 🔢 Value/number settings
- 💪 Strength/threshold settings
- 🏦 Financial metrics
- 📈 Technical indicators
- 🌊 Waves/patterns
- 🎨 Style/colors

### Nord Color Theme

**All indicators use the Nord color palette:**

**Required rule**: Every `.pine` indicator file in this repository must declare the full `NORD0` through `NORD15` palette in the `// 🧱 CONSTANTS` section, even when some of those colors are not used by that specific indicator. Do not trim the palette down to only the currently referenced colors.

```pine
// Dark backgrounds (Polar Night)
const color NORD0  = #2E3440  // Darkest
const color NORD1  = #3B4252
const color NORD2  = #434C5E
const color NORD3  = #4C566A  // Lightest dark

// Light colors (Snow Storm)
const color NORD4  = #D8DEE9  // Text
const color NORD5  = #E5E9F0
const color NORD6  = #ECEFF4  // Brightest

// Frost (Teal/Blue accents)
const color NORD7  = #8FBCBB  // Cyan
const color NORD8  = #88C0D0  // Light blue (above threshold)
const color NORD9  = #81A1C1  // Blue
const color NORD10 = #5E81AC  // Dark blue

// Aurora (Status colors)
const color NORD11 = #BF616A  // Red (negative/error)
const color NORD12 = #D08770  // Orange (warning)
const color NORD13 = #EBCB8B  // Yellow (caution)
const color NORD14 = #A3BE8C  // Green (positive)
const color NORD15 = #B48EAD  // Purple (special)
```

**Common Color Usage:**
- `NORD4` - Default text color
- `NORD8` - "Above threshold" / positive strength color
- `NORD11` - "Below threshold" / negative/warning color
- `NORD2/NORD3` - Table backgrounds, borders, frames
- `NORD13` - Neutral/middle range values

---

## ⚠️ CRITICAL CODING CONVENTIONS

### 1. ALWAYS Use Explicit Parameter Names

**NON-NEGOTIABLE RULE**: Name parameters explicitly by default.
Exception: built-in functions that accept a variable number of arguments must use positional arguments because Pine rejects keyword arguments for them.

#### ❌ WRONG - Positional Arguments
```pine
indicator("My Indicator", "MI", true)
input.bool(true, "Show Volume")
table.new(position.top_right, 5, 2)
plot(ema, "EMA", color.blue, 2)
ta.sma(close, 50)
request.financial(syminfo.tickerid, "RETURN_ON_EQUITY", "FY")
```

#### ✅ CORRECT - Explicit Parameter Names
```pine
indicator(title = "My Indicator", shorttitle = "MI", overlay = true)
input.bool(defval = true, title = "Show Volume")
table.new(position = position.top_right, columns = 5, rows = 2)
plot(series = ema, title = "EMA", color = color.blue, linewidth = 2)
ta.sma(source = close, length = 50)
request.financial(symbol = syminfo.tickerid, financial_id = "RETURN_ON_EQUITY", period = "FY")
```

**This applies to ALL Pine Script functions**, including:
- `indicator()`, `strategy()`, `library()`
- All `input.*()` functions
- All `request.*()` functions
- All `table.*()` functions
- All `plot*()` functions
- All `ta.*()` functions
- All `label.*()`, `line.*()`, `box.*()` functions
- **Even conditional expressions**: `plot(series = emaVisible ? ema : na, title = "EMA")`

**The complete list of positional-argument exceptions** (everything else is
keyword — this list is exhaustive, do not extend it ad hoc):

1. **Variadic built-ins** — `math.max()`, `math.min()`, `array.from()`, and the
   format arguments of `str.format()`, `log.info()`, `log.warning()`,
   `log.error()`. Pine rejects keywords on variadic parameters (`CE10119`). The
   format STRING itself and any non-variadic parameters stay keyworded where
   Pine allows it. (`array.from()` was missing from this list until 2026-09-25
   while five files used it positionally — the list is meant to be exhaustive,
   so add to it here rather than letting call sites diverge from the doc.)
2. **`color.t()`** — positional single argument (established repo-wide form).
3. **Type casts** — `int(x)`, `float(x)` (established repo-wide form).
4. **`max_bars_back()`** — the first parameter cannot be keyworded (`var` is a
   reserved word); the accepted repo form is both parameters positional:
   `max_bars_back(macd, 200)`.

```pine
// ✅ CORRECT
float range = math.max(high - low, syminfo.mintick)
int visibleStart = math.max(0, bar_index - lookbackBars + 1)
log.warning("feed missing after {0} bars — {1}", graceBars, missingText)

// ❌ WRONG
float range = math.max(number0 = high - low, number1 = syminfo.mintick)
```

**Verification Required:**
- **Always check the Pine Script v6 Reference** for correct parameter names
- If a function doesn't have documented parameter names, or if it is a variadic
  built-in that rejects keywords, positional arguments are required
- When in doubt, fetch: `https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/[namespace].md`

### 2. ALWAYS Use Meaningful Variable Names

**NON-NEGOTIABLE RULE**: Never use single-letter or cryptic variable names.

#### ❌ WRONG - Cryptic Names
```pine
var table t = table.new(position.top_right, 5, 20)
for i = 0 to a.size() - 1
    p = prices.get(i)
    v = volumes.get(i)
    tm = times.get(i)
    table.cell(t, 0, i, str.tostring(p))
```

#### ✅ CORRECT - Meaningful Names
```pine
var table tapeTable = table.new(position = position.top_right, columns = 5, rows = 20)
for tickIndex = 0 to prices.size() - 1
    tickPrice = prices.get(tickIndex)
    tickVolume = volumes.get(tickIndex)
    tickTime = times.get(tickIndex)
    table.cell(table_id = tapeTable, column = 0, row = tickIndex, text = str.tostring(value = tickPrice))
```

**Variable Naming Guidelines:**
- Use **full words**, not abbreviations (e.g., `tickPrice` not `p`, `tickVolume` not `v`)
- Use **camelCase** for multi-word variables (`tickIndex`, `tableRow`, `footprintBuyVolume`)
- Loop indices should be descriptive (`tickIndex`, `rowIndex`, `columnIndex` instead of `i`, `j`, `k`)
- Temporary variables should still be meaningful (`currentPrice` not `tmp`, `priceColor` not `clr`)
- Boolean variables should be descriptive (`isAboveAsk`, `showFootprint`, `hasValidData`)

**Acceptable Short Names:**
- Standard financial/technical abbreviations: `ema`, `sma`, `rsi`, `atr`, `roc`, `macd`
- Well-known acronyms: `vwap`, `eps`, `roe`, `rps`
- Time units: `ms` (milliseconds), `sec` (seconds) - but prefer full words when possible

### 3. Helper Function Pattern

**Always prefix helper functions with `f_`**:

```pine
// Helper function to create label cell
f_labelCell(table targetTable, int column, int row, string cellText) =>
    table.cell(table_id = targetTable, column = column, row = row, text = cellText,
         text_color = labelColor, text_size = labelSize,
         text_halign = labelHalign, text_valign = labelValign,
         text_font_family = labelFontFamily, bgcolor = tableBackgroundColor)

// Helper function to format large numbers
f_formatNumber(float rawValue) =>
    if na(rawValue)
        "N/A"
    else if rawValue >= 1e12
        str.format("{0, number, #.00}T", rawValue / 1e12)
    else if rawValue >= 1e9
        str.format("{0, number, #.00}B", rawValue / 1e9)
    else if rawValue >= 1e6
        str.format("{0, number, #.00}M", rawValue / 1e6)
    else
        str.format("{0, number, #,###}", rawValue)

// Helper function to get earnings date string
f_getEarningsDateString(int timestamp) =>
    if na(timestamp)
        "N/A"
    else
        string monthName = switch month(time = timestamp)
            1 => "Jan"
            2 => "Feb"
            3 => "Mar"
            // ... etc
            => "N/A"
        str.format("{0} {1}", monthName, year(time = timestamp))
```

**Common Helper Function Patterns:**
- `f_labelCell()`, `f_valueCell()`, `f_emptyCell()` - Table cell creation
- `f_clearLines()`, `f_clearLabels()`, `f_clearBoxes()` - Drawing object cleanup
- `f_formatNumber()`, `f_formatPercent()` - Number formatting
- `f_getColor()` - Conditional color selection
- `f_safeFloat()` - Safe type conversion with null handling

### 4. Type Annotations

**Pine Script v6 supports type inference.** Explicit type annotations are optional
when the compiler can infer the type from the assigned value.

#### When types CAN be omitted (inferred)
```pine
adjustedTransp = color.t(baseColor) - 20       // inferred as float
isActive = close > open                         // inferred as bool
tickerId = ticker.modify(tickerid = syminfo.tickerid, session = session.regular) // inferred as string
pivotHighArray = array.new<pivotPoint>()        // inferred as array<pivotPoint>
murreyPlotStyle = line.style_solid              // inferred from built-in line style constant
```

#### Important Pine-specific restriction
- Do not invent type keywords from built-in constants.
- `line.style_solid`, `line.style_dashed`, etc. are valid values for `style`
  parameters, but `line_style` is not a valid declaration type keyword.
- In Pine, declaration types must be fundamental types, special types, UDTs,
  or user-declared enums. If a variable stores a built-in style constant, leave
  it inferred unless you are using a valid declared type from the docs.
- If you write `line_style someVar = ...`, TradingView will fail compilation
  with `CE10149: "line_style" is not a valid type keyword.`
- Treat built-in style constants as values, not declaration keywords. This same
  rule applies to other built-in style families such as `plot.style_*`.

#### ✅ CORRECT — leave built-in style values inferred
```pine
resolvedTrendStyle = f_trendLineStyle(styleInput = trendLineStyleInput)
murreyPlotStyle = line.style_solid
```

#### ❌ WRONG — invented type keyword from built-in constant family
```pine
line_style resolvedTrendStyle = f_trendLineStyle(styleInput = trendLineStyleInput)
```
- Do not force explicit integer typing onto expressions built with
  `math.max()`/`math.min()` or similar numeric helpers just for consistency.
  Those expressions often resolve as float expressions in Pine, so `int x = ...`
  can fail even when the runtime values look integer-like.
- If a local variable is initialized from a numeric expression and Pine can infer
  it correctly, prefer the inferred type unless a specific declared type is
  required by the docs or by an `na` initialization.

#### When types MUST be declared
```pine
float myPrice = na       // na alone is ambiguous — type required
int myBar = na           // same: must declare when initializing to na
var float persistedVal = na
```

#### UDT field assignment uses `:=`, never `=`

Writing to a field of an existing object is an ASSIGNMENT, not a declaration:

```pine
// ✅ CORRECT
QwReading copied = original.copy()
copied.pctChange := newValue

// ❌ WRONG — three errors at once
copied.pctChange = newValue
```

A plain `=` makes Pine read `copied.pctChange` as the NAME of a new variable,
so it fires `CE10089` ("use := instead of ="), `CE10090` ("identifiers should
not contain '.'") and `CE10095` ("already defined") together. The three-error
signature is the tell. Only `Type.new(...)` and the initial `Type x = ...`
declaration use `=`.

#### Important `bool` rule
- Do not initialize `bool` variables with `na`.
- In Pine, `bool` values are always either `true` or `false`, so cache flags and
  state booleans must start from a real boolean value such as `false`.
- If you need an "uninitialized" sentinel state, use a different type or a
  separate boolean flag rather than `bool someFlag = na`.

**Rule for this repository:** explicit types are recommended for readability and
are required when initializing to `na`, but do not flag inferred-type locals as
style violations.

### 5. Declaration Order

**Pine Script v6 is strictly top-to-bottom.** Variables, inputs, and functions
must be declared before they are referenced. There is no hoisting.

This matters for multi-section indicators: if Section B references an input or
helper from Section A, Section A must appear above Section B in the file.

Cross-cutting inputs consumed by many sections (e.g., a show/hide toggle that
controls visibility across multiple sections) should be declared in the GENERAL
section so every downstream section can reference them without forward-reference
errors.

```pine
// ⚙️ GENERAL — shared controls
bool showCluster = input.bool(...)   // consumed by Pivots, Murrey, Value Area, etc.

// ✅ Works — showCluster is declared above
bool pivotPlotVisible = showPivots and not showCluster
```

```pine
// ❌ WRONG — forward reference, will not compile
bool pivotPlotVisible = showPivots and not showCluster   // showCluster not yet declared
// ... many lines later ...
bool showCluster = input.bool(...)
```

### 6. Prefer UDTs Over Parallel Arrays

When multiple arrays track different fields of the same logical entity (e.g.,
price, weight, color, style for each level), prefer a single array of a
user-defined type (UDT) over parallel arrays.

#### ❌ WRONG — Parallel arrays
```pine
array<float>  levelPrices  = array.new<float>()
array<int>    levelWeights = array.new<int>()
array<color>  levelColors  = array.new<color>()
// ... N more arrays, all kept in lockstep
```

#### ✅ CORRECT — UDT array
```pine
type Level
    float  price
    int    weight
    color  levelColor

var array<Level> levels = array.new<Level>()
array.push(id = levels, value = Level.new(price = 100.0, weight = 3, levelColor = NORD4))
```

**Benefits:**
- Push, sort-swap, and read are one operation instead of N
- Function signatures shrink dramatically
- Fields are self-documenting and cannot drift out of sync

**UDT sorting/searching (since 2026):** `array.sort()`, `array.sort_indices()`,
and `matrix.sort()` accept UDT collections (April 2026), and
`array.binary_search()` / `_leftmost()` / `_rightmost()` search them
(August 2026). All take a `sort_field` parameter — a "const int" field index
(default 0 = first field in the type declaration) or a "const string" field
name; binary search requires the array pre-sorted ASCENDING by that same
field. A manual sort loop is now only justified for custom ordering the
built-in can't express (e.g. quote-window's na-sinks-to-bottom insertion
sort); comments in files written before April 2026 may still claim UDT
sorting is impossible — that claim is obsolete.

### 7. Emoji Shorttitle Pattern

**Always use emoji in shorttitle** for visual identification:

```pine
indicator(title = "Fundamental View Indicator", shorttitle = "🧾 FVI", overlay = true)
indicator(title = "Technical View Indicator", shorttitle = "🧭 TVI", overlay = true)
indicator(title = "MAs & Waves", shorttitle = "🌊 MA&W", overlay = true)
indicator(title = "Options GEX Levels", shorttitle = "🧬 GEX", overlay = true)
```

**Emoji Suggestions:**
- 🧾 Fundamental data
- 🧭 Technical metrics
- 🌊 Waves/momentum
- 🧬 Options/derivatives
- 📊 Charts/analysis
- ⚡ Real-time/fast data
- 🎯 Targets/levels
- 📈 Trends

---

## 📊 Common Indicator Patterns

### Data Retrieval Patterns

#### Financial Data (Fundamentals)
```pine
// Quarterly data
float roe = request.financial(symbol = syminfo.tickerid,
     financial_id = "RETURN_ON_EQUITY", period = "FQ", ignore_invalid_symbol = true)

float tso = request.financial(symbol = syminfo.tickerid,
     financial_id = "TOTAL_SHARES_OUTSTANDING", period = "FQ")

// Annual data
float annualRoe = request.financial(symbol = syminfo.tickerid,
     financial_id = "RETURN_ON_EQUITY", period = "FY")
```

**Common Financial IDs:**
- `TOTAL_SHARES_OUTSTANDING`
- `RETURN_ON_EQUITY`
- `TOTAL_REVENUE`
- `EARNINGS_PER_SHARE_BASIC`
- `PRICE_EARNINGS_FORWARD`
- `PRICE_SALES_FORWARD`
- `EARNINGS_ESTIMATE`
- `SALES_ESTIMATES`

#### Earnings Data
```pine
float currEpsActual = request.earnings(ticker = syminfo.tickerid,
     field = earnings.actual, ignore_invalid_symbol = true)
float currEpsEstimate = request.earnings(ticker = syminfo.tickerid,
     field = earnings.estimate, ignore_invalid_symbol = true)

// Event detection
bool isEpsEvent = ta.change(source = currEpsActual) != 0 and not na(currEpsActual)

// Historical earnings using ta.valuewhen
float epsQ0 = ta.valuewhen(condition = isEpsEvent, source = currEpsActual, occurrence = 0)  // Most recent
float epsQ1 = ta.valuewhen(condition = isEpsEvent, source = currEpsActual, occurrence = 1)  // Previous quarter
int epsTime0 = ta.valuewhen(condition = isEpsEvent, source = time, occurrence = 0)
```

#### Security Data (Multi-symbol)
```pine
float floatShares = request.security(symbol = syminfo.tickerid,
     timeframe = "D", expression = syminfo.shares_outstanding_float,
     lookahead = barmerge.lookahead_on)

float volumeTicker = request.security(symbol = syminfo.tickerid,
     timeframe = "D", expression = ta.sma(source = volume, length = 20),
     lookahead = barmerge.lookahead_on)
```

#### Session Handling for request.security

`syminfo.tickerid` inherits the chart's session setting. If a user has
"Extended Trading Hours" enabled, daily OHLC values will include pre/post-market
data, which can produce different highs, lows, and closes than the official
regular-session bar.

**Use `ticker.modify` for deterministic session control:**

```pine
// Forces regular-session data regardless of chart settings
string regularSymbol = ticker.modify(tickerid = syminfo.tickerid, session = session.regular)

// Daily H/L/C will always match the official regular-session bar
[prevHigh, prevLow, prevClose] = request.security(
     symbol = regularSymbol, timeframe = "D",
     expression = [high[1], low[1], close[1]],
     lookahead = barmerge.lookahead_on)
```

**When to use which:**
- `syminfo.tickerid` — when you want the data to follow whatever the user's
  chart is set to (rare)
- `ticker.modify(..., session = session.regular)` — when you want consistent
  regular-session values across all users (most S&R / pivot indicators)

**Consistency rule:** if one `request.security` call in a section uses a
session-modified ticker, all calls in that section that request the same
instrument should use the same ticker to avoid mismatched session data.

#### Footprint Data (Volume Profile)
```pine
footprint currentFootprint = request.footprint(
     ticks_per_row = ticksPerRow, va_percent = valueAreaPercent)
```

### Conditional Coloring Pattern

**Use ternary operators for threshold-based coloring:**

```pine
color mktCapColor = na(mktCapBillions) ? textColor :
     mktCapBillions <= mktCapBelow ? aboveColor : textColor

color volumeColor = volumeTicker >= volumeAbove ? aboveColor :
     volumeTicker <= volumeBelow ? belowColor : textColor

color peColor = na(peRatio) ? textColor :
     peRatio >= peAbove ? belowColor :
     peRatio <= peBelow ? aboveColor : textColor
```

**Three-tier coloring (above/neutral/below):**
```pine
var color aboveColor = input.color(defval = color.new(color = NORD8, transp = 0),
     title = "Above Color", group = GROUP_STRENGTH)
var color belowColor = input.color(defval = color.new(color = NORD4, transp = 40),
     title = "Below Color", group = GROUP_STRENGTH)
```

### Number Formatting Patterns

**Large numbers with M/B/T suffixes:**
```pine
string mktCapStr = na(mktCap) ? "N/A" : str.tostring(value = mktCap, format = format.volume)
```

**Percentages:**
```pine
string epsYoyStr = na(epsYoyVal) ? "N/A" : str.format("{0}%", math.round(number = epsYoyVal, precision = 1))
string adrFormatted = na(adrRounded) ? "-" : str.format("{0, number, #.00}%", adrRounded * 100)
```

**Currency:**
```pine
string avgPrice = na(syminfo.target_price_average) ? "N/A" :
     str.format("${0}", math.round(number = syminfo.target_price_average, precision = 2))
string revenueVal = na(revenue) ? "N/A" : str.tostring(value = revenue, format = format.currency)
```

**na fallbacks must not impersonate data:** a missing price target rendered as
`"$0"` reads as a real zero-dollar target. Use `"N/A"` (or `"-"`) for missing
values, and guard EVERY formatted field — a single unguarded `str.format` on an
na series renders a literal `NaN` in the table.

### Table Rendering Pattern

**Create table once with `var`, populate in `barstate.islastconfirmedhistory`:**

```pine
var table techTable = table.new(position = tablePosition, columns = 13, rows = 1,
     border_width = tableBorderSize,
     border_color = tableBorderColor,
     frame_width = tableFrameSize,
     frame_color = tableFrameColor)

if barstate.islastconfirmedhistory
    col = 0

    // Left spacer
    if tableSpacerLeft
        table.cell(table_id = techTable, column = col, row = 0, text = "   ",
             bgcolor = tableBackgroundColor, text_size = textSize)
        col += 1

    // Market Cap
    if mktCapVisible
        table.cell(table_id = techTable, column = col, row = 0, text = mktCapText,
             text_color = mktCapColor,
             text_halign = textHalign,
             text_valign = textValign,
             text_size = textSize,
             bgcolor = tableBackgroundColor,
             tooltip = mktCapTooltip,
             text_font_family = textFontFamily)
        col += 1
```

**Helper function pattern:**
```pine
f_labelCell(table targetTable, int column, int row, string cellText) =>
    table.cell(table_id = targetTable, column = column, row = row, text = cellText,
         text_color = labelColor, text_size = labelSize,
         text_halign = labelHalign, text_valign = labelValign,
         text_font_family = labelFontFamily, bgcolor = tableBackgroundColor)

f_valueCell(table targetTable, int column, int row, string cellText) =>
    table.cell(table_id = targetTable, column = column, row = row, text = cellText,
         text_color = valueColor, text_size = valueSize,
         text_halign = valueHalign, text_valign = valueValign,
         text_font_family = valueFontFamily, bgcolor = tableBackgroundColor)

f_emptyCell(table targetTable, int column, int row) =>
    table.cell(table_id = targetTable, column = column, row = row, text = "",
         bgcolor = tableBackgroundColor)
```

### Type Definitions Pattern

**Define custom types for complex data structures:**

```pine
type Trend
    TrendDir direction
    color plotColor

type Wave
    int number
    int letter
    float lastImpulseHigh
    float lastImpulseLow

type Price
    float close
    bool isExtreme
    bool isHigherHigh
    bool isLowerLow
```

**Use enums for state:**
```pine
enum TrendDir
    UP
    DOWN
    FLAT
```

---

## 🚫 Common Pitfalls to Avoid

### 1. Never Mix v4/v5 Syntax with v6
- Some functions were renamed or moved to namespaces in v6
- Always verify function names in the reference docs
- **Always check**: `https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/[namespace].md`

### 2. Never Skip Parameter Names
- While Pine Script allows positional arguments, this project **REQUIRES** explicit parameter names
- **Always verify parameter names** in the Pine Script v6 Reference

### 3. Never Use Single-Letter Variables
- Except for standard abbreviations (ema, sma, rsi, etc.)
- Loop indices must be descriptive (`rowIndex` not `i`)

### 4. Never Skip Documentation Lookup
- **Before suggesting ANY function**, check the documentation
- Don't assume a function exists - verify it first
- **Prevent hallucinations** by consulting references

### 5. Never Forget Repainting Considerations
- Choose `lookahead` by request type:
  - `lookahead = barmerge.lookahead_on` for stable snapshot requests — daily
    fundamentals, or previous-period OHLC fetched with `[1]` offsets — where the
    requested value is already final and lookahead only fixes real-time lag.
  - `lookahead = barmerge.lookahead_off` for streams of confirmed events from a
    higher timeframe (e.g. `ta.pivothigh()`/`ta.pivotlow()` via
    `request.security()`). With `lookahead_on` these read HTF values before the
    HTF bar closes and repaint history.
- Understand bar-by-bar execution model
- Read: `https://www.tradingview.com/pine-script-docs/concepts/repainting/`

### 6. Never Forget to Group Inputs
- All inputs must have a `group = GROUP_*` parameter
- Define group constants with emoji prefixes
- Organize logically (General, Table, Style, Metrics, etc.)

### 7. Never Create Tables Without Helper Functions
- Use `f_labelCell()`, `f_valueCell()`, `f_emptyCell()` pattern
- Keeps code DRY and maintainable
- Makes styling consistent across cells

### 8b. Never Derive a Session Edge From the Full-Session Window

`inSession and not inSession[1]` does NOT detect a new session when the chart
is RTH-only: every bar is inside `"0930-1600"`, so the edge fires once on the
first loaded bar and never again. Daily reseeds, snapshots and counters built
on it silently stop after day one — and they keep rendering, so nothing looks
broken.

```pine
// ❌ WRONG — fires once, ever, on an RTH-only chart
bool inRth = not na(time(timeframe.period, "0930-1600:23456", "America/New_York"))
bool sessionOpened = inRth and not inRth[1]

// ✅ CORRECT — pin the edge to a few minutes at the open
const string SESSION_RTH_OPEN = "0930-0935:23456"
bool inOpenWindow = not na(time(timeframe.period, SESSION_RTH_OPEN, "America/New_York"))
bool sessionOpened = inOpenWindow and not inOpenWindow[1]
```

This repo has hit it three times (`composite-breadth` daily reseeds,
`quote-window` colour-rotation snapshot and its log layer). Keep the
full-session window for "am I in RTH" tests only.

### 8. Never Forward-Reference Variables or Functions
- Pine Script v6 has no hoisting — all identifiers must be declared above their
  first use
- Cross-cutting inputs belong in GENERAL, not in the section that "owns" the
  feature, if other sections above it need them
- Helper functions called from a section must be defined before that section

### 9. Never Rely on `var` (or UDT Fields) Persisting Across Realtime Ticks
- On every realtime tick the script re-executes from the bar's last COMMITTED
  state: plain variables and `var` assignments roll back; only `varip` SCALARS
  and `array.push` survive across ticks.
- Fields of an object held in a `varip` variable still roll back unless the
  FIELD itself is declared `varip` inside the `type`. This repo has been bitten
  by this exact class more than once (ticker-tape watermark, degraded-path
  state) — when tick-to-tick persistence is needed, use varip scalars or
  varip-declared fields, never plain fields on a varip object.
- Corollary: a `var bool` "already fired" guard around `alert()` or `log.*` is
  broken on realtime — the flag un-sets on the next tick while the alert/log
  output does NOT roll back, so it fires once per tick until the bar closes.
  Gate on `barstate.isconfirmed` or make the flag `varip`.

### 10. Never Create or Delete Drawings on Intrabar Ticks
- Intrabar ticks may only MODIFY (`set_*`) a live drawing object — never
  `label.new`/`label.delete` (or line/box equivalents) outside a
  `barstate.isconfirmed` path. Deletes commit while references roll back
  (dangling ref), and at the `max_*_count` cap an intrabar creation
  garbage-collects the oldest COMMITTED drawing, which does not roll back.
- The repo lifecycle pattern: mint ONE object per logical cycle on a confirmed
  tick (blank if it should start hidden), `set_*` only intrabar, hide via
  `set_text("")`, reuse or delete it at the next confirmed boundary.

### 11. Never Let Event Engines Fire on Unconfirmed Ticks by Default
- Signal/state engines that feed alerts or markers evaluate on
  `barstate.isconfirmed` unless tick-time behavior is a deliberate, documented
  choice — an intrabar condition that reverts before the close otherwise fires
  a phantom alert with no committed evidence on the chart.
- Prefer close-gated first-shows for live drawings: when every state write
  lands on a confirmed tick, plain `var` suffices and replay reproduces
  realtime exactly (both waves indicators converged on this 2026-07-25). If
  tick-time display IS deliberate anyway, make the visibility latch
  `varip`-sticky and document the reload caveat: intrabar-only state does not
  reproduce on replay, because historical bars run a single closing tick.

### 11b. Never Anchor a Long-Lived Drawing by an Old `bar_index`
- A drawing coordinate given as `xloc.bar_index` is resolved through the
  history buffer: `x = someOldBarIndex` is a historical offset of
  `bar_index - someOldBarIndex`. If that origin is stored and re-applied every
  bar (`line.set_xy1(x = swing.barIndex)`), the offset grows by one per bar and
  eventually crosses the buffer — "The requested historical offset (1413) is
  beyond the historical buffer's limit (1412)". The runtime error wipes EVERY
  drawing at once, and it typically fires on the first realtime bar, because
  the last historical bar sat exactly at the limit.
- Fix: store the origin's `time` and draw with `xloc = xloc.bar_time`. A time
  coordinate is not a history reference. `swings.pine` hit this 2026-10-01
  (`Swing.barTime`); a bigger `max_bars_back` only moves the cliff.

### 12. Never Put a History Reference Inside a Conditionally-Called Helper
- `and` / `or` / `?:` short-circuit, so `cond and f_helper(...)` skips the call
  on bars where `cond` is false. If `f_helper` reads history — a `[]` offset, or
  any `ta.*` built-in — its history buffer is then built from an irregular
  subset of bars and its results are inconsistent. The compiler warns: "The
  `f_x()` call inside the conditional expression might not execute on every
  bar, which can cause inconsistent calculations."
- Two fixes; prefer the second. Assign the call to a global and use that global
  in the conditional, OR hoist the history read out of the helper and pass the
  already-read value in. The second removes the history dependency instead of
  routing around it, so the helper cannot regress the next time a caller adds a
  guard (cvd.pine's `divergenceAnchorStartAtPivot` does this).
- This fires the moment a previously history-free helper gains one `[]`, which
  is easy to miss in review: the offending line is the CALL SITE, not the edit.

---

## 🎯 AI Workflow for Code Changes

### Step-by-Step Process

1. **Read Current File**
   - Understand purpose, structure, and existing patterns

2. **Identify Required Documentation**
   - Determine which namespace/concept files are needed
   - Use the Query-to-Documentation Routing table above

3. **Fetch Relevant Documentation**
   ```
   https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/[namespace].md
   https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/concepts/[concept].md
   ```

4. **Verify Function Signatures**
   - Check Pine Script v6 Reference for correct parameter names
   - Ensure all parameters are explicitly named

5. **Implement Changes**
   - Follow emoji section headers
   - Use Nord color theme
   - Apply naming conventions (explicit parameters, meaningful variables)
   - Add helper functions with `f_` prefix
   - Group inputs with emoji prefixes

6. **Verify Patterns**
   - All parameters explicitly named ✓
   - All variables meaningful (no single letters) ✓
   - Nord colors used consistently ✓
   - Emoji section headers in correct order ✓
   - Helper functions prefixed with `f_` ✓
   - Inputs organized by groups ✓

7. **Test Compilation**
   - Ensure syntax matches Pine Script v6 standards
   - Verify no deprecated functions are used

---

## 📖 Indicator File Reference

### Current Indicators

1. **`composite-breadth.pine`**
   - LEAN REBUILD 2026-10-03 (Henry: "all those colors are annoying… make obv,
     cvd and cbi extreme similar and simple"). 1,898 → ~530 lines; the
     pre-lean file is at `~/Projects/Trading/cbi-logs/composite-breadth-pre-lean-2026-10-03.pine`.
     REMOVED on purpose: opacity/consensus colouring, consensus votes and
     tiers, Line Trust regime + Trust table + ▲ markers, time-of-day dims,
     session divider, the fast/slow signal pair and its ±4 confirmation band,
     data-window debug plots. Don't re-add them without Henry asking
   - Engine kept: five legs (VOLD RTH-only from 09:30, ADD, %VWAP, CUMTICK
     cash-session only on classic `USI:TICK`, NQ PREMIUM cash-session only on
     Nasdaq-listed charts), per-leg universe routing on `ticker.new(...,
     session.extended)`, 07:00 premarket start with per-leg de-bias, line drawn
     07:00-16:00 ET, 6-minute display EMA
   - WEIGHTS 75/5/10/20/40 (VOLD/ADD/%VWAP/CUMTICK/NQ) — 2026-10-03 sweep on
     85 logged sessions, worst-regime direction +0.0114 → +0.0178 vs the old
     75/5/20/20/20, shift unchanged; NQ above ~40 trades one chunk against
     another and turns the line into futures premium
   - Pane = the shared volume-pane pattern (see "Signal MA lengths" below):
     CBI line NORD3 width 1, signal MA EMA Auto 4 h, slope NORD8/NORD9 width 3,
     line/MA fill, computed over a rolling sample window; 🧮 Calculation group (Timeframe /
     Wait for timeframe closes) built manually because the ◆ are drawings.
     The MA window does NOT restart at 07:00/09:30 (the CBI is a ±100
     oscillator, not a running total). No vendor volume guard: every leg is a
     USI/CME feed, so NDX/SPX charts without volume are valid hosts
   - 🎯 PRICE CONFIRMATION ◆ kept (bullish 65-76% right at 30 min over 166
     sessions; bearish never measured — both ON by default, tooltips say so),
     coloured like cvd's divergences (NORD8 bull / NORD11 bear)
   - NO `alertcondition()` — the pane is read, not subscribed to
   - BREADTH LEVEL vs MOMENTUM (2026-10-03, cbimom.py, v4 logs 85 sessions,
     75/5/10/20/40): worst-chunk DIRECTION level +0.018 (2-min) / +0.021
     (6-min); line − 40-min MA −0.015 / −0.020; 20-min slope −0.002 / −0.008.
     Opposite of VSM: breadth POSITION carries forward, breadth MOMENTUM
     mean-reverts. Only CUMTICK holds in both forms. Tooltips now point at
     distance from zero; the signal MA stays context
   - "CBI / Signal Fill" (2026-10-03, Henry's visual trial — CBI first, may
     roll to the other panes): fill() between the CBI plot and the signal MA
     plot, two colors only — NORD8 at 10% opacity (transp 90) while CBI ≥ MA,
     NORD9 at 5% (transp 95) below. No input — toggled in the Style tab; hidden
     with the MA when Type = None
   - WHOLE-MARKET ROUTING (2026-10-03, bulstudy/bulsweep/buldia*.py on
     bul-1/2/3 = 87 sessions Jun 1–Oct 2, 3 chunks of 29): universe inputs
     REMOVED, routing fixed: VOLD = mean of ADVDECV/TVOL .NQ + .NY + .DJ (each
     tape its own 09:30 baseline via f_cbiVoldLeg), ADD = ADVDEC.US (±4500),
     %VWAP = PCTABOVEVWAP.US (±15), CUMTICK = classic USI:TICK. Weights
     75/5/5/30/20. QQQ worst-chunk DIR/SHIFT 2-min +0.018/+0.004, 6-min
     +0.017/−0.003 vs old routing −0.005/+0.009 and −0.004/+0.004 (old ranked
     805/864 in the sweep). Bullish ◆ +5.8 bps 71% n21 (every chunk positive;
     old +4.3 65%); bearish ◆ still no edge (−0.7, 52%). All-US TICK (TICK.US)
     gave the best line SHIFT (+0.025) but broke the ◆ (−3.0, 50%) — rejected.
     SPY: direction improves, nothing predicts SPY shift. Single stocks
     (NVDA/AAPL/MSFT/TSLA): no configuration holds in every chunk — breadth is
     a market read, not a single-name read. NQ PREMIUM measured −0.090 alone
     in Jun–Jul (it carried 40 before) → 20

2. **`fundamental-view-indicator.pine`**
   - Displays comprehensive fundamental data table
   - Includes: Market cap, ROE, float, analyst recommendations, price targets, EPS/revenue history
   - Vertical two-column table (label + value)
   - Uses `request.financial()` and `request.earnings()`

3. **`technical-view-indicator.pine`**
   - Single-row horizontal table with technical metrics
   - Includes: Market cap, float, volume, dollar volume, P/E, P/S, ADR, ATR, RPS
   - Uses `request.financial()` and `request.security()`

4. **`ma-waves.pine`**
   - Moving average wave counting indicator (Barry Burns methodology)
   - Three layered engines: 50 SMA trend (with a `TrendDir` enum and
     ATR-fraction hysteresis), stochastic %D 45/55 cycle boundaries, and the
     wave count classifying each half-cycle's extreme
   - Implements wave labeling with impulses and retracements
   - Uses `label.new()` for wave annotations (live label first shows on a
     confirmed close where %K holds the turn against the cycle, pinned on the
     %D cross)

5. **`macd-waves.pine`**
   - Barry Burns momentum MACD (5/20/30) with the MOM wave count
   - Stochastic %D 45/55 half-cycle windows partition the count (plot-in-zone
     engine); labels anchor on a display-only extreme layer with pin migration
     and an ordering guard
   - Trend shifts two ways, both committing at a bar close: a TAKE against the
     trend (plots the new trend's 1), or an ARMED trend's FAILED IMPULSE — a
     high that cannot take the up trend's last high, or the mirror — which
     plots as the new trend's 2 and relabels the retrace behind it to 1. A
     trend is armed by any take; a trend born from a failure starts unarmed and
     cannot be shifted by another failure, which is what stops a contraction
     from thrashing 1,2,1,2
   - `qualifies` gates BOTH the plot and the structural-extreme update — one
     question, "did this wave move the structure?". Letting an unqualified wave
     update the extreme was the 2026-08-21 ratchet defect: a failed impulse
     demoted the level the next impulse had to clear, so a decaying staircase
     of lower highs each read as a fresh HH and the count ran to 9 through a
     dead trend
   - Live labels first show TICK-TIME — the first tick with both the MACD line
     and %K angling against the open half-cycle while the wave qualifies —
     then MACD direction alone rules visibility tick by tick; renumbering,
     pins and relabels stay close-committed (the 🧪 debug/Pine Logs layer was
     stripped 2026-07-25 after tuning — restore from git history before
     re-tuning)

6. **`stochastic.pine`**
   - Barry Burns cycle stochastic (5/2/3, 80/20 + 45 mid) — bare cycle
     indicator, no pattern engines in the file

7. **`support-resistance.pine`**
   - Multi-indicator cluster map for support and resistance
   - Combines Fibonacci, floor pivots, previous day, round numbers, major
     swings, Murrey Math, and value area into cluster zones
   - Uses `request.security()`, `request.footprint()`, and drawing objects
   - Renders in `barstate.islast` with line/label/box arrays

8. **`structure-and-levels.pine`**
   - Price structure and key levels engine

9. **`fibonacci.pine`** / **`pivots.pine`** / **`swings.pine`**
   - Standalone level engines (fib retracements, pivots, strength-scored
     major swings)
   - `swings.pine` (was `major-swings.pine`) draws the two-degree
     medium/major swing structure, with a Left/Middle/Right label anchor
   - `swings.pine` Swing Strength is in MINUTES since 2026-10-01 (default 30,
     converted to bars per interval; a bars input covers daily+), so 1m/2m/3m/6m
     resolve the same swings — the old bar count made the 1m an 11-minute swing
     chart. Defaults ship six lines max (2 major + 1 nearest medium per side);
     ordinary broken levels are hidden unless Show Broken History is on, while
     FLIP and MSS draw for one reference window with their own color inputs
     (they used to inherit Broken, so they ignored the color you set)
   - `swings.pine` selection rules (2026-10-01 review): FLIP and MSS share one
     3000 "in play" score band — MSS had none and lost every slot to unbroken
     levels. Only a NEW strong promotion bumps `structureStamp` (re-promoting an
     already-strong origin used to reshuffle on nearly every break); a held level
     that stops being drawable triggers its own reselection. Strength caps at 120
     minutes / 120 bars and the yardstick at 960 bars, so no minute chart is
     clamped. A swing is not scanned for touch/pierce on its own confirmation bar
   - `swings.pine` break scan is GATED (`liveHighFloor` / `liveLowCeiling`): a
     bar below every unbroken high's zone and above every unbroken low's zone
     cannot change any swing, so the 40-swing scan is skipped (it was ~70% of
     runtime). The touch latch is `lastInsideBarIndex`, not a bool, precisely so
     skipped bars need no latch clearing — don't revert it to a flag. A released
     (no-longer-drawable) held level is a REFILL, not a re-rank: survivors keep
     their slots. Re-ranking on release made unrelated lines vanish the next bar
   - ⚠️ `swings.pine` is CLOSED-BAR ONLY by design (Henry, 2026-10-01): it is
     the past projected into the future, so nothing runs intrabar or per
     realtime tick. Render gate is `barstate.islastconfirmedhistory or
     (barstate.islast and barstate.isconfirmed)`; every state write is on
     `barstate.isconfirmed`. Never add tick-time behavior to it
   - `pivots.pine` (was `floor-pivots.pine`) holds three independent engines —
     classic floor pivots + CPR, the Camarilla equation, and previous day —
     each with its own history depth, styling and label placement, all reading
     ONE shared source period (⚙️ General → Resolution)
   - ⚠️ `pivots.pine` floor ladder was TradingView's **Classic** (R3 = P+2(H−L))
     while calling itself "classic floor-trader pivots" — colloquial "classic"
     is NOT TradingView's Classic type. Traditional (R3 = 2P+(H−2L)) is the
     default everyone else's chart shows; the two diverge by exactly (H−P) at
     rung 3 and widen outward (+26.7 / +53.3 pts on a 60-pt ES day). Now a
     `PivotFormula` input, Traditional default, R5/S5 added (Traditional-only,
     na on Classic). Verified against TradingView's published formulas for
     Traditional, Classic and Camarilla — Camarilla H1–H5/L1–L5 already matched
     exactly; H6/L6 are our extension beyond TradingView's set
   - `pivots.pine` requests with `settlement_as_close.on` as well as
     `session.regular`: on futures the daily close becomes the exchange
     SETTLEMENT, which is the close floor pivots are defined on. Left to
     inherit it follows a chart setting, so the same symbol drew different
     pivots for different viewers
   - ⚠️ `pivots.pine` collapsed to that single shared resolution on 2026-09-29
     for COST: a `request.security` inside a user-defined function is
     instantiated PER CALL SITE and fetched on every bar regardless of whether
     its call site's guard runs, so per-engine resolutions meant three
     permanent nine-series HTF fetches (~50% of runtime on the profiler) while
     the "sharing rules" only skipped array bookkeeping. Two call sites remain:
     the shared engine source, and Previous Day's daily fallback (it is daily
     by definition and its close must come from the daily series to land on
     settlement). `calc_bars_count` dropped 5000 → 2000 at the same time
   - `pivots.pine` labels are QUEUED (`LevelLabel`), not drawn on the spot, so
     all three engines can sit on the SAME side (the default) without
     overlapping. Once every engine has drawn, two passes run: labels sharing
     an anchor time group into RUNS by Collision Distance (percent of price,
     matched against each run's FIRST member — matching against every member
     chains runs end to end, and anchoring lets a label that cleared the run
     drop back to column 0), then each steps inward past the earlier members of
     its own run by `Σ(len(earlier code) + gap)` CHARACTERS so the gap holds at
     every zoom. Nothing moves vertically and nothing guesses at a pixel
     distance — Pine exposes no vertical zoom, so a label's HEIGHT can only be
     stood in for by a price distance. Same pattern as
     `options-positioning-map.pine`, which learned the same lesson: levels do
     not have to share a price to collide

10. **`options-positioning-map.pine`** (was `options-gex-levels.pine`)
    - Options positioning map — the whole book projected onto price, not gamma
      alone: gamma walls + flip, delta (D1-D3) and vega (V1-V3) exposure, open
      interest and volume concentrations, hedging peak, max pain, the expected
      move band, an expiry marker, and IV30/HV30 + P/C chain context carried in
      the FLIP and VEX tooltips
    - Parses a pasted LADDER row (or a whole session of them) from
      `input.text_area()`; the chart serves the most recent row the current bar
      has reached, so bar replay walks the session forward
    - STATIC BY DESIGN: nothing changes until a new row is served. Every
      change-gate (`opmLastDrawnBar`, `opmNeedsRefresh`, `opmActiveIndex`, the
      level scalars, the tooltip strings) is `varip` — a plain `var` gate rolls
      back per realtime tick and re-runs the whole pipeline. `opmLastDataText`
      is deliberately NOT varip: the parse writes UDT fields, which roll back
      anyway, so it must re-run until it lands on a confirmed execution
    - Drawing pool is minted once, blank, on `barstate.islastconfirmedhistory`;
      the render is `set_*` only
    - Every drawing lives on the TIME axis (`xloc.bar_time`), not on bar
      indices, so the map can be clamped to a minute on the clock: two shared
      edges (`opmMapLeft`/`opmMapRight`) feed every line, label and box. The
      right edge stops at the feed's own `EXPTIME` and pins there once passed —
      levels run to the expiration line, freeze, and stay dimmed through the
      post-market, the overnight and the next pre-market until a row with a
      LATER expiry is served. `opmAfterExpiry` is an absolute timestamp test;
      a minute-of-day test un-dims a spent map at midnight
    - No `plot()` / `alertcondition()`, so it is NOT Pine Screener eligible —
      correctly, a paste-driven map has nothing to screen on
    - Carries the repo's UDT-over-parallel-arrays pattern: one
      `array<OpmSlot>` (code, note, hoverText, price, visible, ownsStrike,
      padChars, cluster) replaced eight slot-keyed parallel arrays
    - Section prefix is `opm`, not `gex` (renamed 2026-09-25). Gamma is one
      LAYER of this map, beside delta, vega, open interest, volume, max pain
      and the expected move — naming the whole file after it mislabelled six
      of the seven. The letters `gex` now appear only where gamma exposure is
      genuinely meant: `opmTotalGex` and `opmAbsGex1-3`. Three names were wrong
      past the prefix and were fixed with it: `gexCall1`→`opmCallWall1` (a wall,
      not a call), `gexAbs1`→`opmAbsGex1` ("abs" of what?), and
      `gexRange*`→`opmExpMove*` (its own input group says Expected Move).
      Feed-facing strings were deliberately NOT renamed — the parser still
      matches the row's own keys `"GEX"`, `"GEXNET"`, `"DEX1"`, `"VEX1"`
    - `opmExtendBars` (📏 Structure) sets the right overhang in bars. It
      lengthens the run past the last bar and nothing else: the expiration
      clamp still wins, so no level can be pushed past its contract's last
      trading minute however large the input is set

11. **`quote-window.pine`**
    - Intermarket day-type panel: 4 cash indexes, 4 e-mini futures, the 11
      sector ETFs, each row a net % change, sorted descending. Two requests per
      symbol (38 total, plus a daily ATR): `[close[1], open]` daily under
      `lookahead_on` (neither leaks — both are settled before the bar exists,
      and lookahead is REQUIRED there or `close[1]` is two days stale), and the
      current price at the CHART timeframe under `lookahead_off`. Replay-,
      history- and live-accurate; nothing repaints
    - Every request goes through `ticker.modify(session = session.regular)`.
      Plain symbols inherit the CHART's session, so with Extended Hours on a
      daily `open` becomes the 04:00 print and `close[1]` the 20:00 one — the
      two baselines silently changed meaning per user. Caveat: "regular
      session" for CME futures is exchange-defined, not 09:30-16:00
    - Baseline modes: vs prior close (default), vs today's open, Both, and
      `vs SPY (relative)` which rebases every row to `row% − SPY%` on UDT
      `.copy()`s so the verdict engine still reads untouched originals
    - The VERDICT FOLLOWS THE BASELINE (2026-10-02 — it used to be hard-wired to
      vs-close, so the banner never changed and the input looked broken).
      `Today's Open` runs the verdict, pair check and row colours vs the open
      with every tier ×`QW_OPEN_TIER_SCALE` 0.64 (moves from the open are
      ~0.64× moves from the close); FUTURES vs-open is their price at the 09:30
      cash open (per-call-site `var` snapshot in `f_qwMakeReading`), not the
      globex daily open. `Both` / `vs SPY` keep the verdict on vs-close. The
      verdict row always names its baseline (`· vs open` / `· vs close`)
    - Opening Range: daily ATR is `ta.atr(14)[1]` under `lookahead_on`
      (yesterday's settled ATR on every bar — the old lookahead_off form used
      TODAY'S developing ATR live, so live and history disagreed); baseline EMA
      60 sessions (was 20 — out-of-sample R² 0.062→0.098 QQQ, 0.129→0.185 SPY
      on 426 sessions; opening volume and prior-day range overfit and were left
      out)
    - TWO independently-toggled day-type rows, **both OFF by default**, either
      of which can render alone as a corner banner:
      · **Regime Verdict** — COMMITTED / MILD / LOW CONV / BIFURCATED /
        DATA GAP. Severity is asymmetric and must stay that way: INDEXES are a
        hard veto (any mix of red and green), SECTORS are GRADED (>25% minority
        caps the verdict below COMMITTED; only a near-50/50 split vetoes).
        Commodity sectors are discounted ONLY when on the minority side. Tiers
        0.2 noise (inclusive, so colour counts are strict >) / 0.5 serious /
        1.0 committed
      · **📐 Opening Range** — the chart symbol's first-N-minute range ÷ daily
        ATR against its own trailing EMA baseline → WIDE / NORMAL / NARROW.
        Self-calibrating because fixed cutoffs mis-bucket across symbols.
        Scales TARGETS, never position size
    - **MEASURED, 2026-09-27, SPY + QQQ, 1,041 sessions each — read this before
      "improving" the verdict.** It has ZERO directional content (with- vs
      against-verdict excursion ratio 1.02/1.01). As a SIZE forecast the
      eleven sectors are beaten by the chart's own opening range: opening-range
      width alone R²=0.074/0.048, sector magnitude + agreement together 0.015,
      and the sectors add +0.001 on top. Sector AGREEMENT alone scores 0.0003.
      The cash↔futures pair check fires 0 times in 434 RTH sessions (SPY/ES
      r=0.9845) because ETF and future are arbitraged to basis points, and
      inverts outside RTH where cash does not tick. The verdict is kept for
      fidelity, not because it contributes
    - Futures continuous contracts are not back-adjusted, so `close[1]` spans
      the quarterly roll. The roll window is COMPUTED (second Thursday of
      Mar/Jun/Sep/Dec, derived from the bar's own day-of-week/day-of-month,
      exact 2024-2030) and suppression is gated on a clean sweep of every
      comparable pair
    - The `🧪` CSV log layer that produced those measurements was STRIPPED
      2026-09-27 after the study closed (same doctrine as macd-waves' debug
      layer). Restore it from git history before any re-tuning pass rather
      than rebuilding it — it logged one row per session with every symbol's
      raw percentage on BOTH baselines, which is what made verdict variants
      rebuildable offline without a re-export
    - Uses AI.md's sanctioned global-inputs exception; the constraint is
      documented in the file header

12. **`ticker-tape.pine`**
    - Realtime time-and-sales tape + block-trade engine on
      `request.security_lower_tf("1T")`, with iceberg detection, pro-flow
      readout, and gated alerts
    - REAL PRINTS ONLY — the chart-volume-delta fallback (one Σ-tagged aggregate
      row standing in for unseen trades) was removed 2026-08-10 and must not be
      reintroduced: a sum of unseen trades rendered as a trade cannot be
      classified, cannot be a block, and reads as order flow that never
      happened. A dead feed shows an empty tape
    - Source of truth for the shared block classifier — the `<<SYNC …>>` regions
      are mirrored into `ticker-block-trades.pine` by
      `scripts/sync-block-engine.sh` (run `--check` in CI/pre-commit)
    - Intraday tool — a daily chart exhausts the lower-timeframe allotment

13. **`hoi.pine`**
    - Hindenburg Omen signal: new highs/lows breadth thresholds, positive-trend
      and McClellan filters, rolling cluster-window confirmation

14. **`ticker-block-trades.pine`**
    - Sub-pane companion to `ticker-tape.pine`: histogram of block-trade COUNT
      per bar (individual prints ≥ the size threshold, never cumulative volume)
    - Exists as a separate file because `overlay` is fixed at compile time — a
      pane version cannot be a runtime toggle on the tape
    - Classifier + `COND_*` codes are GENERATED from `ticker-tape.pine` between
      the `<<SYNC …>>` markers; edit them there, then run
      `scripts/sync-block-engine.sh`. Never hand-edit a synced region
    - Bar color = order-flow lean: NORD8 cyan buy-side / NORD11 red sell-side,
      two tiers per side (transp 45 aggressive, transp 70 passive) reusing the
      tape's five block-square color slots and names
    - Watermark-gated per-bar recount held in `varip` SCALARS; zero-block bars
      plot `na` (not 0) so the baseline stays bare

15. **`obv.pine`**
    - On Balance Volume (Barry Burns methodology) — smart-money/accumulation
      detector in its own pane
    - OBV drawn thin/neutral (width 1); the signal MA OF OBV (SMA, Auto 15
      min) is the hero line, slope-colored with the same blue up/down pair as
      the macd-waves signal line and stochastic %D, with the line/MA fill
    - Deliberately carries no trend lines or horizontal S/R (Barry rejects both
      on OBV) — the signal MA is the only reference
    - THE REFERENCE PATTERN for cvd, composite-breadth and
      volume-split-momentum (see "Signal MA lengths" for the shared pane). It alone uses the
      built-in `indicator(timeframe = "", timeframe_gaps = false)` because it
      draws nothing; no zero line because a chart-start cumulative total has
      no meaningful zero

16. **`cvd.pine`**
    - Cumulative Volume Delta for QQQ / big tech on the 2-MINUTE / 6-MINUTE
      pair. Rebuilt 2026-10-02, leaned to the obv.pine pattern 2026-10-03
    - DELTA = `request.footprint(ticks_per_row = 100)` → `.delta()`, the ONLY
      source (one call per script; Premium+). MEASURED on the cvd logs: where
      1-second data exists (last ~8 sessions on a 2-min chart) it is IDENTICAL
      to 1-second bars signed close vs open (2,514 bars, 0 diff) — NOT bid/ask
      aggressor data; older bars come at ~1-minute resolution. The 1-second
      intrabar request, Resolution/Budget inputs, delta-source input, slope
      colours, Style and smoothing line were removed as redundant; never
      offer a 1-tick resolution (200K budget = 1-3 h of QQQ)
    - ANCHOR default SESSION (Henry's call). DECAY = total × (1 − 2/(N+1)) +
      delta, N = 30 bars. Week / Month / Continuous kept. The reset comes from
      the SESSION (`session.isfirstbar[_regular]`), not `timeframe.change("1D")`
      — they disagree on an extended-hours chart — and is unconditional,
      separate from the accumulation (the 04:00 bar is the likeliest to have
      no footprint)
    - TWO SERIES: `cvdValue` is the private accumulator; `cvdSeries` is the
      rendered line, `na` outside the session under Regular Hours Only and
      before the anchor's first measured bar. Pivot readings take `cvdSeries`.
      A mid-session feed gap is NOT unmeasured — the level carries forward
    - NO `runtime.error` for a missing footprint: "symbol serves none" and
      "context serves none" (Bar Replay) are indistinguishable from inside
    - Pane = obv.pine: one ⚖️ group (Anchor, Decay Length [`active` only on
      Decay], Session Data, Zero Line); CVD NORD3 width 1; 〰️ Signal MA =
      the shared pane (SMA, Auto 30 min, slope NORD8 t20 / NORD9 t60, width 3,
      line/MA fill);
      🧮 Calculation (Timeframe + Wait for timeframe closes, default OFF like
      obv's `timeframe_gaps = false`) built manually because
      indicator(timeframe=) is barred for scripts that draw. The MA runs on a
      rolling sample window (one per Calculation-timeframe bar; SMA/EMA/RMA/
      WMA/VWMA/stdev rebuilt on arrays, EMA/RMA seeded from the window SMA)
      and RESTARTS at every anchor reset — an average holding the pre-reset
      period would paint every open as a cross. Wait-for-close saves nothing:
      it only blanks the plot between HTF closes
    - Divergences: pivots 5/5 on PRICE, CVD read on the same bars, extension
      ≥ 0.75 ATR(14) as of the pivot bar, range 5-30 bars, same-anchor guard
      on `cvdAnchorStartBar[divergencePivotRight]`. Default REGULAR (changed
      from Both 2026-10-03 after Henry reported hidden false signals); regular
      dotted / hidden dashed; R/H label tooltips carry the edge (footprint, 63
      sessions, Session anchor, 20 min): reg bear +7.9 bps 73% n22 · reg bull
      +2.0 52% n40 · hid bull +3.0 54% n35 but −0.1 at 30 min · hid bear +0.6
      46% n39. HIDDEN HAS NO EDGE OVER THE PRICE SWING ALONE: the same higher
      low without the CVD condition reads +2.2 bps 58% (n168); every rescue
      filter tried (extension 1.0/1.5 ATR, net delta ≥10/20% of swing volume,
      day's-flow side) either stayed flat, flipped sign by month, or left
      n<12. The logic is correct (hidden = net delta between the two swings
      against price's direction); it just does not predict. Lines and state
      commit on confirmed closes only
    - Code comments and tooltips carry logic only (emoji + bullets, key
      values); dates, sample sizes and provenance live here, not in the file
    - NO `alertcondition()`

17. **`volume-split-momentum.pine`** (🔋 VSM, built 2026-10-03)
    - Henry's request: "same idea as VBSM (2tm) but far superior". VBSM sums
      cumulative ROC on falling-volume bars (NVI) and rising-volume bars (PVI)
      — the sum IS price (corr 0.9999 with cumulative % move), so its fill is
      price vs its 25 SMA (DIRECTION −0.07, 47% hit on 29 sessions)
    - VSM keeps the halves APART: line = cum(ROC × +1 on HEAVY bars, −1 on
      LIGHT bars), heavy = volume > SMA(volume, 120 min) incl. current bar.
      Session's first bar ROC = 0 (overnight gap). Read = line vs signal MA
    - MEASURED on the cvd logs (58 sessions Jul–Sep, QQQ, ETH, scored on RTH,
      line − MA, DIRECTION = ½IC + ½partial IC vs trailing 20 min at 10/20/30
      min; SHIFT as in the CBI work), worst month:
      2-min: VSM +0.035 / shift +0.025 · VBSM −0.010 / −0.040 · OBV −0.030 /
      −0.021 · CVD session +0.011 / +0.007
      6-min: VSM +0.032 / +0.009 · VBSM −0.012 / −0.091 · OBV −0.001 / −0.006
      · CVD +0.005 / +0.005
      The edge is in DISTANCE from the MA, not the colour: following the
      above/below side alone is ~50-51% hit, +0.4-1.1 bps / 20 min
    - Rejected variants: PVI, NVI, PVI−NVI (sign flips by month); time-of-day
      relative volume (worse than trailing); participation-weighted ROC×rvol;
      heavy threshold 1.2/1.5 (fails a month); 0.8 also fine. Windows MUST be
      in minutes: 20-bar signal on 6-min (2 h) fails July (−0.041); 40-min
      signal works on both → Auto (now 30 min, see Signal MA lengths),
      baseline 120 min
    - OBV pattern exactly: built-in `indicator(timeframe = "",
      timeframe_gaps = false)` (no drawings), line NORD3 width 1, signal MA
      width 3 + line/MA fill, no zero line (chart-start cumulative), vendor
      volume guard, NO alerts. Not compiled by Henry yet at time of writing
    - Analysis scripts: scratchpad vbm1-4.py (cvd-logs)
    - MERGE WITH CVD TESTED AND REJECTED (2026-10-03, merge1/2.py): z-blends
      of VSM + delta increments at 1:1/2:1/1:2/3:1 all lose VSM's worst-month
      direction (−0.015 to +0.015); delta split by heavy/light, ROC × delta
      ratio, |delta|-defined heavy bars all worse. "VSM only on bars where
      delta agrees with price" is a wash (6-min worst dir +0.041 vs +0.032,
      but 2-min shift avg +0.049 vs +0.057) and would add a footprint
      dependency. Divergences on VSM do NOT carry CVD's edge: reg bear +0.2
      bps/20m (CVD +7.9, 73%). Keep two panes: VSM = direction, CVD =
      regular-bearish divergence. `simple` qualifiers on f_vsmBars params are
      required — untyped-qualifier params made signalLength series and
      ta.ema/ta.rma refused it

18. **`agreement-strategy.pine`** (🤝 VAS, strategy(), built 2026-10-03)
    - Henry's "all panes agree" trade as a Strategy Tester script. Recomputes
      VSM, CVD (footprint, session anchor) and CBI (whole-market engine,
      constant weights) exactly as the panes do; 6-minute states built from
      the chart's bars at each `time_close("6")` close. OBV deliberately out
      (removing it improved the offline test)
    - Entry: all three on the trade's side of their signal MAs on 2-min AND
      6-min, %D(5/2/3) ≥ 85 long / ≤ 15 short (first bar of the setup), no
      entries 11:30-13:30 or after 15:40. Fills next open
    - Exits in thirds: stop beyond the 10-bar swing; T1 at +0.5R or first
      disagreement (strategy.close + cancel T1) → stop to breakeven; T2 at +1R;
      T3 when all three flip against, BE stop, or 15:56
    - Offline expectation (63 sessions, Jul–Oct): win ~47%, +0.054%/trade,
      PF ~3.5, ~1.9 trades/day — chosen from 120 combos, expect lower live
    - Commission 0.005% per side (= 1 bp round trip as tested); capital 250k
      so 300 QQQ shares fit at 100% margin
    - ENTRY MODE input (2026-10-03, Henry: "the entries are wrong"): default
      "Cycle Hook" = Henry's rules — all three SIGNAL-MA SLOPES agree (pane
      colour), longs only when rising / shorts only when falling, %D hooks up
      from < 20 (down from > 80) on the bar close; disagreement exits use the
      slopes too. "Momentum Push" = the line-vs-MA + %D-at-extreme version.
      6-min agreement and lunch skip now default OFF (not in Henry's rules).
      OFFLINE (slope.py/slope2.py, 63 sessions): Cycle Hook PF 0.53, win 32%,
      negative every month; %D crossing back through 20/80 PF 0.58; line slopes
      PF 0.41. Momentum Push at the same defaults PF 2.03, win 35%

### Signal MA lengths — all four volume/breadth panes (2026-10-03, siglen.py)
- SHARED PANE PATTERN (OBV, CVD, VSM, CBI — keep identical): main line NORD3
  width 1; 〰️ Signal MA (Type SMA/EMA, ☑ Auto + Length inline), slope-colored
  NORD8 t20 / NORD9 t60 width 3; `signalFillColor` fill between line and MA
  (NORD8 t90 above / NORD9 t95 below); Style tab order line → fill → MA via
  the hidden `signalFillEdge` plot. CVD/CBI add the 🧮 Calculation group
- TYPES REDUCED to SMA / EMA only (Henry, 2026-10-03): None, SMA + Bollinger
  Bands, SMMA (RMA), WMA and VWMA removed with their code (BB plots, stdev,
  WMA/VWMA helpers, sample-volume arrays). OBV/VSM compute ta.sma AND ta.ema
  every bar and pick one (no conditional ta.* calls); CVD/CBI keep one
  rolling sample window — SMA = full-window mean, EMA seeded from it. Hide
  the MA from the Style tab instead of a "None" type
- CBI fill row sits ABOVE Signal MA in the Style tab: the MA is plotted
  twice — a hidden `editable = false` edge plot for fill(), then the visible
  line (Style tab lists entries in declaration order; fill must follow its
  plots)
- UI: an "Auto" checkbox (default ON) inline with "Length"; Length is greyed
  out (`active = not signalAutoLength`) while Auto is on and holds the 2-min
  equivalent (OBV 8 / CVD 15 / VSM 15 / CBI 120) for when it is unticked.
  f_signalAutoBars clamps to 3..1000 bars; a bar of ≥1 day → 20 bars. OBV/VSM
  keep it simple-qualified (ta.ema/ta.rma need simple int)
- AUTO is set in MINUTES (a fixed bar count is a
  different window on 2-min vs 6-min — "20 bars" was 40 min vs 2 h, and at 2 h
  OBV and CVD read BACKWARDS). Non-intraday falls back to 20 bars; CVD/CBI
  count minutes in Calculation-timeframe bars
- Measured on line − MA DIRECTION, worst month 2-min / 6-min:
  · OBV  SMA 15 min (8 / 3 bars)   ≈ +0.02 / +0.034  (old 20 bars: −0.030 / −0.073)
  · CVD  SMA 30 min (15 / 5 bars)  +0.008 / +0.005   (old: +0.011 / −0.057)
  · VSM  SMA 30 min (15 / 5 bars)  +0.047 / +0.038   (old 40 min: +0.035 / +0.032)
  · CBI  EMA 240 min (120 / 40)    +0.033 / +0.034   (old 20 bars: −0.021 / −0.019);
    every CBI length under ~90 min is negative — breadth momentum mean-reverts,
    only a slow baseline helps. CBI type default changed SMA → EMA
- Signal-line COLOUR (slope) is ~50-52% hit at every length on every pane — it
  is cosmetic; the distance from the MA is the read
- VSM bug fixed same pass: `session.isfirstbar ? 0` zeroed EVERY bar on daily
  charts / Timeframe ≥ 1D (flat line) → now `timeframe.isintraday and …`

### Common Features Across Indicators

- **Nord Theme**: All use NORD0-NORD15 color constants
- **Grouped Inputs**: Organized with GROUP_* constants and emoji prefixes
- **Helper Functions**: Prefixed with `f_`
- **Table Rendering**: Created in `barstate.islastconfirmedhistory` or `barstate.islast`
- **Tooltips**: Extensive use for user guidance
- **Conditional Coloring**: Threshold-based color selection
- **Type Safety**: Custom type definitions where needed

---

## 🤖 Final Checklist for AI Assistants

Before submitting any code changes, verify:

- [ ] `//@version=6` at the top of file
- [ ] Mozilla Public License header included
- [ ] Emoji banner sections, 80-column dividers, CONSTANTS → TYPE DEFINITIONS →
      GENERAL → feature sections → PLOTS/RENDER last (a global 🎛️ inputs
      section only under the documented sanctioned exception)
- [ ] Nord color constants defined (NORD0-NORD15, all 16, never trimmed)
- [ ] Group constants defined with emoji prefixes
- [ ] ALL function parameters explicitly named (positional ONLY for the four
      documented exceptions: variadics, `color.t`, casts, `max_bars_back`)
- [ ] ALL variables have meaningful names (no single letters except standard abbreviations)
- [ ] Helper functions prefixed with `f_`
- [ ] EVERY input has `group = GROUP_*`, and a `tooltip =` wherever the
      tooltip says something the title does not (an inline pair may share one
      tooltip on the pair). NO PURE-RESTATEMENT TOOLTIPS (Henry, 2026-07-31):
      a Show/Color/Width/Style quartet inside a `➖ Zero Line` group needs no
      "Show the zero baseline." — the group name already said it. Titles must
      not repeat their group name either. Missing tooltips on that class of
      input are correct, not debt
- [ ] Tables created once with `var`, populated in `barstate.islastconfirmedhistory`
      or `barstate.islast`; per-event drawings minted ONLY on confirmed ticks
- [ ] No `var`-guarded `alert()`/`log.*` on realtime paths (rollback re-fires
      them per tick) — gate on `barstate.isconfirmed` or use `varip`
- [ ] No `label.new`/`label.delete` (or line/box) on intrabar ticks — `set_*` only
- [ ] Conditional coloring uses ternary operators
- [ ] Number formatting appropriate for data type; every formatted field
      na-guarded, fallbacks are "N/A"/"-" (never "$0" or a printable NaN)
- [ ] `ignore_invalid_symbol = true` wherever the REQUEST can fail, which is
      not the same question as whether the symbol exists. Required on foreign
      feeds and constructed tickers (`composite-breadth`, `hoi`,
      `support-resistance`, `fundamental-view-indicator`). Also required on
      `request.security_lower_tf` even for `syminfo.tickerid`, because there
      the failure is "no tick stream on this symbol/plan/session", not a bad
      symbol (`ticker-tape`, `ticker-block-trades` — pair it with
      `ignore_invalid_timeframe`). NOT needed on a plain `request.security`
      against `syminfo.tickerid`: the chart's own symbol always resolves, so
      the flag is a no-op and the repo omits it deliberately (`ma-waves`,
      `macd-waves`, `technical-view-indicator`)
- [ ] Function signatures verified against Pine Script v6 Reference
- [ ] No deprecated v4/v5 functions used
- [ ] Repainting considerations addressed (lookahead, barmerge, varip reload caveat)
- [ ] No forward references — all identifiers declared before first use
- [ ] Session-modified tickers used consistently within each section
- [ ] UDTs preferred over parallel arrays for related data

---

## 📝 Additional Notes

### Performance Considerations
- Use `ignore_invalid_symbol = true` on any `request.*()` that can FAIL, so it
  degrades to `na` instead of erroring the script out: foreign or constructed
  tickers, and every `request.security_lower_tf` (a symbol/plan/session with no
  tick stream fails even on the chart's own symbol — pair it with
  `ignore_invalid_timeframe`). A plain `request.security` on `syminfo.tickerid`
  does not need it
- Use `lookahead = barmerge.lookahead_on` only for stable snapshot requests;
  confirmed-event streams (HTF pivots) need `lookahead_off` — see Pitfall 5
- Render tables/labels only in `barstate.islast` or `barstate.islastconfirmedhistory`
- Do not rescan an entire retained higher-timeframe history array on every new
  HTF bar when the signal is natively confirmable with built-ins like
  `ta.pivothigh()` / `ta.pivotlow()`. Prefer incremental maintenance:
  request confirmed HTF pivots with `request.security()`, append only newly
  confirmed candidates, prune aged-out candidates, and rebuild derived levels
  only when the candidate set actually changes.
- When TradingView's profiler shows a high percentage on an `if` line, treat
  that as the cost of the whole block under that branch, not just the condition
  itself.
- Use `var` keyword for variables that should persist across bars
- Cache constant `math.log()` results with `var` when used repeatedly (e.g.,
  `var float logTen = math.log(number = 10.0)`)
- Avoid heavy per-level lookback loops — prefer computing touch/acceptance
  scores per cluster zone rather than per individual level
- Prefer UDT arrays over parallel arrays to reduce sort and access overhead
- `array.sort()` / `array.sort_indices()` / `matrix.sort()` support UDT
  collections via `sort_field` (since April 2026), and `array.binary_search*()`
  searches them (August 2026, pre-sorted ascending by the same field) — prefer
  these over manual sort loops unless the ordering needs custom logic (na
  handling, multi-key)

### String Formatting
- Use `str.format()` for complex formatting with placeholders
- Use `str.tostring()` with format constants: `format.volume`, `format.currency`, `format.percent`
- Use `math.round()` before formatting for decimal precision control
- Triple-quoted multiline string literals (`"""..."""`) are VALID Pine v6 —
  each code line becomes a text line (newlines inserted automatically, leading
  indentation included literally); strings may hold up to 40,960 characters.
  Do not flag them as syntax errors in review.

### Error Handling
- Always handle `na` values with conditional checks
- Use `na(value) ? "N/A" : formatted_value` pattern for display strings
- Provide fallback colors for missing data: `na(value) ? textColor : conditionalColor`

---

## 🔗 Quick Reference Links

- **LLM-Optimized Pine Script v6**: https://github.com/codenamedevan/pinescriptv6
- **Master Navigation**: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/LLM_MANIFEST.md
- **Official Pine Script Docs**: https://www.tradingview.com/pine-script-docs/
- **Pine Script v6 Reference**: https://www.tradingview.com/pine-script-reference/v6/
- **Repainting Concepts**: https://www.tradingview.com/pine-script-docs/concepts/repainting/

---

**Last Updated**: 2026-10-02
**Repository**: `/Users/henryoliver/Projects/Trading/pinescript-indicators`

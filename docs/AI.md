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

**NON-NEGOTIABLE RULE**: Never use positional arguments. ALWAYS name ALL parameters explicitly.

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

**Verification Required:**
- **Always check the Pine Script v6 Reference** for correct parameter names
- If a function doesn't have documented parameter names, positional arguments are acceptable as last resort
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
    table.cell(table_id = tapeTable, column = 0, row = tickIndex, text = str.tostring(tickPrice))
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
f_labelCell(table t, int col, int row, string txt) =>
    table.cell(table_id = t, column = col, row = row, text = txt,
         text_color = labelColor, text_size = labelSize,
         text_halign = labelHalign, text_valign = labelValign,
         text_font_family = labelFontFamily, bgcolor = tableBackgroundColor)

// Helper function to format large numbers
f_formatNumber(float val) =>
    if na(val)
        "N/A"
    else if val >= 1e12
        str.format("{0, number, #.00}T", val / 1e12)
    else if val >= 1e9
        str.format("{0, number, #.00}B", val / 1e9)
    else if val >= 1e6
        str.format("{0, number, #.00}M", val / 1e6)
    else
        str.format("{0, number, #,###}", val)

// Helper function to get earnings date string
f_getEarningsDateString(int timestamp) =>
    if na(timestamp)
        "N/A"
    else
        string monthName = switch month(timestamp)
            1 => "Jan"
            2 => "Feb"
            3 => "Mar"
            // ... etc
            => "N/A"
        str.format("{0} {1}", monthName, year(timestamp))
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
tickerId = ticker.modify(syminfo.tickerid, session = session.regular) // inferred as string
pivotHighArray = array.new<pivotPoint>()        // inferred as array<pivotPoint>
```

#### When types MUST be declared
```pine
float myPrice = na       // na alone is ambiguous — type required
int myBar = na           // same: must declare when initializing to na
var float persistedVal = na
```

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

**Limitation:** `array.sort()` does not work on UDT arrays — there is no
built-in comparator. A manual sort loop is still needed, but each swap is one
`array.get`/`array.set` pair instead of N.

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
bool isEpsEvent = ta.change(currEpsActual) != 0 and not na(currEpsActual)

// Historical earnings using ta.valuewhen
float epsQ0 = ta.valuewhen(isEpsEvent, currEpsActual, 0)  // Most recent
float epsQ1 = ta.valuewhen(isEpsEvent, currEpsActual, 1)  // Previous quarter
int epsTime0 = ta.valuewhen(isEpsEvent, time, 0)
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
string regularSymbol = ticker.modify(syminfo.tickerid, session = session.regular)

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
string mktCapStr = na(mktCap) ? "N/A" : str.tostring(mktCap, format.volume)
```

**Percentages:**
```pine
string epsYoyStr = na(epsYoyVal) ? "XX" : str.format("{0}%", math.round(epsYoyVal, 1))
string adrFormatted = str.format("{0, number, #.00}%", adrRounded * 100)
```

**Currency:**
```pine
string avgPrice = na(syminfo.target_price_average) ? "$0" :
     str.format("${0}", math.round(syminfo.target_price_average, 2))
string revenueVal = na(revenue) ? "XX" : str.tostring(revenue, format.currency)
```

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
f_labelCell(table t, int col, int row, string txt) =>
    table.cell(table_id = t, column = col, row = row, text = txt,
         text_color = labelColor, text_size = labelSize,
         text_halign = labelHalign, text_valign = labelValign,
         text_font_family = labelFontFamily, bgcolor = tableBackgroundColor)

f_valueCell(table t, int col, int row, string txt) =>
    table.cell(table_id = t, column = col, row = row, text = txt,
         text_color = valueColor, text_size = valueSize,
         text_halign = valueHalign, text_valign = valueValign,
         text_font_family = valueFontFamily, bgcolor = tableBackgroundColor)

f_emptyCell(table t, int col, int row) =>
    table.cell(table_id = t, column = col, row = row, text = "",
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
- Use `lookahead = barmerge.lookahead_on` for real-time data accuracy
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

### 8. Never Forward-Reference Variables or Functions
- Pine Script v6 has no hoisting — all identifiers must be declared above their
  first use
- Cross-cutting inputs belong in GENERAL, not in the section that "owns" the
  feature, if other sections above it need them
- Helper functions called from a section must be defined before that section

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

1. **`fundamental-view-indicator.pine`**
   - Displays comprehensive fundamental data table
   - Includes: Market cap, ROE, float, analyst recommendations, price targets, EPS/revenue history
   - Vertical two-column table (label + value)
   - Uses `request.financial()` and `request.earnings()`

2. **`technical-view-indicator.pine`**
   - Single-row horizontal table with technical metrics
   - Includes: Market cap, float, volume, dollar volume, P/E, P/S, ADR, ATR, RPS
   - Uses `request.financial()` and `request.security()`

3. **`ma-waves.pine`**
   - Moving average wave counting indicator (Barry Burns methodology)
   - Uses custom type definitions (Trend, Wave, Cycle, Price)
   - Implements wave labeling with impulses and retracements
   - Uses `label.new()` for wave annotations

4. **`options-gex-levels.pine`**
   - Options gamma exposure (GEX) levels indicator
   - Parses CSV data from `input.text_area()`
   - Renders horizontal lines and zones for key GEX levels
   - Uses arrays to manage lines/labels/boxes

5. **`macd-waves.pine`**
   - Advanced MACD with wave identification
   - Identifies momentum waves based on MACD structure

6. **`stochastic.pine`**
   - Standard Stochastic Oscillator
   - Customizable bands and styling

7. **`support-resistance.pine`**
   - Multi-indicator cluster map for support and resistance
   - Combines Fibonacci, floor pivots, previous day, round numbers, major
     swings, Murrey Math, and value area into cluster zones
   - Uses `request.security()`, `request.footprint()`, and drawing objects
   - Renders in `barstate.islast` with line/label/box arrays

8. **Market breadth indicators**
   - `market-updown-volume-delta.pine` - NASDAQ 100 up/down volume delta
   - `market-advdecl-issues-delta.pine` - NASDAQ 100 advance/decline delta

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
- [ ] Emoji section headers in correct order (🧱 🧩 🎛️ 🧮)
- [ ] Nord color constants defined (NORD0-NORD15)
- [ ] Group constants defined with emoji prefixes
- [ ] ALL function parameters explicitly named (no positional arguments)
- [ ] ALL variables have meaningful names (no single letters except standard abbreviations)
- [ ] Helper functions prefixed with `f_`
- [ ] Inputs grouped with `group = GROUP_*`
- [ ] Table/label/line creation in `barstate.islastconfirmedhistory` or `barstate.islast`
- [ ] Tooltips provided for user-facing inputs
- [ ] Conditional coloring uses ternary operators
- [ ] Number formatting appropriate for data type (volume, currency, percent)
- [ ] Function signatures verified against Pine Script v6 Reference
- [ ] No deprecated v4/v5 functions used
- [ ] Repainting considerations addressed (lookahead, barmerge)
- [ ] No forward references — all identifiers declared before first use
- [ ] Session-modified tickers used consistently within each section
- [ ] UDTs preferred over parallel arrays for related data

---

## 📝 Additional Notes

### Performance Considerations
- Use `ignore_invalid_symbol = true` for `request.*()` functions
- Use `lookahead = barmerge.lookahead_on` for real-time accuracy
- Render tables/labels only in `barstate.islast` or `barstate.islastconfirmedhistory`
- Use `var` keyword for variables that should persist across bars
- Cache constant `math.log()` results with `var` when used repeatedly (e.g.,
  `var float logTen = math.log(number = 10.0)`)
- Avoid heavy per-level lookback loops — prefer computing touch/acceptance
  scores per cluster zone rather than per individual level
- Prefer UDT arrays over parallel arrays to reduce sort and access overhead
- `array.sort()` does not support UDT arrays — manual sort is still needed but
  operates on single elements instead of N parallel arrays

### String Formatting
- Use `str.format()` for complex formatting with placeholders
- Use `str.tostring()` with format constants: `format.volume`, `format.currency`, `format.percent`
- Use `math.round()` before formatting for decimal precision control

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

**Last Updated**: 2026-04-10
**Repository**: `/Users/henryoliver/Projects/Trading/pinescript-indicators`

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

Every indicator follows this consistent structure:

```pine
// Mozilla Public License 2.0 header
// © henry_oliver

//@version=6
indicator(title = "Full Name", shorttitle = "🎯 ABC", overlay = true)

// 🧱 CONSTANTS
const string GROUP_GENERAL = "⚙️ General"
const string GROUP_TABLE = "📋 Table"
// ... more group constants

// Nord Theme Colors
const color NORD0  = #2E3440
const color NORD1  = #3B4252
// ... NORD0-NORD15

// Calculation constants
const float MILLION = 1e6
const float BILLION = 1e9

// 🧩 TYPE DEFINITIONS (if needed)
type CustomType
    int field1
    float field2
    color field3

// 🎛️ USER INPUT SETTINGS
var string tablePosition = input.string(defval = position.top_right, title = "Position",
     options=[position.top_left, position.top_center, position.top_right], group = GROUP_TABLE)
// ... more inputs grouped by GROUP_*

// 🧮 DATA & CALCULATIONS
// Data fetching, calculations, indicator logic

// Helper functions (prefixed with f_)
f_helperFunction(params) =>
    // logic

// Main rendering logic
if barstate.islastconfirmedhistory or barstate.islast
    // Create and populate table/labels/lines
```

### Section Markers (Emoji Headers)

Use these **exact emoji section headers** in this order:

1. `// 🧱 CONSTANTS` - Group names, colors, calculation constants
2. `// 🧩 TYPE DEFINITIONS` - Custom type definitions (if needed)
3. `// 🎛️ USER INPUT SETTINGS` - All input.* functions
4. `// 🧮 DATA & CALCULATIONS` - Main logic, data fetching, calculations
5. Helper functions - Prefixed with `f_`
6. Rendering logic - Table/label/line creation

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

### 4. Emoji Shorttitle Pattern

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

7. **Market breadth indicators**
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

---

## 📝 Additional Notes

### Performance Considerations
- Use `ignore_invalid_symbol = true` for `request.*()` functions
- Use `lookahead = barmerge.lookahead_on` for real-time accuracy
- Render tables/labels only in `barstate.islast` or `barstate.islastconfirmedhistory`
- Use `var` keyword for variables that should persist across bars

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

**Last Updated**: 2026-03-05
**Repository**: `/Users/henryoliver/Projects/Trading/pinescript-indicators`

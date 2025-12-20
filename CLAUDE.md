# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains Pine Script indicators for TradingView that display fundamental and technical analysis metrics. All indicators are written in Pine Script (versions 5 and 6) and designed to overlay on TradingView charts with customizable table displays.

## Essential Pine Script Documentation

**MUST READ AND UNDERSTAND** these references before coding Pine Script:

1. **Pine Script Documentation**: https://www.tradingview.com/pine-script-docs/welcome/
   - Comprehensive guide to Pine Script language and concepts

2. **Pine Script v6 Reference**: https://www.tradingview.com/pine-script-reference/v6/
   - Complete API reference for all built-in functions and constants

3. **Repainting Concept**: https://www.tradingview.com/pine-script-docs/concepts/repainting/#introduction
   - Critical understanding of how Pine Script recalculates on historical vs real-time bars
   - Affects data accuracy and indicator reliability

## Coding Conventions

### ALWAYS Use Verbose Parameter Names

**CRITICAL**: Always use explicit parameter names in ALL function calls. Never use positional arguments.

**❌ WRONG - Do NOT use positional arguments:**
```pine
indicator("Price Tape", "⚡ Tape", overlay = false, max_bars_back = 0)
input.bool(true, "Show Volume")
table.new(position.top_right, 5, 2)
```

**✅ CORRECT - Always use explicit parameter names:**
```pine
indicator(title = "Price Tape", shorttitle = "⚡ Tape", overlay = false, max_bars_back = 0)
input.bool(defval = true, title = "Show Volume")
table.new(position = position.top_right, columns = 5, rows = 2)
```

**IMPORTANT: This applies even when using conditional expressions or ternary operators:**

**❌ WRONG - Skipping parameter name for conditional value:**
```pine
plot(emaVisible ? ema : na, "EMA", emaColor, emaWidth, emaOffset)
label.new(bar_index, high, "Label", label.style_label_down, waveColor, waveColor)
```

**✅ CORRECT - All parameters explicitly named, even with conditionals:**
```pine
plot(series = emaVisible ? ema : na, title = "EMA", color = emaColor, linewidth = emaWidth, offset = emaOffset)
label.new(x = bar_index, y = high, text = "Label", style = label.style_label_down, color = waveColor, textcolor = waveColor, size = size.normal)
```

This applies to ALL Pine Script functions including:
- `indicator()`, `strategy()`, `library()`
- All `input.*()` functions (`input.bool()`, `input.float()`, `input.int()`, `input.string()`, `input.color()`, etc.)
- All `request.*()` functions (`request.security()`, `request.financial()`, `request.earnings()`, etc.)
- All `table.*()` functions (`table.new()`, `table.cell()`, `table.merge_cells()`, etc.)
- All `plot*()` functions (`plot()`, `plotshape()`, `plotchar()`, etc.)
- All `ta.*()` functions (`ta.sma()`, `ta.rsi()`, `ta.atr()`, etc.)
- All `label.*()` and `line.*()` functions
- All other built-in functions

**Refer to the Pine Script v6 Reference documentation for the complete parameter names for each function.**

### Common Parameter Naming Mistakes to Avoid

1. **DO NOT skip the first parameter name** - Even though Pine Script allows it, always name it explicitly
2. **DO NOT use positional arguments after the first few parameters** - Name ALL parameters
3. **DO NOT assume parameter order** - Different functions have different parameter orders
4. **DO NOT mix positional and named arguments** - Use named arguments exclusively

## Code Architecture

### Core Design Pattern

All indicators follow a consistent architecture:

1. **Type System**: Custom types (`indicatorObject`, `indicatorVisibilityObject`) encapsulate indicator data (text, color, tooltip)
2. **Input Configuration**: Extensive `input.*` functions for user customization (thresholds, colors, visibility)
3. **Data Fetching**: `request.security()`, `request.financial()`, `request.earnings()` for real-time and historical data
4. **Conditional Rendering**: Visibility arrays filter indicators before table creation
5. **Table Display**: Dynamic table generation in `barstate.islast` block with merged cells and tooltips

### Indicator Files

**fund-tech-indicators.pine** (v5)
- Combined fundamental and technical indicators in a single table
- Displays up to 7 fundamental metrics (EPS, Sales, ROE, Market Cap, Float Shares)
- Displays up to 4 technical metrics (ADR, ATR, 52-week high, RPS)
- Uses two-section table with optional titles

**market-breadth.pine** (v5)
- Nearly identical to fund-tech-indicators.pine
- Same indicator set and structure
- Appears to be a duplicate or variant for market breadth monitoring

**trend-intensity-relative-strength.pine** (v5)
- Overlay=false (separate pane below chart)
- Four visualization components:
  - Relative Strength: Colored line comparing ticker to benchmark (default SPY)
  - Trend Intensity: Area plot when 7-day/65-day SMA ratio exceeds thresholds
  - Breakout/Breakdown: Character markers (▲▼) for 4%+ price moves
  - 52-week High/Low: Circle markers at extremes

**technical-view-indicator.pine** (v6)
- Single-row horizontal table overlay
- 8 technical metrics: Volume, Dollar Volume, Price, PE Ratio, ADR, ATR, RPS, VWAP
- Nord theme color palette constants (NORD0-NORD15)
- Text customization: size, font family, alignment

**fundamental-view-indicator.pine** (v6)
- Two-column vertical table (label + value)
- 9 fundamental metrics following CANSLIM methodology:
  - Market Cap, Annual ROE, EPS % Change (Last Qtr), 3-Yr EPS Growth
  - Sales % Change (Last Qtr), 3-Yr Sales Growth, IPO Date, Sector, Industry
- Nord theme with extensive styling options
- Color-coded thresholds based on CANSLIM criteria (e.g., 25% EPS growth, 17% ROE)

### Common Patterns

**Data Retrieval**
```pine
float currEps = request.earnings(ticker = syminfo.tickerid, field = earnings.actual, ignore_invalid_symbol = true, lookahead = barmerge.lookahead_on)
float annualRoe = request.financial(symbol = syminfo.tickerid, financial_id = "RETURN_ON_EQUITY", period = "FY", ignore_invalid_symbol = true)
```

**Conditional Coloring**
```pine
color epsGrowthColor = (epsGrowth >= epsGrowthAbove) ? colorIndAbove : (epsGrowth <= epsGrowthBelow) ? colorIndBelow : colorIndNeutral
```

**Event Detection**
```pine
bool isEpsEvent = ta.barssince(currEpsActual != currEpsActual[1] or currEpsStandard != currEpsStandard[1]) == 0
```

**Number Formatting**
- All indicators use switch/ternary logic to format large numbers (M/B/T suffixes)
- Percentage formatting: `str.format("{0, number, 0.00%}", value)`
- Currency formatting: `str.format("{0, number, currency}", value)`

**Table Creation**
- v5 indicators: Single table with `createTableCells()` helper function
- v6 indicators: Direct `table.cell()` calls with explicit positioning
- Both use `barstate.islast` to render only on final bar

### Nord Theme Colors

The v6 indicators use the Nord color palette:
- **Polar Night** (NORD0-3): Dark backgrounds, UI elements
- **Snow Storm** (NORD4-6): Text, light elements
- **Frost** (NORD7-10): Accents, positive indicators (teal/blue)
- **Aurora** (NORD11-15): Status colors (red/orange/yellow/green/purple)

## Development Notes

### Version Differences
- **Pine Script v5**: Used in fund-tech-indicators, market-breadth, trend-intensity
  - Simpler table API, helper functions for cell creation
- **Pine Script v6**: Used in technical-view, fundamental-view
  - Enhanced features: `dynamic_requests`, `behind_chart`, `force_overlay` flags
  - More granular text formatting (font family, explicit sizing)

### Financial Metrics
All fundamental indicators rely on TradingView's financial data API:
- Quarterly data: `period = "FQ"`
- Annual data: `period = "FY"`
- Common financial IDs: `TOTAL_REVENUE`, `RETURN_ON_EQUITY`, `TOTAL_SHARES_OUTSTANDING`, `EARNINGS_PER_SHARE_BASIC`

### CANSLIM Methodology
The fundamental-view-indicator follows William O'Neil's CANSLIM investment criteria with specific thresholds:
- EPS growth: 25%+ (strong), <0% (decline)
- Sales growth: 25%+ (strong), <10% (weak)
- Annual ROE: 17%+ (strong), <10% (weak)
- IPO age: <10 years preferred

### Performance Considerations
- All indicators use `ignore_invalid_symbol = true` to handle invalid tickers gracefully
- `lookahead = barmerge.lookahead_on` for real-time data accuracy
- Table rendering only on `barstate.islast` to avoid redundant calculations

## Pine Script Language Notes

- Variables: `var` keyword for initialization once per chart (not per bar)
- Constants: `const` for immutable values
- Type annotations: Required for custom types and most declarations
- Arrays: `array.from()`, `array.push()`, `array.get()`
- Ternary: `condition ? valueIfTrue : valueIfFalse`
- Comments: `//` for single-line, no multi-line syntax
- String interpolation: Use `str.format()` or `+` concatenation

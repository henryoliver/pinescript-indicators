# Project Overview

This project is a collection of Pine Script indicators for the TradingView platform. The indicators provide a range of functionalities, from displaying fundamental company data and technical metrics to advanced wave counting and momentum analysis. The scripts are written in Pine Script version 6 and share a consistent "Nord" color theme.

## Indicators

*   **`fundamental-view-indicator.pine`**: Displays a comprehensive table of fundamental data for a given stock, including market cap, ROE, float, analyst recommendations, price targets, and historical EPS/revenue data.
*   **`technical-view-indicator.pine`**: Shows a table of key technical metrics, such as Market Cap, Float, Average Daily Volume, P/E and P/S ratios, ADR, ATR, and Relative Price Strength (RPS).
*   **`macd-waves.pine`**: An advanced MACD indicator that identifies and labels momentum waves based on the MACD's structure (higher highs, lower lows, etc.).
*   **`mas-waves.pine`**: Implements the "Top Dog Trading" wave counting methodology by Barry Burns, using a combination of moving averages and a stochastic oscillator to label price and momentum waves.
*   **`price-tape.pine`**: Simulates a "time and sales" tape, providing a real-time view of order flow by sampling 1-second data (requires a TradingView premium subscription).
*   **`stochastic.pine`**: A standard Stochastic Oscillator indicator with customizable bands and styling.
*   **`ndx-updown-volume-delta.pine`**: Tracks the difference between NASDAQ 100 up volume and down volume, visualized as a histogram with Nord theme colors. Data sources: `USI:UPVOL.NQ` and `USI:DNVOL.NQ`.
*   **`ndx-advdecl-issues-delta.pine`**: Tracks the difference between NASDAQ 100 advancing and declining issues, visualized as a histogram with Nord theme colors. Data sources: `USI:ADVN.NQ` and `USI:DECL.NQ`.

## Development Conventions

*   **Pine Script Version 6**: All scripts use `@version=6`.
*   **Styling**: The indicators share a common "Nord" color theme, with constants defined for colors.
*   **Inputs**: User-configurable inputs are grouped for better organization in the indicator settings.
*   **File Structure**: Each indicator is a self-contained `.pine` file.
*   **Verbose Parameter Naming**: ALWAYS use explicit parameter names in ALL function calls where the official Pine Script v6 documentation specifies parameter names. **You MUST verify this in the documentation first.** Never use positional arguments if named parameters are available. This applies to all Pine Script functions, including `indicator()`, `input.*()`, `request.*()`, `table.*()`, `plot*()`, `ta.*()`, `label.*()`, `line.*()`, and all other built-in functions. If the official documentation for a function shows no parameter names, then positional arguments are acceptable as a last resort. Refer to the Pine Script v6 Reference documentation for complete parameter names.

## Building and Running

There are no explicit build commands for this project. To use these indicators:

1.  Open a chart on [TradingView](https://www.tradingview.com).
2.  Open the "Pine Editor" from the bottom panel.
3.  Copy the code from one of the `.pine` files and paste it into the editor.
4.  Click "Add to Chart".

Alternatively, you can publish these indicators on TradingView to use them across different devices and share them with others.

## References

### ⚠️ MANDATORY REQUIREMENT - READ BEFORE EVERY FILE UPDATE

**CRITICAL**: You MUST read and consult the official Pine Script documentation **EVERY TIME** you update any `.pine` file in this project. This is not optional - it is a mandatory step to ensure:

1.  **Correct Syntax**: Use the latest Pine Script v6 syntax and avoid deprecated methods
2.  **Best Practices**: Follow TradingView's recommended coding patterns and conventions, including **always using verbose parameter names**.
3.  **Avoid Reinventing the Wheel**: Leverage built-in functions and idioms instead of custom implementations
4.  **Prevent Errors**: Understand language requirements (e.g., local scope blocks, proper parameter naming)
5.  **Stay Current**: Keep code updated with the latest Pine Script features and improvements

### Essential Pine Script Documentation

**READ THESE BEFORE CODING:**

1.  **Pine Script v6 Examples and Patterns**
    [https://github.com/codenamedevan/pinescriptv6](https://github.com/codenamedevan/pinescriptv6)
    *Community examples demonstrating v6 syntax and common patterns*

2.  **Pine Script Documentation (Comprehensive Guide)**
    [https://www.tradingview.com/pine-script-docs/welcome/](https://www.tradingview.com/pine-script-docs/welcome/)
    *Complete guide covering concepts, language features, and methodology*

3.  **Pine Script v6 Reference (Function/Constant Lookup)**
    [https://www.tradingview.com/pine-script-reference/v6/](https://www.tradingview.com/pine-script-reference/v6/)
    *API reference for all built-in functions, variables, and constants - USE THIS for parameter names*

4.  **Repainting Concepts (Critical for Indicator Accuracy)**
    [https://www.tradingview.com/pine-script-docs/concepts/repainting/](https://www.tradingview.com/pine-script-docs/concepts/repainting/)
    *Understanding how Pine Script recalculates - essential for accurate indicators*

### Workflow for File Updates

1.  **Review current file** to understand its purpose and structure
2.  **Consult Pine Script v6 Reference** for correct function signatures and parameter names
3.  **Check Pine Script Documentation** for language requirements and best practices
4.  **Implement changes** following the coding conventions in this `GEMINI.md` file (especially verbose parameter naming)
5.  **Verify syntax** matches current v6 standards
6.  **Test compilation** to catch errors before committing

## 🤖 LLM Usage Instructions for Pine Script v6 Documentation

If you are an LLM or AI Assistant, follow these comprehensive instructions for accessing and using Pine Script v6 documentation.

### 📚 Documentation Source

**Repository**: https://github.com/codenamedevan/pinescriptv6
**Purpose**: Restructured Pine Script v6 documentation optimized for AI consumption, addressing context limitations and hallucination prevention

---

## 🗺️ Navigation Strategy

### Primary Entry Point
**Always start with**: `LLM_MANIFEST.md` - This is the master index and navigation map for the entire documentation collection.

### Repository Structure
```
pinescriptv6/
├── LLM_MANIFEST.md           # Master navigation guide (START HERE)
├── concepts/                  # Core language concepts
│   ├── execution_model.md    # Bar-by-bar execution, var keyword
│   ├── timeframes.md         # Multi-timeframe analysis, repainting
│   ├── colors_and_display.md # Color functions, transparency
│   └── common_errors.md      # Troubleshooting guide
├── reference/
│   ├── variables.md          # Built-in variables (open, close, high, low, etc.)
│   ├── constants.md          # Color values, style constants, enums
│   └── functions/
│       ├── ta.md             # Technical analysis (RSI, EMA, SMA, etc.)
│       ├── strategy.md       # Backtesting, order placement, position management
│       ├── request.md        # External data retrieval (security, financial, etc.)
│       ├── drawing.md        # Visual elements (plot, line, box, label, etc.)
│       └── collections.md    # Arrays, matrices, maps
├── writing_scripts/          # Guides and practical examples
└── visuals/                  # Chart rendering documentation
```

---

## 🎯 Modular Retrieval Protocol

**CRITICAL**: Do NOT attempt to ingest the entire codebase at once. Use targeted retrieval based on the specific question type.

### Query-to-File Routing

| User Question Type | Primary Files to Retrieve |
|-------------------|---------------------------|
| **Technical Analysis** (RSI, EMA, crossovers) | `reference/functions/ta.md` |
| **Backtesting/Strategies** | `reference/functions/strategy.md` |
| **Moving Averages** | `reference/functions/ta.md` |
| **Data Retrieval** (financial data, other symbols) | `reference/functions/request.md` |
| **Drawing/Plotting** (lines, labels, shapes) | `reference/functions/drawing.md` |
| **Arrays/Matrices** | `reference/functions/collections.md` |
| **Built-in Variables** (bar_index, close, volume) | `reference/variables.md` |
| **Constants** (colors, styles) | `reference/constants.md` |
| **Execution Issues** (var keyword, bar-by-bar) | `concepts/execution_model.md` |
| **Repainting Issues** | `concepts/timeframes.md` |
| **Compile/Runtime Errors** | `concepts/common_errors.md` |

### Complex Query Examples

**Example 1**: "Create an RSI indicator with custom colors"
- Retrieve: `reference/functions/ta.md` (for RSI function)
- Retrieve: `reference/functions/drawing.md` (for plot function)
- Retrieve: `concepts/colors_and_display.md` (for color handling)

**Example 2**: "Build a moving average crossover strategy"
- Retrieve: `reference/functions/ta.md` (for SMA/EMA functions)
- Retrieve: `reference/functions/strategy.md` (for entry/exit orders)
- Retrieve: `concepts/execution_model.md` (for understanding execution flow)

**Example 3**: "Fix variable reset on every bar"
- Retrieve: `concepts/execution_model.md` (for var keyword behavior)
- Retrieve: `concepts/common_errors.md` (for troubleshooting)

---

## ⚠️ Critical Rules for Code Generation

### 1. Version Enforcement
**ALWAYS** include `//@version=6` at the top of every Pine Script file.

```pine
//@version=6
indicator("My Indicator")
```

### 2. Use Namespace Functions
Prefer built-in namespace functions over manual calculations:

✅ **CORRECT**:
```pine
rsi_value = ta.rsi(source = close, length = 14)
ema_value = ta.ema(source = close, length = 20)
```

❌ **INCORRECT** (manual calculation when built-in exists):
```pine
// Don't manually implement RSI if ta.rsi exists
```

### 3. No Hallucinations
**If a function is not documented in the reference files, it likely does not exist in v6 or has been renamed.**

- DO NOT invent function names
- DO NOT assume v4/v5 syntax works in v6
- If uncertain, check the documentation first

### 4. Explicit Parameter Names
Always use explicit parameter names (as per the "Development Conventions" in this `GEMINI.md` file):

✅ **CORRECT**:
```pine
ta.sma(source = close, length = 50)
plot(series = my_value, title = "My Plot", color = color.blue, linewidth = 2)
```

❌ **INCORRECT** (positional arguments):
```pine
ta.sma(close, 50)
plot(my_value, "My Plot", color.blue, 2)
```

---

## 🔍 How to Use Documentation URLs

### Fetching Documentation During Conversations

When you need to solve a Pine Script issue:

1. **Identify the problem domain** (e.g., technical analysis, strategy, drawing)
2. **Determine which file(s) to fetch** using the routing table above
3. **Fetch the specific raw file** from GitHub

**URL Pattern**:
```
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/[path-to-file]
```

**Examples**:
```
# Technical analysis functions
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/ta.md

# Strategy/backtesting functions
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/strategy.md

# Execution model concepts
https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/concepts/execution_model.md
```

### When to Fetch Documentation

Fetch documentation when:
- User asks about a specific Pine Script function you're unsure about
- Compilation errors occur that might be related to v6 syntax changes
- User asks "how do I..." questions about Pine Script functionality
- You need to verify correct parameter names or function signatures

---

## 📖 Best Practices

### 1. Start Specific, Expand as Needed
Begin with the most relevant file, then expand to related files if needed:
```
User: "How do I calculate RSI?"
→ Fetch: reference/functions/ta.md (look for ta.rsi)
```

### 2. Combine Concept + Reference
For complex issues, combine conceptual understanding with function reference:
```
User: "Why is my variable resetting every bar?"
→ Fetch: concepts/execution_model.md (understand bar-by-bar execution)
→ Fetch: concepts/common_errors.md (check for related errors)
```

### 3. Verify Before Suggesting
If you're about to suggest a function or syntax:
- Check if it exists in the appropriate reference file
- Verify parameter names and types
- Confirm it's v6 compatible

---

## 🚫 Common Pitfalls to Avoid

1. **Don't mix v4/v5 syntax with v6**
   - Some functions were renamed or moved to namespaces in v6
   - Always verify function names in the reference docs

2. **Don't assume positional arguments work**
   - While Pine Script allows them, the project conventions require explicit parameter names

3. **Don't create custom implementations for built-in functions**
   - Check `ta.md` before implementing any technical indicator manually

4. **Don't forget about namespace changes**
   - v6 introduced namespaces like `ta.`, `strategy.`, `request.`, etc.

---

## 📝 Documentation Disclaimer

This is a **community-maintained restructuring** of official Pine Script v6 documentation, not affiliated with TradingView. It's designed purely for AI efficiency and retrieval-augmented generation workflows.

---

## 🔗 Quick Reference URLs

- **Repository**: https://github.com/codenamedevan/pinescriptv6
- **Manifest**: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/LLM_MANIFEST.md
- **TA Functions**: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/ta.md
- **Strategy Functions**: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/strategy.md
- **Drawing Functions**: https://raw.githubusercontent.com/codenamedevan/pinescriptv6/main/reference/functions/drawing.md
- **Official TradingView Docs**: https://www.tradingview.com/pine-script-docs/
# Project Overview

This project is a collection of Pine Script indicators for the TradingView platform. The indicators provide a range of functionalities, from displaying fundamental company data and technical metrics to advanced wave counting and momentum analysis. The scripts are written in Pine Script version 6 and share a consistent "Nord" color theme.

## Indicators

*   **`fundamental-view-indicator.pine`**: Displays a comprehensive table of fundamental data for a given stock, including market cap, ROE, float, analyst recommendations, price targets, and historical EPS/revenue data.
*   **`technical-view-indicator.pine`**: Shows a table of key technical metrics, such as Market Cap, Float, Average Daily Volume, P/E and P/S ratios, ADR, ATR, and Relative Price Strength (RPS).
*   **`macd-waves.pine`**: An advanced MACD indicator that identifies and labels momentum waves based on the MACD's structure (higher highs, lower lows, etc.).
*   **`mas-waves.pine`**: Implements the "Top Dog Trading" wave counting methodology by Barry Burns, using a combination of moving averages and a stochastic oscillator to label price and momentum waves.
*   **`price-tape.pine`**: Simulates a "time and sales" tape, providing a real-time view of order flow by sampling 1-second data (requires a TradingView premium subscription).
*   **`stochastic.pine`**: A standard Stochastic Oscillator indicator with customizable bands and styling.

## Development Conventions

*   **Pine Script Version 6**: All scripts use `@version=6`.
*   **Styling**: The indicators share a common "Nord" color theme, with constants defined for colors.
*   **Inputs**: User-configurable inputs are grouped for better organization in the indicator settings.
*   **File Structure**: Each indicator is a self-contained `.pine` file.

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

1. **Correct Syntax**: Use the latest Pine Script v6 syntax and avoid deprecated methods
2. **Best Practices**: Follow TradingView's recommended coding patterns and conventions
3. **Avoid Reinventing the Wheel**: Leverage built-in functions and idioms instead of custom implementations
4. **Prevent Errors**: Understand language requirements (e.g., local scope blocks, proper parameter naming)
5. **Stay Current**: Keep code updated with the latest Pine Script features and improvements

### Essential Pine Script Documentation

**READ THESE BEFORE CODING:**

1. **Pine Script v6 Examples and Patterns**
   [https://github.com/codenamedevan/pinescriptv6](https://github.com/codenamedevan/pinescriptv6)
   *Community examples demonstrating v6 syntax and common patterns*

2. **Pine Script Documentation (Comprehensive Guide)**
   [https://www.tradingview.com/pine-script-docs/welcome/](https://www.tradingview.com/pine-script-docs/welcome/)
   *Complete guide covering concepts, language features, and methodology*

3. **Pine Script v6 Reference (Function/Constant Lookup)**
   [https://www.tradingview.com/pine-script-reference/v6/](https://www.tradingview.com/pine-script-reference/v6/)
   *API reference for all built-in functions, variables, and constants - USE THIS for parameter names*

4. **Repainting Concepts (Critical for Indicator Accuracy)**
   [https://www.tradingview.com/pine-script-docs/concepts/repainting/](https://www.tradingview.com/pine-script-docs/concepts/repainting/)
   *Understanding how Pine Script recalculates - essential for accurate indicators*

### Workflow for File Updates

1. **Review current file** to understand its purpose and structure
2. **Consult Pine Script v6 Reference** for correct function signatures and parameter names
3. **Check Pine Script Documentation** for language requirements and best practices
4. **Implement changes** following the coding conventions in CLAUDE.md
5. **Verify syntax** matches current v6 standards
6. **Test compilation** to catch errors before committing

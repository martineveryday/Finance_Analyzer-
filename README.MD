# Finance Analyzer (First Draft)

## Overview
Welcome to the **Finance Analyzer** project! This tool is designed to help you easily load and analyze financial data from CSV files. You can use it to calculate expenses, categorize transactions, and compare income and expenses.

Please note that this is the **first draft**, and the final version is still under development. I appreciate your patience as I continue to refine and improve the tool.

## Features
- Load multiple CSV files containing financial data
- Calculate total expenses from a dataset
- Categorize transactions based on specified columns
- Compute total income from multiple sources
- Determine the difference between income and expenses

## How It Works
1. **FileLoader Class**: Reads CSV files and stores them in a dictionary.
2. **FinanceAnalyzer Class**:
   - Computes total expenses from a given column.
   - Groups transactions by category and summarizes spending.
   - Calculates total income from multiple inputs.
   - Computes the difference between income and expenses.
3. **Main Function**:
   - Loads a sample CSV file (`bank1.csv`)
   - Computes total expenses and categorized spending
   - Displays the results

## Getting Started
To use this tool, ensure you have **Python** and **pandas** installed. You can run the script with:
```sh
python your_script.py
```

## Next Steps
- Enhancing error handling
- Adding support for more file formats
- Improving user input validation
- Adding Data Visualization

Stay tuned for updates!


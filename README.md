# NBA Player Stat Analysis

This Python script allows you to analyze and calculate the standard deviation of counting statistics for a specific NBA player in a given season. It fetches data from the website "basketball-reference.com" based on the player's name and the desired year, processes the data, and presents the mean and standard deviation of various statistical categories.

## Prerequisites

To run this script, you'll need:

- Python installed on your system.
- The `requests` library for making HTTP requests.
- The `pandas` library for data manipulation and analysis.

You can install the required libraries using the following commands:

```bash
pip install requests
pip install pandas
```

## How to Use

1. Open a terminal and navigate to the directory containing the `playerStatAnalysis.py` script.

2. Make the script executable if necessary. Run the following command:

   ```bash
   chmod +x playerStatAnalysis.py
   ```

3. Run the script using the command:

   ```bash
   ./playerStatAnalysis.py
   ```

4. Follow the prompts to input the NBA player's name and the desired season.

5. The script will fetch player's game log data from "basketball-reference.com," process it, and calculate the mean and standard deviation of various counting statistics.

6. The output will display the player's name, the specified season, mean statistics, and standard deviation statistics for the relevant counting categories.

## Features

- Fetches game log data for a specific NBA player in a given season from an external website.
- Calculates the mean and standard deviation of counting statistics such as field goals, three-pointers, free throws, rebounds, assists, steals, blocks, turnovers, and more.

## Note

Please be aware that the script fetches data from an external website, and its functionality might be affected if the website's structure or data format changes. The script may need adjustments in such cases.

## Disclaimer

This script is provided as-is and may not have full error handling or extensive testing. Use it responsibly and feel free to modify it to suit your needs.

For more information about the script's implementation and functions, refer to the script's comments and the [pandas documentation](https://pandas.pydata.org/docs/).

**Author**: Leo Chao

**Date**: 2023/08/13

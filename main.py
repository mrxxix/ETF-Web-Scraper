import requests
import pandas as pd
import sys

# Função com consequências do input do utilizador
def getUserInput():
    while True:
        numResults = input("Results to show (1-250) or 'exit': ").strip()

        if numResults.lower() == "exit":
            print("Script terminated by the user")
            sys.exit()

        try:
            numResults = int(numResults)  # Int value
            if 1 <= numResults <= 250:    # Int value inside the limits
                print(f"Showing {numResults} results.")
                return numResults
            else:                         # Int outside the limits
                print(f"Error: Input exceeds stablished limits (1-250). Input: {numResults}.")
                
        except ValueError:                # Not int value
            print("Error: Insert a valid number imput or 'exit'.")     

# Required headers to avoid API blocks
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Get result number
numResults = getUserInput()

# Historical API's URL
urlHistorical = "https://api.nasdaq.com/api/quote/JEPI/historical"
paramsHistorical = {
    "assetclass": "etf",
    "fromdate": "2024-06-03",
    "todate": "2025-06-03",
    "limit": numResults
}

# Resquest
response = requests.get(urlHistorical, headers=headers, params=paramsHistorical)

# JSON conversion
data = response.json()

# Scrape table data
rows = data['data']['tradesTable']['rows']

# Make a DataFrame with pandas
dataFrame = pd.DataFrame(rows)

# Print DataFrame
print(dataFrame)
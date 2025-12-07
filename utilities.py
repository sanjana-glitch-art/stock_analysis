#Helper Functions

import matplotlib.pyplot as plt
from datetime import datetime

from os import system, name

# Function to Clear the Screen
def clear_screen():
    if name == "nt": # User is running Windows
        _ = system('cls')
    else: # User is running Linux or Mac
        _ = system('clear')

# Function to sort the stock list (alphabetical)
def sortStocks(stock_list):
    ## Sort the stock list
    pass


# Function to sort the daily stock data (oldest to newest) for all stocks
def sortDailyData(stock_list):
    pass

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    # find stock
    for stock in stock_list:
        if stock.symbol==symbol:
            # check if data exists or not
            if len(stock.DataList)==0:
                print(f"No data available for {symbol}")
                return
            
            #sort data by date
            sortDailyData(stock.DataList)

            #extract dates and prices
            dates=[data.date for data in stock.DataList]
            prices=[data.close for data in stock.DataList]

            #create chart
            plt.figure(figsize=(10,6))
            plt.plot(dates,prices,marker='o',linestyle='-', linewidth=2, markersize=4)
            plt.title(f"{stock.name} ({stock.symbol}) - stock price history", fontsize=16)
            plt.xlabel("Date", fontsize=12)
            plt.ylabel("Price ($)", fontsize=12)
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            return
    
    print(f"stock {symbol} not found")
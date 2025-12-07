# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.

from datetime import datetime
from stock_class import Stock, DailyData
from utilities import clear_screen, display_stock_chart, sortDailyData
from os import path
import stock_data

# Main Menu
def main_menu(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Stock Analyzer ---")
        print("1 - Manage Stocks (Add, Update, Delete, List)")
        print("2 - Add Daily Stock Data (Date, Price, Volume)")
        print("3 - Show Report")
        print("4 - Show Chart")
        print("5 - Manage Data (Save, Load, Retrieve)")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","5","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Stock Analyzer ---")
            print("1 - Manage Stocks (Add, Update, Delete, List)")
            print("2 - Add Daily Stock Data (Date, Price, Volume)")
            print("3 - Show Report")
            print("4 - Show Chart")
            print("5 - Manage Data (Save, Load, Retrieve)")
            print("0 - Exit Program")
            option = input("Enter Menu Option: ")
        if option == "1":
            manage_stocks(stock_list)
        elif option == "2":
            add_stock_data(stock_list)
        elif option == "3":
            display_report(stock_list)
        elif option == "4":
            display_chart(stock_list)
        elif option == "5":
            manage_data(stock_list)
        else:
            clear_screen()
            print("Goodbye")

# Manage Stocks
def manage_stocks(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Stocks ---")
        print("1 - Add Stock")
        print("2 - Update Shares")
        print("3 - Delete Stock")
        print("4 - List Stocks")
        print("0 - Exit Manage Stocks")
        option = input("Enter Menu Option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("1 - Add Stock")
            print("2 - Update Shares")
            print("3 - Delete Stock")
            print("4 - List Stocks")
            print("0 - Exit Manage Stocks")
            option = input("Enter Menu Option: ")
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            update_shares(stock_list)
        elif option == "3":
            delete_stock(stock_list)
        elif option == "4":
            list_stocks(stock_list)
        else:
            print("Returning to Main Menu")

# Add new stock to track
def add_stock(stock_list):
    clear_screen()
    print("Add stock...")
    symbol=input("enter stock symbol: ").upper()
    name=input("enter company name: ")
    shares=float(input("enter number of shares: "))

    new_stock=Stock(symbol,name,shares)
    stock_list.append(new_stock)
    print(f"\n {symbol} added successfully!")
    input("press enter to continue...")
        
# Buy or Sell Shares Menu
def update_shares(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("update Shares...")
        print("1 - Buy Shares")
        print("2 - Sell Shares")
        print("0- Exit update Shares")
        option=input("Enter Menu Option: ")
        while option not in ["1","2","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Update Shares...")
            print("1 - Buy Shares")
            print("2 - Sell Shares")
            print("0- Exit update Shares")
            option=input("Enter Menu Option: ")
        if option == "1":
            buy_stock(stock_list)
        elif option == "2":
            sell_stock(stock_list)
        else:
            print("Returning to Manage Stocks Menu")

# Buy Stocks (add to shares)
def buy_stock(stock_list):
    clear_screen()
    print("Buy Shares ---")

    if len(stock_list)==0:
        print("No stocks in portfolio. Please add stocks.")
        input("Press enter to continue...")
        return
    
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    symbol =input("\n Enter stock symbol to buy shares: ").upper()

    stock_found =False
    for stock in stock_list:
        if stock.symbol == symbol:
            stock_found=True
            shares=float(input(f"Enter number of shares to buy for {symbol}: "))
            stock.buy(shares)
            print(f"\n Successfully purchased {shares} shares fo {symbol} ")
            print(f"Total shares owned: {stock.shares}")
            break
    
    if not stock_found:
        print(f"\n*** Stock {symbol} not found in portfolio. ***")
    input("Press Enter to continue...")

# Sell Stocks (subtract from shares)
def sell_stock(stock_list):
    clear_screen()
    print("Sell Shares...")
    if len(stock_list)==0:
        print("No stocks in portfolio. Please add stocks first.")
        input("Press enter to continue...")
        return
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    symbol =input("\n Enter stock symbol to sell shares: ").upper()

    stock_found=False
    for stock in stock_list:
        if stock.symbol==symbol:
            stock_found = True
            print(f"Current shares owned: {stock.shares}")
            shares= float(input(f"Enter number of shares to sell for {symbol}: "))

            if shares > stock.shares:
                print(f"\n*** Error: Cannot sell more shares than owned ({stock.shares}). ***")
            else:
                stock.sell(shares)
                print(f"\nSuccessfully sold {shares} shares of {symbol}.")
                print(f"Remaining shares owned: {stock.shares} ")
            break

        if not stock_found:
            print(f"\n*** Stock {symbol} not found in portfolio. ***") 
        
        input("Press Enter to continue...")

# Remove stock and all daily data
def delete_stock(stock_list):
    clear_screen()
    print("Delete Stock...")

    if len(stock_list)==0:
        print("no stocks in portfolio. Please add stocks first.")
        input("press enter to continue...")
        return
    
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    symbol=input("\n enter stock symbol to delete: ").upper()
    stock_found=False
    for i,stock in enumerate(stock_list):
        if stock.symbol==symbol:
            stock_found=True
            confirm=input(f"\nAre you sure you want to delete {symbol} and all its deta? (yes/no): ").lower()
            if confirm=="yes":
                stock_list.pop(i)
                print(f"\n{symbol} has been deleted successfully.")
            else:
                print("\n Deletion cancelled.")
            break
    
    if not stock_found:
        print(f"\n*** stock {symbol} not found in portfolio. ***")
    input("Press Enter to continue...")

# List stocks being tracked
def list_stocks(stock_list):
    clear_screen()
    print("Stock List...\n")
    if len(stock_list)==0:
        print("no stocks in portfolio.")
    else:
        print("\nSymbol | Company Name | Shares")
        print("-"*60)
        for stock in stock_list:
            print(f"{stock.symbol:6} | {stock.name:30} | {stock.shares:.2f}")
    
    input("\nPress Enter to continue...")

# Add Daily Stock Data
def add_stock_data(stock_list):
    clear_screen()
    print("Add Daily Stock Data ---")
    if len(stock_list)==0:
        print("No stocks in portfolio. Please add stocks first.")
        input("Press Enter to continue...")
        return

    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    symbol=input("\nEnter stock symbol:").upper()

    stock_found=False
    for stock in stock_list:
        if stock.symbol==symbol:
            stock_found=True
            date_str=input("Enter date (m/d/yy):")
            price=float(input("Enter closing price: "))
            volume=int(input("Enter volume: "))

            try:
                daily_data=DailyData(date_str,price,volume)
                stock.add_data(daily_data)
                print(f"\Daily data added successfully for {symbol} on {date_str}.")
            except Exception as e:
                print(f"\n ***Stock {symbol} not found in portfolio.***")
            break
    
    if not stock_found:
        print(f"\n*** stock {symbol} not found in portfolio. ***")
    input("Press Enter to continue...")

# Display Report for All Stocks
def display_report(stock_list):
    clear_screen()
    print("Stock Report...\n")
    
    if len(stock_list) == 0:
        print("No stocks in portfolio.")
    else:
        for stock in stock_list:
            print("=" * 50)
            print(f"Stock: {stock.symbol} - {stock.name}")
            print(f"Shares owned: {stock.shares}")
            print(f"Data points: {len(stock.DataList)}")
            if len(stock.DataList) > 0:
                # Sort data by date
                sortDailyData(stock.DataList)
                
                # Get first and last date - check if it's a datetime object or string
                first_date_obj = stock.DataList[0].date
                last_date_obj = stock.DataList[-1].date
                
                # Convert to string if it's a datetime object
                if hasattr(first_date_obj, 'strftime'):
                    first_date = first_date_obj.strftime("%m/%d/%y")
                else:
                    first_date = str(first_date_obj)
                
                if hasattr(last_date_obj, 'strftime'):
                    last_date = last_date_obj.strftime("%m/%d/%y")
                else:
                    last_date = str(last_date_obj)

                print(f"Date range: {first_date} to {last_date}")

                # Latest price
                latest_price = stock.DataList[-1].close
                print(f"Latest price: ${latest_price:.2f}")

                # Calculate total value
                total_value = stock.shares * latest_price
                print(f"Total value: ${total_value:.2f}")
            else:
                print("No price data available.")
            
            print()
    print("=" * 50)
    input("Press Enter to continue...")

# Display Chart
def display_chart(stock_list):
    clear_screen()
    print("Display chart...")

    if len(stock_list)==0:
        print("no stocks in portfolio.")
        input("\nPress enter to continue...")
        return
    print("\n stock list:[",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")
    symbol=input("\n enter stock symbol to display chart:").upper()

    stock_found=False
    for stock in stock_list:
        if stock.symbol==symbol:
            stock_found=True
            if len(stock.DataList)==0:
                print(f"\n no data available for {symbol}. Please retrieve data first.")
            else:
                print(f"\n displaying chart for {symbol}...")
                display_stock_chart(stock_list,symbol)
            break
    if not stock_found:
        print(f"\n*** stock {symbol} not found in porfolio. ***")
    
    input("\nPress enter to continue...")

# Manage Data Menu
def manage_data(stock_list):
    option = ""
    while option != "0":
        clear_screen()
        print("Manage Data ---")
        print("1 - Save Data")
        print("2 - Load Data")
        print("3 - Retrieve Data from web")
        print("4- Import Data from CSV")
        print("0 - Exit Manage Data")
        option =input("enter meru option: ")
        while option not in ["1","2","3","4","0"]:
            clear_screen()
            print("*** Invalid Option - Try again ***")
            print("Manage Data..... ")
            print("1-Save Data")
            print("2-Load Data")
            print("3-Retrieve Data from CSV")
            print("4-Import Data from CSV")
            print("0-Exit Manage Data")
            option=input("Enter Menu Option:")

        if option =="1":
            stock_data.save_stock_data(stock_list)
            print("Data Saved!")
            input("Press Enter to continue...")
        elif option=="2":
            stock_list.clear()
            stock_data.load_stock_data(stock_list)
            print(f"Data Loaded {len(stock_list)} stocks loaded.")
            input("Press Enter to continue...")
        elif option=="3":
            retrieve_from_web(stock_list)
        elif option=="4":
            import_csv(stock_list)
        else:
            print("Returning to Main Menu")

# Get stock price and volume history from Yahoo! Finance using Web Scraping
def retrieve_from_web(stock_list):
    clear_screen()
    print("Retrieve Data from Web ---")
    if len(stock_list)==0:
        print("no stocks in portfolio. Please add stocks first.")
        input("press enter to continue...")
        return
    print("\n Current Stocks:")
    for stock in stock_list:
        print(f"-{stock.symbol}: {stock.name}")
    
    print("\nNote: you can retrieve approx. 60 days of data at a time.")
    dateFrom =input("\nEnter stating Date (m/d/y):")
    dateTo =input("Enter ending Date (m/d/y):")

    print("\nretrieving data from Yahoo! Finance...")
    print("chrome windows will open for wach stock.\n")

    try:
        recordCount = stock_data.retrieve_stock_web(dateFrom, dateTo, stock_list)
        print(f"\n Scuccess! Retrieved {recordCount} records.")
    except Exception as e:
        print(f"\n Error: {str(e)}")
        print("check ChromeDriver and stock symbols.")
    
    input("Press Enter to continue...")

# Import stock price and volume history from Yahoo! Finance using CSV Import
def import_csv(stock_list):
    clear_screen()
    print("import data from CSV...")

    if len(stock_list)==0:
        print("no stocks in portfolio. Please add stocks first.")
        input("press enter to continue...")
        return
    
    print("\n stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    symbol=input("\n enter stock symbol to import data for:").upper()

    stock_exists=False
    for stock in stock_list:
        if stock.symbol==symbol:
            stock_exists=True
            break
    
    if not stock_exists:
        print(f"\n*** stock {symbol} not found in portfolio. ***")
        input("press enter to continue...")
        return
    
    filename=input("enter CSV filename :")

    try:
        stock_data.import_stock_web_csv(stock_list,symbol,filename)
        print(f"\n Successfully imported data for {symbol}")
    except Exception as e:
        print(f"\n Error: file '{filename} not found.")
    except Exception as e:
        print(f"\n Error importing CSV: {str(e)}")
    
    input("Press Enter to continue...")

# Begin program
def main():
    #check for database, create if not exists
    if path.exists("stocks.db") == False:
        stock_data.create_database()
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
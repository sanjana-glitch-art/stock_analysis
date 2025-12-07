# Stock_Analysis

A comprehensive Python-based stock portfolio management system with a console interface. Track your stock investments, retrieve historical data from Yahoo! Finance, visualize trends with charts, and manage your portfolio with ease.

# ✨ Features
  Portfolio Management
    **Add/Update/Delete Stocks:** Manage your stock portfolio with full CRUD operations
    **Buy/Sell Shares:** Track share purchases and sales
    **Portfolio Overview:** View all stocks with current holdings and values

  Data Management
    **Manual Data Entry:** Add daily stock data (date, price, volume) manually
    **Web Scraping:** Retrieve historical data from Yahoo! Finance using Selenium
    **CSV Import:** Import stock data from Yahoo! Finance CSV files
    **Database Storage:** Save and load portfolio data using SQLite

  Visualization & Reporting
    **Stock Charts:** Visual representation of price trends over time
    **Detailed Reports**: View comprehensive stock information, including:
                          Total shares owned
                          Date ranges
                          Latest prices
                          Total portfolio value
# 🚀 Getting Started
  Prerequisites
    Python 3.7 or higher
    Chrome browser (for web scraping)
    ChromeDriver (matching your Chrome version)

# Installation
  
  1. Clone the repository

    bash   git clone https://github.com/yourusername/stock-analyzer.git
           cd stock-analyzer
  
  2. Install required packages

    bash   pip install -r requirements.txt

  3. Download ChromeDriver

     Visit ChromeDriver Downloads
     Download the version matching your Chrome browser
     Extract and place chromedriver.exe in your project folder

  4. Set up PATH variable (for web scraping) Windows:

     Right-click on 'This PC' → Properties → Advanced System Settings
     Click 'Environment Variables'
     Under 'User variables', select 'Path' and click 'Edit.'
     Click 'New' and add your project folder path

     Linux/Mac:
     
         bash   export PATH=$PATH:/path/to/your/project/folder
     
# 📦 Required Libraries
  
  tkinter 
  beautifulsoup4
  selenium
  matplotlib
  sqlite3 

  _**Create a requirements.txt file:**_
    
    txtbeautifulsoup4==4.12.2
    selenium==4.15.2
    matplotlib==3.8.0

# 🎮 Usage

  Run the command-line interface:
      
      bash python stock_console.py
  
  Main Menu Options:
    Manage Stocks (Add, Update, Delete, List)
    Add Daily Stock Data (Date, Price, Volume)
    Show Report
    Show Chart
    Manage Data (Save, Load, Retrieve)
    Exit Program

# 📊 Project Structure

    stock-analyzer/
    │
    ├── stock_GUI.py              # GUI interface
    ├── stock_console.py          # Console interface
    ├── stock_class.py            # Stock and DailyData classes
    ├── stock_data.py             # Database operations
    ├── utilities.py              # Helper functions (charts, sorting)
    ├── stocks.db                 # SQLite database (created automatically)
    ├── chromedriver.exe          # Chrome driver for web scraping
    └── README.md                 # This file

# 💡 How to Use

  1. Adding a Stock

     Enter stock symbol (e.g., AAPL, MSFT, GOOGL)
     Enter company name
     Enter the number of shares owned

  2. Retrieving Historical Data
     Option 1: Web Scraping

       Add stocks to your portfolio
       Select "Scrape Data from Yahoo! Finance" from the Web menu
       Enter date range (m/d/yy format)
       Wait for Chrome to retrieve data (approximately 60 days at a time)

     Option 2: CSV Import

      Visit Yahoo! Finance
      Search for your stock symbol
      Click "Historical Data" tab
      Click "Download" to save CSV file
      In the application, select the stock and import the CSV file

  3. Viewing Reports and Charts
  
      Select "Show Report" to see detailed portfolio information
      Select "Show Chart" and enter stock symbol to visualize price trends
      Charts display historical closing prices over time

_**# ⚠️ Important Notes**_

**_Date Format: Always use m/d/yy format (e.g., 12/25/23)_**
_**Web Scraping Limitation: Yahoo! Finance allows approximately 60 days of data per request**_
_**Valid Stock Symbols: Ensure you use valid ticker symbols from major exchanges**_
_**ChromeDriver Version: Must match your Chrome browser version**_

# 🐛 Troubleshooting

  ChromeDriver Not Found:
    Ensure ChromeDriver is in your project folder
    Verify PATH environment variable is set correctly
    Check ChromeDriver version matches Chrome browser

  Import Errors:
    Install missing packages: pip install -r requirements.txt
    Ensure you're using Python 3.7+

  Date Format Errors:
    Always use m/d/yy format (e.g., 1/15/24)
    Ensure dates are valid


# 👨‍💻 Author
Sai Teja Sri Sanjana Thummalapalli

For questions or feedback about this project, please contact through GitHub issues.

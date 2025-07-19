Question 1: Use yfinance to Extract Stock Data

Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

CODE:	
import yfinance as yf

# Download Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

# Reset index
tesla_data.reset_index(inplace=True)

# Display first five rows
tesla_data.head()

Question 2: Use Webscraping to Extract Tesla Revenue Data

Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.

CODE:
import pandas as pd
import requests

# Set headers to pretend the request is coming from a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36"
}

# Get the HTML content from MacroTrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
response = requests.get(url, headers=headers)

# Read all tables from the HTML content
tables = pd.read_html(response.text)

# Find the correct table (with "Revenue" in column name)
tesla_revenue = None
for table in tables:
    if table.shape[1] == 2 and "Revenue" in table.columns[1]:
        tesla_revenue = table
        break

# Check if found
if tesla_revenue is None:
    raise ValueError("❌ Could not find Tesla revenue table.")

# Clean data
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r"\$|,", "", regex=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue.dropna(inplace=True)

# Show the last 5 rows
tesla_revenue.tail()

Question 3: Use yfinance to Extract Stock Data

Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

CODE:
# Download GameStop stock data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")

# Reset index
gme_data.reset_index(inplace=True)

# Display first five rows
gme_data.head()

Question 4: Use Webscraping to Extract GME Revenue Data

Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.

CODE:
import pandas as pd
import requests

# 1️⃣ Define the URL and a browser-like User-Agent header
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/113.0.0.0 Safari/537.36"
}

# 2️⃣ Fetch the page HTML
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raises an error if the request failed

# 3️⃣ Parse all tables from the HTML using pandas
tables = pd.read_html(response.text)

# 4️⃣ Identify the correct revenue table (2 columns + 'Revenue')
gme_revenue = None
for tbl in tables:
    if tbl.shape[1] == 2 and "Revenue" in tbl.columns[1]:
        gme_revenue = tbl
        break

if gme_revenue is None:
    raise ValueError("❌ GameStop revenue table not found!")

# 5️⃣ Clean the data
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r"\$|,", "", regex=True)
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
gme_revenue.dropna(inplace=True)

# 6️⃣ Display the last 5 rows
gme_revenue.tail()

Question 5: Plot Tesla Stock Graph

Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.

CODE:
import matplotlib.pyplot as plt

def make_graph(data, title):
    plt.figure(figsize=(14,6))
    plt.plot(data.Date, data.Close)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.show()

make_graph(tesla_data, "Tesla Stock Price Over Time")

Question 6: Plot GameStop Stock Graph

Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.

CODE:
make_graph(gme_data, "GameStop Stock Price Over Time")
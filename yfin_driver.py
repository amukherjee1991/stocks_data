from yfin_data import YFStocks

# Instantiate the YFStocks class with your Twelve Data API key
api_key = "d3b7c1458amsh18c268d298148c9p1f55ccjsn9a161d57b562"
yf_stocks = YFStocks(api_key)

# # Download and process the data for a specific exchange
exchange = "NASDAQ"
from twelve_data import RequestStocks

yf_stocks.download_exchange_data(exchange).to_csv("Nasdaq_stocks.csv",index=False)
# nyse = make_request("NYSE")

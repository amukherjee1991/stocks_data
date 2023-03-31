from twelve_data import RequestStocks

# Instantiate the RequestStocks class with your API key
api_key = "d3b7c1458amsh18c268d298148c9p1f55ccjsn9a161d57b562"
stocks = RequestStocks(api_key)

# Call the make_request function with your desired exchange
exchange = "NYSE"
response = stocks.make_request(exchange)

# Process the response to get tickers
tickers = stocks.process_response(response)

# Do something with the data
print(tickers)

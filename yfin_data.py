import yfinance as yf
from twelve_data import RequestStocks
import pandas as pd
import time

class YFStocks:

	'''
	needs API key of twelve data to get list of tickers
	'''
	def __init__(self, api_key):
		self.twelve_data = RequestStocks(api_key)

	'''
	uses an exchange name as an argument
	Retrieves response and process it get tickers as list
	list is then passed as an argument to yf.Tickers 'all_tickers' variable
	returns a dataframe
	'''
	def download_exchange_data_multi(self, exchange):
		response = self.twelve_data.make_request(exchange)
		all_tickers = self.twelve_data.process_response2(response)
		tickers = yf.Tickers(all_tickers)
		tickers_hist = tickers.history(period='max', interval='1d',)
		fin_data = tickers_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()
		return fin_data

	def download_exchange_data(self,exchange):
		response = self.twelve_data.make_request(exchange)
		all_tickers = self.twelve_data.process_response(response)
		final_data = pd.DataFrame()
		for at,name in all_tickers:
			time.sleep(3)
			ticker_object= yf.Ticker(at)
			data=ticker_object.history(period="max",interval="1d")
			data= data.reset_index()
			data['ticker']=at
			data['name']=name
			final_data = pd.concat([final_data, data])
		return final_data

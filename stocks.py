import yfinance as yf
import pandas as pd
import time
import urllib.request
import json
import tqdm
import requests
import os
api_key = os.environ.get('API_KEY')
if api_key is None:
    raise ValueError('API key is not set')

'''
Get all stock names and stuff based on exchanges
Exchanges like NASDAQ,NYSE
'''
class yf_stocks:
	def __init__(self):
		return self

	def make_request(exchange):
	    url = "https://twelve-data1.p.rapidapi.com/stocks"
	    querystring = {f"exchange":{exchange},"format":"json"}
	    headers = {
	    	"X-RapidAPI-Key": api_key,
	    	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
	    }
	    response = requests.get(url, headers=headers, params=querystring)
	    # response_text = json.loads(response.text)
	    return response.json()

	'''
	Process response to get tickers
	'''
	def process_response(response):
		tickers=[]
		name=[]
		for k,v in response.items():
			if k=="data":
				data=v
				for d in data:
					tickers.append(d["symbol"].lower())
					name.append(d["name"])
		return zip(tickers[:10],name[:10])


	'''
	Process response to get tickers
	only returns ticker/symbol
	returns a list which can be passed to download_exchange_data_multi
	'''
	def process_response2(response):
		tickers=[]
		name=[]
		for k,v in response.items():
			if k=="data":
				data=v
				for d in data:
					tickers.append(d["symbol"])

		return tickers
	'''
	creates a object for exchanges
	'''
	nasdaq=make_request("NASDAQ")
	nyse = make_request("NYSE")

	'''
	iterates over the tickers
	returns concatenated pandas data DataFrame
	'''

	def download_exchange_data(data):
		all_tickers = process_response(data)
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
	'''
	argument exchange is querystring
	Exchange names are like NYSE,NASDAQ as used by
	tweleve data
	Works only with US exchanges
	'''
	def download_exchange_data_multi(exchange):
		something=make_request(exchange)
		all_tickers = process_response2(something)
		tickers = yf.Tickers(all_tickers)
		tickers_hist = tickers.history(period='max',interval='1d',)
		fin_data =tickers_hist.stack(level=1).rename_axis(['Date', 'Ticker']).reset_index()
		return fin_data

# download_exchange_data_multi("NASDAQ").to_csv("NASDAQ_historical.csv",index=False)
# download_exchange_data_multi("NYSE").to_csv("NYSE_historical.csv",index=False)
#
#
# '''
# Downloads stock data and saves it to a csv
# '''
# download_exchange_data(nasdaq).to_csv("Nasdaq_stocks.csv",index=False)
# download_exchange_data(nyse).to_csv("NYSE_stocks.csv",index=False)
#
# print ("Files saved to project folder")

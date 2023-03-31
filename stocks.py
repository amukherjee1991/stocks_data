import yfinance as yf
import pandas as pd
import time
import urllib.request
import json
import tqdm
import requests

'''
Get all stock names and stuff based on exchanges
Exchanges like NASDAQ,NYSE
'''
def make_request(exchange):
    url = "https://twelve-data1.p.rapidapi.com/stocks"

    querystring = {f"exchange":{exchange},"format":"json"}

    headers = {
    	"X-RapidAPI-Key": "d3b7c1458amsh18c268d298148c9p1f55ccjsn9a161d57b562",
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
	return zip(tickers[:5],name[:5])


nasdaq=make_request("NASDAQ")
nyse = make_request("NYSE")

def download_exchange_data(data):
	all_tickers = process_response(data)
	# all_tickers = all_tickers[:10]
	final_data = pd.DataFrame()
	for at,name in all_tickers:
		# print(at,type(at))
		time.sleep(3)
		ticker_object= yf.Ticker(at)
		data=ticker_object.history(period="max",interval="1d")
		data= data.reset_index()
		data['ticker']=at
		data['name']=name
		final_data = pd.concat([final_data, data])
	return final_data
#
download_exchange_data(nasdaq).to_csv("Nasdaq_stocks.csv",index=False)
download_exchange_data(nyse).to_csv("nyse_stocks.csv",index=False)

print ("Files saved to project folder")

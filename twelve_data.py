import requests

class RequestStocks:
	'''
	Needs an API key
	'''
	def __init__(self, api_key):
		self.api_key = api_key

	'''
	Makes request which returns a json file
	'''
	def make_request(self, exchange):
		url = "https://twelve-data1.p.rapidapi.com/stocks"
		querystring = {f"exchange":{exchange},"format":"json"}
		headers = {
			"X-RapidAPI-Key": self.api_key,
			"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers, params=querystring)
		return response.json()

	'''
	process the json to get ticker and company name
	download_exchange_data
	'''

	def process_response(self, response):
		tickers = []
		names = []
		for k, v in response.items():
			if k == "data":
				data = v
				for d in data:
					tickers.append(d["symbol"].lower())
					names.append(d["name"])
		return list(zip(tickers[:10], names[:10]))

	'''
	process the json to get ticker only
	used to get data in bulk
	download_exchange_data_multi
	'''
	def process_response2(self,response):
		tickers=[]
		name=[]
		for k,v in response.items():
			if k=="data":
				data=v
				for d in data:
					tickers.append(d["symbol"])
		return tickers

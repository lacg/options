import pandas as pd
import numpy as np
import requests, json
from bs4 import BeautifulSoup

class Stock():

	def __init__(self, symbol: str = "AAPL") -> None:
		self.session = requests.Session()
		self.symbol = symbol # Change to the stock symbol you want to analyze

	@property
	def calls(self):
		return self._calls

	@calls.setter
	def calls(self, value):
		self._calls = value
		self.filteredCalls = self._filterChain(value)

	@property
	def lastPrice(self):
		return self.quote["regularMarketPrice"]

	@property
	def puts(self):
		return self._puts

	@puts.setter
	def puts(self, value):
		self._puts = value
		self.filteredPuts = self._filterChain(value)

	@property
	def session(self):
		return self._session

	@session.setter
	def session(self, value):
		self._session = value
		self._session.headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36" }

	@property
	def symbol(self):
		return self._symbol

	@symbol.setter
	def symbol(self, value):
		self._symbol = value

		self._update()

	@property
	def url(self):
		return f'https://query1.finance.yahoo.com/v7/finance/options/{self.symbol}'

	def _filterChain(self, chain, threshold = 0.1):
		return [ link for link in chain if (self.lastPrice * (1.0 - threshold) < link["strike"] < self.lastPrice * (1.0 + threshold)) and (link["bid"]) and (link["ask"]) and (link["ask"] - link["bid"] < threshold) ]

	def _update(self):
		self.response = json.loads(self.session.get(self.url).text)["optionChain"]["result"][0]
		self.quote = self.response["quote"]
		self.calls = self.response["options"][0]["calls"]
		self.puts = self.response["options"][0]["puts"]

		""" self.options['Strike'] = self.options['Strike'].apply(lambda x: float(x))
		self.options['Bid'] = self.options['Bid'].apply(lambda x: float(x))
		self.options['Ask'] = self.options['Ask'].apply(lambda x: float(x))
		self.options['Implied Volatility'] = self.options['Implied Volatility'].apply(lambda x: float(x.strip('%')) / 100)
		self.options = self.options[self.options['Strike'] > self.options['Last Price'] * 0.9]
		self.options = self.options[self.options['Strike'] < self.options['Last Price'] * 1.1]
		self.options = self.options[self.options['Bid'] != 0]
		self.options = self.options[self.options['Ask'] != 0]
		self.options = self.options[self.options['Ask'] - self.options['Bid'] < 0.1]
		print("Passei por aqui") """

	def show(self):
		print(self.filteredCalls)
		print(self.filteredPuts)
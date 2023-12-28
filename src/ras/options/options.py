import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

class Options():

	def __init__(self, symbol: str = "AAPL") -> None:
		self.symbol = symbol # Change to the stock symbol you want to analyze

	@property
	def symbol(self):
		return self._symbol

	def symbol(self, value):
		self._symbol = value

		self._update()

	@property
	def url(self):
		return f'https://finance.yahoo.com/quote/{symbol}/options?p={symbol}'

	def _update(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		table = soup.find_all('table')[0]
		self.options = pd.read_html(str(table))[0]

		self.options['Strike'] = self.options['Strike'].apply(lambda x: float(x))
		self.options['Bid'] = self.options['Bid'].apply(lambda x: float(x))
		self.options['Ask'] = self.options['Ask'].apply(lambda x: float(x))
		self.options['Implied Volatility'] = self.options['Implied Volatility'].apply(lambda x: float(x.strip('%')) / 100)
		self.options = self.options[self.options['Strike'] > self.options['Last Price'] * 0.9]
		self.options = self.options[self.options['Strike'] < self.options['Last Price'] * 1.1]
		self.options = self.options[self.options['Bid'] != 0]
		self.options = self.options[self.options['Ask'] != 0]
		self.options = self.options[self.options['Ask'] - self.options['Bid'] < 0.1]

	def show(self):
		print(self.options)
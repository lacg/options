"""Controlling a rigidbody quadcopter using Control Theory and Reinforcement Learning"""

from ras.stocks.stocks import Stock

def stock(symbol: str = "AAPL") -> None:
	Stock().show(symbol)

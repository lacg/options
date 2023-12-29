"""Printing option stock."""

import argparse

from ras.stocks.stocks import Stock

def main():
	args = parse_arguments()
	print(f"Symbol: {args.symbol}\nOption Type: {args.optionType}\n")
	Stock(args.symbol).show(args.optionType)
	# Process the parameters as needed

def parse_arguments():
	parser = argparse.ArgumentParser(description='Stock options')
	parser.add_argument('symbol', help='Stock symbol. Default AAPL.', default="AAPL")
	parser.add_argument('-o', "--optionType", help='Option type to print.', default="Call")
	return parser.parse_args()

if __name__ == '__main__':
	main()
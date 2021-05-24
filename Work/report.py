# report.py
#
# Exercise 2.4
# Exercise 2.5
# Exercise 2.6


import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #holding = (row[0], int(row[1]), float(row[2]))
            info = {
	            'name': row[0],
	            'shares': int(row[1]),
	            'price': float(row[2]),
	    }
            portfolio.append(info)
            
    return portfolio

def read_prices(filename):
    
    stock_price = {}

    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            
            stock_price[row[0]] = float(row[1]),
            
        except IndexError:
            print("Index Error")
            pass

    return stock_price

# report.py
#
# Exercise 2.4
# Exercise 2.5
# Exercise 2.6


import csv
from pprint import pprint

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

# Exercise 2.7
def main():
   portfolio = read_portfolio('Data/portfolio.csv')
   prices = read_prices('Data/prices.csv')

   current_portfolio = {}
   
   for n in range(len(portfolio)):
       name = portfolio[n]['name']
       shares = int(portfolio[n]['shares'])
       price = float(portfolio[n]['price'])
       
       current_value = shares * float(prices[name][0]) 
       
       if price <= float(prices[name][0]):
          status = 'Gain'
       else:
          status = 'Loss'

       current_portfolio[name] = [current_value,status] 

   pprint(current_portfolio)
   

if __name__ == "__main__":
    main()

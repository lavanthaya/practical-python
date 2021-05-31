# report.py
#
# Exercise 2.4
# Exercise 2.5
# Exercise 2.6
# Exercise 2.16

import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            #holding = (row[0], int(row[1]), float(row[2]))
            #info = {
	    #        'name': row[0],
	    #        'shares': int(row[1]),
	    #        'price': float(row[2]),
	    #}
            portfolio.append(record)
            
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

#Exercise 3.1
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- -----------')
    for r in report:
        print('%10s %10d %10s %10.2f' % r)
    
    return 0

#Exercise 2.9
def make_report(portfolio, prices):
   
   report = []

   for n in range(len(portfolio)):
       name = portfolio[n]['name']
       shares = int(portfolio[n]['shares'])
       price_old = float(portfolio[n]['price'])
       price_current = float(prices[name][0])
       change =  price_current - price_old

       report.append((name,shares,'${:.2f}'.format(price_current),change))
      
   print_report(report)   

   return 0


# Exercise 2.7
# Exercise 2.11
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
   print("Printing report")
   make_report(portfolio, prices)

if __name__ == "__main__":
    main()

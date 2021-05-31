# report.py
#
# Exercise 2.4
# Exercise 2.5
# Exercise 2.6
# Exercise 2.16

import csv
from pprint import pprint
import fileparse

def read_portfolio(filename):
            
    return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):

    return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

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

# Exercise 3.2
def portfolio_report(portfolio,prices):
   portfolio = read_portfolio(portfolio)
   prices = read_prices(prices)
    
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
    

# Exercise 2.7
# Exercise 2.11
def main():
   
   portfolio_report('Data/portfolio.csv', 'Data/prices.csv') 


if __name__ == "__main__":
    main()

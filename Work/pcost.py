# pcost.py
#
# Exercise 1.27
# Exercise 1.30
# Exercise 1.31
# Exercise 1.32
# Exercise 1.33
# Exercise 2.15
# Exercise 2.16

import csv
import sys
import report

def portfolio_cost(filename):
    try:
      tot_cost = 0

      portfolio = report.read_portfolio(filename)
      
      return sum([s['shares']*s['price'] for s in portfolio])

    except ValueError:
      print("Missing Data, clean the file")
      print(f'Row {rowno}: Bad row: {line}')

if len(sys.argv) == 2:
   filename = sys.argv[1]
else:
   filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
#print(f'Total cost {cost:0.2f}')

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)


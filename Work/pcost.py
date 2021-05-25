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

def portfolio_cost(filename):
    try:
      tot_cost = 0

      f = open(filename)
      rows = csv.reader(f)
      headers = next(rows)

      for rowno, line in enumerate(rows, start=1):
          record = dict(zip(headers, line))
          #row = line.split(',')
          #tot_cost += (float(row[2])*float(row[1]))
          nshares = int(record['shares'])
          price = float(record['price'])
          #tot_cost += (float(line[2])*float(line[1]))
          tot_cost += nshares * price

      f.close()
      return tot_cost

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


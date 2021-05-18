# pcost.py
#
# Exercise 1.27
# Exercise 1.30
# Exercise 1.31
# Exercise 1.32

import csv

def portfolio_cost(filename):
    try:
      tot_cost = 0

      f = open(filename)
      rows = csv.reader(f)
      next(rows)

      for line in rows:
          #row = line.split(',')
          #tot_cost += (float(row[2])*float(row[1]))
          tot_cost += (float(line[2])*float(line[1]))

      f.close()
      return tot_cost

    except ValueError:
      print("Missing Data, clean the file")

cost = portfolio_cost("Data/portfolio.csv")
print('Total cost:', cost)
#print(f'Total cost {cost:0.2f}')

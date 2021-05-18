# pcost.py
#
# Exercise 1.27

tot_cost = 0

f = open('Data/portfolio.csv', 'rt')
next(f).split(',')

for line in f:
    row = line.split(',')
    #print(row[2])
    tot_cost += (float(row[2])*float(row[1])) 

f.close()

print(f'Total cost {tot_cost:0.2f}')

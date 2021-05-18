# pcost.py
#
# Exercise 1.27
# Exercise 1.30


def portfolio_cost(filename):
    tot_cost = 0

    f = open(filename, 'rt')
    next(f).split(',')

    for line in f:
        row = line.split(',')
        #print(row[2])
        tot_cost += (float(row[2])*float(row[1])) 

    f.close()
    return tot_cost

cost = portfolio_cost("Data/portfolio.csv")
print('Total cost:', cost)
#print(f'Total cost {cost:0.2f}')

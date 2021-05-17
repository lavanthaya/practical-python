# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month +=1
    if month <=12:
       payment = 2684.11 + 1000.00
    else:
       payment = 2684.11
    
    #print(month,payment)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment


print('Total paid', round(total_paid,2))
print('Total month', month)


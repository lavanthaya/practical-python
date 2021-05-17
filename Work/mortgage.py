# mortgage.py
#
# Exercise 1.7
# Exercise 1.8
# Exercise 1.9
# Exercise 1.10
# Exercise 1.11
# Exercise 1.17

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month +=1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
       payment = 2684.11 + 1000.00
    else:
       payment = 2684.11
    
    if (principal * (1 + rate/12)) <= payment:
       payment = principal * (1+rate/12)
 
    #print(month,payment)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    #print (month, round(total_paid,2), round(principal,2))
    print (f'{month} ${total_paid:0.2f} ${principal:0.2f}')	# Exercise 1.17

print('Total paid', round(total_paid,2))
print('Total month', month)


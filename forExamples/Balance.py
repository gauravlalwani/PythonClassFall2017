balance = 1000
interest = 0.06
for i in range(30):
    balance = balance * (1+interest)
    print('The balance for this year is $' + str(balance))

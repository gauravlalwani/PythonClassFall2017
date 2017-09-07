balance = 500
amount = int(input('How much do you want to withdraw? '))
remAmount = amount % 10
if (amount<=balance) and (remAmount==0):
    print('Your money is available below.')
    newBalance = balance - amount
    print('The new balance is ' + str(newBalance) + '.')
else:
    print('Invalid entry!')

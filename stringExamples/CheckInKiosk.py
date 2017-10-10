print('Please enter your last name, membership number, or record locator.')
userInput = input()

if userInput.isalpha():
    print('Your last name is ' + userInput.upper())
elif userInput.isdecimal():
    print('Your membership number is ' + userInput)
elif userInput.isalnum():
    print('Your record locator is ' + userInput.upper())
else:
    print('Invalid entry')

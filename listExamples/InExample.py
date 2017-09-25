nameList = ['Sarah', 'Paul', 'Jill', 'Robert']
print('What is your name?')
name = input()
while name not in nameList:
    print('Your name is not on the list.')
    print('What is your name again?')
    name = input()

print('Welcome to the party, ' + name + '!')

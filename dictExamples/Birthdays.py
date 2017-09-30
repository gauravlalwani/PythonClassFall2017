# The initial birthday list
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()

    # if blank, then exit the while loop
    if name == '':
        break

    # if a name on the birthday list is entered
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    # if a new name is entered
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

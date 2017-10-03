passwords = ['aaargh', 'fjfjkdg', 'qwerty']
userPW = input('Please enter the password: ')
while userPW not in passwords:
    print('Incorrect password!!!')
    userPW = input('Please enter the password: ')

print('Access granted!')

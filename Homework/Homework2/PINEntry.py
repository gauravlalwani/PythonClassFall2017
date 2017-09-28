PIN = '2468'
nTry = 1
maxTry = 5
while nTry<=maxTry:
    userPIN = input('Please enter the PIN ')
    if userPIN == PIN:
        print('Access granted!')
        break
    elif nTry<maxTry:
        print('Incorrect PIN!')
    else:
        print('Too many attempts. Further attemps denied!')
    nTry = nTry + 1
    

import random

def compareNum(a,b):
    if a<b:
        print('Too high')
    if a>b:
        print('Too low')

# the number to be guessed
target = random.randint(1,10)
while True:
    guess = int(input('Guess the number: '))
    if target==guess:
        print('You got it!')
        break
    else:
        compareNum(target, guess)

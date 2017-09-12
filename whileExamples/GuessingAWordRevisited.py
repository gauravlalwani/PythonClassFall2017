# secret word
secretWord = 'spaghetti'

while True:
    # ask user to enter a word
    word = input('What is the secret word? ')
    
    if word==secretWord:
        break
    else:
        print('Wrong word! Try again!')

# correct word was guessed
print('You guessed it correctly!')

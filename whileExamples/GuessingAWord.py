# secret word
secretWord = 'spaghetti'

# ask user to enter a word
word = input('What is the secret word? ')
while word!=secretWord:
    print('Wrong word! Try again!')

    # ask user to enter a word
    word = input('What is the secret word? ')

# correct word was guessed
print('You guessed it correctly!')

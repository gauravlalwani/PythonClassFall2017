import random

def HiddenWord(word):
    for i in range(len(word)):
        for j in range(len(word)):
            if i==j:
                print(word[i], end='')
            else:
                print(random.randint(0,9), end='')
        print()


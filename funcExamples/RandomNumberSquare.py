import random

def randSQ(sizeSQ):
    for iRow in range(sizeSQ):
        for iCol in range(sizeSQ):
            print(str(random.randint(0,9)), end='')
        print()


def printAnswer():
    global Answer
    Answer = 38
    print('Variable Answer inside the function is ' + str(Answer))

Answer = 42
print('Variable Answer is ' + str(Answer))
printAnswer()
print('Variable Answer is ' + str(Answer))


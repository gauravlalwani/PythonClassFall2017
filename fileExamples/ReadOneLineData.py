import os

# reading the line from the data file
f = open(os.path.join('TestData','ExerciseData_OneLine.txt'),'r')
line = f.readline()
f.close()

# converting into a numerical list
inString = line.strip().split()
inNumber = [int(i) for i in inString]

# putting numbers in appropriate lists
trial = inNumber[:3]
onsetTime = inNumber[3:6]
respTime = inNumber[6:9]
score = inNumber[9:12]


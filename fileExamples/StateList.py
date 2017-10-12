import os

# reading the line from the data file
f = open(os.path.join('TestData','StateList.txt'),'r')
line = f.readline()
f.close()

# making a list of states
stateList = line.split(',')

# printing the list
for iState in stateList:
    print(iState)


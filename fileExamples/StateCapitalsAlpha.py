import os

# reading the data
f = open(os.path.join('TestData','StateCapitalList.txt'), 'r')
fileData = f.read()
f.close()

# split into lines
lines = fileData.strip().split('\n')

# putting them in lists
state = []
capital = []
for iState in lines:
    items = iState.split(',')
    state.append(items[0])
    capital.append(items[1])

# writing the state capitals, alphabetical
f = open('StateCapitalAlpha.txt','w')
capital.sort()
for iCap in capital:
    f.write(iCap + '\n')
f.close()

    

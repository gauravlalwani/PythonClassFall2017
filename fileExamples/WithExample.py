stateList = []
capitalList = []
with open('TestData/StateCapitalList.txt','r') as infile:
    for line in infile:
        state, capital = line.strip().split(',')
        stateList.append(state)
        capitalList.append(capital)
        print('State: ' + '%-15s' % state + '\tCapital: ' + capital)

with open('TestData/FormatStateList.txt','w') as outfile:
    for i, state in enumerate(stateList):
        outfile.write('State: ' + '%-15s' % state + '\tCapital: ' + capitalList[i])
        outfile.write('\n')



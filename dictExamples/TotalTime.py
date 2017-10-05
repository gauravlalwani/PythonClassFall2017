washer = {'soak':10, 'wash':20, 'rinse':12, 'spin':6}

totalTime = 0
for iCycle in washer.values():
    totalTime += iCycle

print('Total required time: ' + str(totalTime) + 'min')

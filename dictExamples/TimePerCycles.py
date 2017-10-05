washer = {'soak':10, 'wash':20, 'rinse':12, 'spin':6}

print('List of cycles:')
for iCycle, iMin in washer.items():
    print(iCycle + ': ' + str(iMin) + 'min')

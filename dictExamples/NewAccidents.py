numAccident = {'A':5, 'C':2, 'D':1, 'F':2, 'H':1}
newAccidents = ['A', 'H', 'H', 'D', 'K', 'J']

for iCar in 'ABCDEFGHIJK':
    numAccident.setdefault(iCar,0)

for iNew in newAccidents:
    numAccident[iNew] += 1




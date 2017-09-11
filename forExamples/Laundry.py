qStart = 40  # You start from a roll of quarters ($10)
qStep = -7  # it costs you 7 quarters to run a wash & dry cycle
qStop = -1  # you have to stop after you run out of quarters
for iCoin in range(qStart, qStop, qStep):
    print('You have ' + str(iCoin) + ' quarters.')


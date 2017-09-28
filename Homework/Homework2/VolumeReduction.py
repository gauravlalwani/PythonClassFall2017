initVol = 100
volume = initVol
redRate = 0.05
duration = 30
halfLife = 0
for iDay in range(1,duration+1):
    volume = volume * (1-redRate)
    print('*' * int(volume // 5))
    if (halfLife == 0) and (volume< 0.5*initVol):
        halfLife = iDay

print('The half-life is ' + str(halfLife) + ' days')

# Iniital charge
battery = 16
minutes = 0

# charging 3 percent every 10 minutes
while True:
    if battery >= 100:
        break
    print('Time: ' + str(minutes) + 'min   Charge: ' + str(battery) + 'percent')
    battery = battery + 3
    minutes = minutes + 10

# fully charged
print(str(minutes) + 'min, and the battery is fully charged')

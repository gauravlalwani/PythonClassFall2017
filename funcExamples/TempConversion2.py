def FtoC(tempF):
    tempC = (tempF - 32) * (5/9)
    return tempC, tempF

C, F = FtoC(90)
print(str(F) + ' degree Fahrenheit = ' + str(C) + ' degree Celsius')

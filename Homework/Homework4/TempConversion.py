# opening input file
f = open('BodyTempData.txt','r')
# opening output file
g = open('BodyTempDataC.txt','w')

# loop over lines of the input file
line = f.readline()
while line:
    # extracting the ID and the temperature
    ID, x = line.strip().split()
    tempF = float(x)
    # converting F to C
    tempC = (tempF-32) * 5/9
    # Treatment groups -- determined by the 2nd digit of the ID
    if ID[1] == '0':
        tx = 1
    elif ID[1] == '1':
        tx = 2
    else:
        tx = 3
    # writing out to the output file
    g.write('  ' + ID + '%6.1f' % tempC + '  ' + str(tx) + '\n')
    # reading in the next line
    line = f.readline()

# closing both files
f.close()
g.close()

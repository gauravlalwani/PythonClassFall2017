# first, open the file
f = open('TestData/SingleLineData.txt', 'r')
# read a line, then put in a variable called line
line = f.readline()
# always close the file you opened
f.close()


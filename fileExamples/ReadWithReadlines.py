# first, open the file
f = open('TestData/MultiLineData.txt', 'r')
# read the file into a list called fileData.
fileData = f.readlines()
# always close the file you opened
f.close()

# first, open the file
f = open('TestData/MultiLineData.txt', 'r')
# read the entire file content into a string variable fileData
fileData = f.read()
# always close the file you opened
f.close()

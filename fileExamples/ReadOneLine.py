import os

# changing the working directory to the appropriate directory
WorkDir = 'TestData'  #this needs to be customized
os.chdir(WorkDir)

# first, open the file
f = open('SingleLineData.txt', 'r')
# read a line, then put in a variable called line
line = f.readline()
# always close the file you opened
f.close()


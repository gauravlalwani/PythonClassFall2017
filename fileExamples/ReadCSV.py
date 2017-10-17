import csv
import os

f = open(os.path.join('TestData','StudySubjects.csv'),'r')
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()

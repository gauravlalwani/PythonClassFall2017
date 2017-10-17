import csv
import os

f = open(os.path.join('TestData','StudySubjects.csv'),'r')
reader = csv.DictReader(f)
for row in reader:
    print(row)

f.close()

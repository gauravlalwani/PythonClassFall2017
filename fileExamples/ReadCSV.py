import csv

f = open('TestData/StudySubjects.csv')
reader = csv.reader(f)
for row in reader:
    print(row)

f.close()

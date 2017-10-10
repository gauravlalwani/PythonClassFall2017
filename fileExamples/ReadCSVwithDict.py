import csv

f = open('TestData/StudySubjects.csv')
reader = csv.DictReader(f)
for row in reader:
    print(row)

f.close()

import csv
import random

f = open('RandomData.csv','w')
writer = csv.writer(f)
writer.writerow(['ID', 'Rand1', 'Rand2'])
for i in range(1,11):
    writer.writerow(['%04d' % i, random.randint(0,10), random.randint(10,20)])

f.close()

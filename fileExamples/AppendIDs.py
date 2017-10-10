f = open('IDs.txt','a')
for i in range(110,126):
    f.write('%05d' % i + '\n')
    
f.close()


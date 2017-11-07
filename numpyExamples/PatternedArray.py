import numpy as np

a = np.ones([5,5])
for i in range(1,5):
    a[i:,i:] = i+1

print(a)

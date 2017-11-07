import numpy as np

g = np.array([[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]])

# Broadcasting 1
h = np.array([[2], [5], [10]])
print(g*h)

# Broadcasting 2
f = np.array([5,2,1,1,1])
print(g*f)

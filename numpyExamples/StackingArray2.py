import numpy as np
matI = np.eye(3)
v = np.array([-33, 44, 35])
print(np.vstack((matI,v)).T)

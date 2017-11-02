import numpy as np

x = np.random.randn(1000,20)
print(x.mean(axis=0))
print(x.std(axis=0))

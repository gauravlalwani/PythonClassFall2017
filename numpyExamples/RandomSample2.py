import numpy as np

x = np.random.randn(1000,20)
y = np.random.randn(1000,20)
z = x + y
print(z.mean(axis=0))
print(z.std(axis=0))

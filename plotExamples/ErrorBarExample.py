import matplotlib.pyplot as plt
import numpy as np

xData = np.array([10, 20, 30, 40])
yData = np.array([41.2, 35.1, 29.5, 22.9])
errData = np.array([3.4, 3.8, 3.3, 3.9])


# plotting the data and error bars separately
plt.plot(xData, yData, 'r-')
plt.errorbar(xData, yData, yerr=errData, fmt='none', ecolor='r')
plt.axis([8,42,15,50])
plt.show()

             

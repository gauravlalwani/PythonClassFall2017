import matplotlib.pyplot as plt
import numpy as np

meanData = np.array([41.2, 35.1, 29.5, 22.9, 43.4, 39.8, 36.6, 32.9])
x = np.array([10,20,30,40,10,20,30,40])
sdData = np.array([3.4, 3.8, 3.3, 3.9, 4.0, 3.2, 3.4, 3.5])
cond = np.array([1,1,1,1,2,2,2,2])


# plotting the data and error bars separately
plt.plot(x[cond==1], meanData[cond==1], 'r-', label='Condition 1')
plt.errorbar(x[cond==1], meanData[cond==1],
             yerr=sdData[cond==1], fmt='none', ecolor='r')
plt.plot(x[cond==2], meanData[cond==2], 'b-', label='Condition 2')
plt.errorbar(x[cond==2], meanData[cond==2],
             yerr=sdData[cond==2], fmt='none', ecolor='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([8,42,15,50])
plt.legend()
plt.show()

             

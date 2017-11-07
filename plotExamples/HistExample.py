import numpy as np
import matplotlib.pyplot as plt

# generating a set of random numbers
randData = 500 + 125*np.random.randn(10000)

# simple histogram
plt.hist(randData)
plt.show()


# changing the number of bins
plt.figure(figsize=[8,3])

plt.subplot(131)
plt.hist(randData,20)
plt.title('20 bins')

plt.subplot(132)
plt.hist(randData,50)
plt.title('50 bins')

plt.subplot(133)
plt.hist(randData,100)
plt.title('100 bins')

plt.subplots_adjust(bottom=0.1, wspace=0.35, left=0.075, right=0.95)
plt.savefig('HistExample.png', dpi=300)
plt.show()


# adding labels
plt.hist(randData,50)
plt.title('Histogram with 50 bins')
plt.xlabel('Random number')
plt.ylabel('Frequency count')
plt.savefig('Hist50bins.png', dpi=300)
plt.show()

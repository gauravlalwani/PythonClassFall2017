import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
meanCong = np.array([33, 44, 52, 48])
sdCong = np.array([8, 9.1, 10.1, 8.8])
meanIncong = np.array([28, 48, 51.3, 46.5])
sdIncong = np.array([7.2, 9.2, 9.6, 8.4])
meanMixed = np.array([31.3, 40.8, 47.8, 47.2])
sdMixed = np.array([7.8, 8.3, 9.1, 7.8])


# paramters
bar_width = 0.2
x = np.arange(len(meanCong))

# plotting bars
plt.bar(x, meanCong, bar_width, yerr=sdCong,
        color='g', ecolor='g', label='Congruent')
plt.bar(x+bar_width, meanIncong, bar_width, yerr=sdIncong,
        color='m', ecolor='m', label='Incongruent')
plt.bar(x+2*bar_width, meanMixed, bar_width, yerr=sdMixed,
        color='c', ecolor='c', label='Mixed')

# formatting and labeling the axes and title
plt.xlabel('Task')
plt.ylabel('Scores')
plt.title('Scores by tasks')

# formatting the x tick marks
plt.xticks(x+1.5*bar_width, ['Task 1', 'Task 2', 'Task 3', 'Task 4'])

# axis limits
plt.axis([-0.2, 3.8, 0, 70])

# legend
plt.legend(loc=2)

# and we are done!
plt.show()

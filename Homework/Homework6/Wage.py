import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading the data
wageData = pd.read_csv('EduWage.csv')

# generating a variable for education category
# 0: Not finished high school (Education<12)
# 1: Completed high school (Education==12)
# 2: Some college (12<Education<16)
# 3: Completed college (Education==16)
# 4: Post-graduate (Education>16)
#
wageData['EduCat'] = np.zeros(len(wageData.Education))
wageData.loc[wageData.Education==12, 'EduCat'] = 1
wageData.loc[(12<wageData.Education) & (wageData.Education<16), 'EduCat'] = 2
wageData.loc[wageData.Education==16, 'EduCat'] = 3
wageData.loc[wageData.Education>16, 'EduCat'] = 4
groupNames = ['< high school',
              'Completed\nhigh school',
              'Some college',
              'Completed\ncollege',
              'Post-graduate']

# plotting bar graph
bar_width = 0.4
x = np.arange(5)
plt.bar(x, wageData[wageData.Sex==0].groupby('EduCat').Wage.mean(),
        bar_width,
        yerr=wageData[wageData.Sex==0].groupby('EduCat').Wage.std(),
        color='c',ecolor='c',label='Males')
plt.bar(x+bar_width, wageData[wageData.Sex==1].groupby('EduCat').Wage.mean(),
        bar_width,
        yerr=wageData[wageData.Sex==1].groupby('EduCat').Wage.std(),
        color='m',ecolor='m',label='Females')

# formatting and labeling the axes and title
plt.xlabel('Education level')
plt.ylabel('Mean hourly wage')
plt.title('Hourly wage by gender and education levels')
plt.xticks(x+bar_width, groupNames)
plt.axis([-0.3,5.1, 0, 22])

# adding the legend
plt.legend(loc=2)

# saving the figure
plt.savefig('WageGraph.png', dpi=300)

plt.show()


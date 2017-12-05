import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# loading the data
fevData = pd.read_csv('fev.csv')

# plotting the graph
plt.plot(fevData.age[fevData.smoke==0], fevData.fev[fevData.smoke==0],
     'bo', label='Non-smokers')
plt.plot(fevData.age[fevData.smoke==1], fevData.fev[fevData.smoke==1],
     'rs', label='Smokers')

# plot title
plt.title('FEV by age')

# adding axis labels
plt.xlabel('Age')
plt.ylabel('FEV')

# adding the legend
plt.legend(loc=2)

# saving the figure
plt.savefig('FEVgraph.png', dpi=300)

plt.show()


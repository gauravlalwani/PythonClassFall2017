import numpy as np
import pandas as pd

# loading the county-level census data
ctyData = pd.read_csv('co-est2016-alldata.csv',
                      encoding = 'iso-8859-1')

# grouping by divisions
divData = ctyData.groupby('DIVISION')

# calculating the total population by division
print(divData.sum().CENSUS2010POP)

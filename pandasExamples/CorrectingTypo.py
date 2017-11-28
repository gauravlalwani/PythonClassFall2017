import numpy as np
import pandas as pd

bodyData = pd.read_csv('BodyFat.csv', index_col=0)
bodyData.drop('Unnamed: 17', axis=1, inplace=True)

bodyData.loc[bodyData.HEIGHT==29.5, 'HEIGHT'] = 69.5

bodyData.to_csv('BodyFatCorrected.csv')




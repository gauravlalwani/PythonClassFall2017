import numpy as np
import pandas as pd

bodyData = pd.read_csv('BodyFatCorrected.csv')
heightM = pd.read_csv('HeightM.csv', index_col=0)
weightKG = pd.read_csv('WeightKG.csv', index_col=0)

newData = pd.merge(bodyData,heightM,on='IDNO')
newnewData = pd.merge(newData,weightKG,on='IDNO')





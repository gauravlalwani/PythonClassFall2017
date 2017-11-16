import numpy as np

# function to calculate the truncated mean
def truncMean(inData):
    # make a copy of the original array to work with
    workData = np.copy(inData)
    workData.sort()
    tMean = workData[1:-1].mean()
    return tMean


# score array
scores = np.array([
    [8, 7, 6, 7, 10, 9, 9, 8],
    [5, 8, 7, 8, 9, 6, 8, 8],
    [9, 8, 9, 9, 7, 8, 10, 10],
    [6, 7, 7, 6, 10, 5, 6, 7],
    [8, 7, 7, 3, 7, 7, 8, 6]])

# calculating trucated means for each athlete
for iRow in scores:
    print('Truncated mean:  %5.2f' % truncMean(iRow))


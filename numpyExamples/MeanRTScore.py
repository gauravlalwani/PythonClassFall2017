import numpy as np

RTMat = np.array([[111, 100,  86, 120,  91],
                  [ 92,  83, 105, 103, 112],
                  [117, 121, 124, 111, 110],
                  [111,  86, 113,  88, 105]])
scoreMat = np.array([[1, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1],
                     [0, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0]])

# Mean RT
print('Mean RT for score==0: ' + '%6.1f' % RTMat[scoreMat==0].mean())
print('Mean RT for score==1: ' + '%6.1f' % RTMat[scoreMat==1].mean())

# Mean score
print('Mean score for RT>100: ' + '%4.1f' % scoreMat[RTMat>100].mean())
print('Mean score for RT<=100: ' + '%4.1f' % scoreMat[RTMat<=100].mean())

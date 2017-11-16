import numpy as np

# data arrays
survTime = np.array([
        285,  131,  180,  596,  109,   17,  841, 1799,   39, 1141,   45,
        941, 1571,   16,   39,  915,    5,   51,   58,  334,  165, 1032,
        340,  852, 1321,   68,  979,  482,  110,  265,  630,  670,   72,
        153,  188,  342,  397,  515, 1407, 1586,  100,  285,  583,  995,
         68,  308,   53,  675,   78,  207,  219,  445,  545,   30,   61,
        186,   72,   80,   96, 1386,  370,   16,   81,   28,   43,   90,
        733,   66,   77])
age = np.array([
       19, 23, 26, 26, 28, 29, 32, 33, 35, 36, 36, 38, 40, 40, 40, 41, 41,
       42, 42, 42, 43, 43, 44, 44, 45, 45, 45, 46, 46, 47, 47, 47, 47, 47,
       47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 50, 50, 51, 51, 51,
       52, 52, 52, 52, 52, 53, 53, 53, 53, 54, 54, 54, 55, 56, 56, 58, 61,
       64])

#### All patients
print("All patients:")
nTotal = len(survTime)
for year in range(1,4):
    survProb = len(survTime[survTime>year*365])/nTotal
    print(str(year) + "-year survival probability: %5.3f" % survProb)



#### younger than 50
print("\nPatients younger than 50:")
# creating sub arrays of the original survival data for age<50
survTime49 = survTime[age<50]
# then calculate survival probabilities
nTotal49 = len(survTime49)
for year in range(1,4):
    survProb49 = len(survTime49[survTime49>year*365])/nTotal49
    print(str(year) + "-year survival probability: %5.3f" % survProb49)

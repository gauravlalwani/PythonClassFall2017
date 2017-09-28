def RepNumbers(inList):
    outList = []
    for i in inList:
        tempList = [i] * i
        outList = outList + tempList
    return outList

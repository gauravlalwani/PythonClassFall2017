def DoubleReverse(inList):
    outList = []
    for iWord in inList[::-1]:
        outList.append(iWord[::-1])
    return outList


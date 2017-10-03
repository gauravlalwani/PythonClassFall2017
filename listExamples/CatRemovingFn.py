import copy

def RemoveCat(inList):
    outList = copy.copy(inList)
    while 'cat' in outList:
        outList.remove('cat')
    return outList


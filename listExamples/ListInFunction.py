def append_item(origList):
    newList = origList
    newList.append('New item')
    return newList

aList = ['apple', 'banana', 'cat']
bList = append_item(aList)
print(aList)
print(bList)


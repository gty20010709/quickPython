def printPrice(itemDict:dict,leftWidth,rightWidth):
    print('Price Items'.center(leftWidth + rightWidth,'-'))
    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'-'),str(v).rjust(rightWidth,'-'))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPrice(picnicItems,12,5)
printPrice(picnicItems,20,6)


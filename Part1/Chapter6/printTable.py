tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def findLonggest(tableData):
    long = 0
    for x in tableData:
        for i in x:
            if len(i) > long:
                long = len(i)
    return long

def printTable(tableData,width):
    for row in tableData:
        for line in row:
            print(line.rjust(width),end='')
        print()
# print(findLonggest(tableData))

width = findLonggest(tableData)
printTable(tableData,width)

theBoard = {
        'top-L':' ','top-M':' ','top-R':' ',
        'mid-L':' ','mid-M':' ','mid-R':' ',
        'low-L':' ','low-M':' ','low-R':' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

flag = 0
print('In the game, just input a postion')
print(theBoard.keys())
while True:
    if flag % 2 == 0:
        ipt = input("First Player\(O\), now it's your turn:")
        Player = 'O'
    elif flag % 2 == 1:
        ipt = input("Second Player \(X\), now it's your turn:")
        Player = 'X'
    else:
        pass
    theBoard[ipt] = Player
    print(theBoard)
    flag += 1



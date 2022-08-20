
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter


def spaceFree(pos):
    return board[pos] == ' '


def printBoard(board):
    vertical_lines = '   |   |  '
    horizontal_lines = '-----------'
    print(vertical_lines)
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(vertical_lines)
    print(horizontal_lines)
    print(vertical_lines)
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(vertical_lines)
    print(horizontal_lines)
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(vertical_lines)
    print(vertical_lines)


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playerMove(board):
    run = True
    while run:
        move = input("Enter your position to place an X (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This space is taken')
            else:
                print('Error, type in a number between 1-9: ')
        except:
            print('Please type a digit between 1-9: ')


def compMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x !=0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move
  

def selectRandom(li):
    import random

    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le ) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
    

def main():
    print('Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove(board)
            printBoard(board)
        else:
            print('O\'s have won!')
            break

        if not(isWinner(board, 'X')):
            move = compMove(board)
            if move == 0:
                print('Tie game!')
            else:
                insertLetter('O', move)
                print('Computer placed an O in position', move , ':')
                printBoard(board)
        else:
            print('X\'s have won!')
            break

    if isBoardFull(board):
        print('Draw!')

while True:
    input('Press Enter to play')
    main()

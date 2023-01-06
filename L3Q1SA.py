#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L3Q1SA.py
#  
#  Purpose:   This program will determine if a given chess move is valid or not
#   given the moved piece relative to its position on the board
#  ----------------------------------------------------

#Purpose: The purpose of this function is to check if the new position differs from the current
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkMoved(currentPos,nextPos):
    if currentPos != nextPos:
        valid = True
    else: 
        valid = False
    return valid

#Purpose: The purpose of this function is to check if the new position is within the bounds of the board
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkBounds(nextPos):
    boardY = '1 2 3 4 5 6 7 8'.split() 
    boardX = 'A B C D E F G H'.split()
    valid = ''
    listt = []
    y = 0
    for x in (nextPos):
        listt.append(x.upper())
    for i in (listt):
        if i in boardX or i in boardY:
            y = y + 1
    if y == 2:
        valid = True
    else:
        valid = False
    return valid

#Purpose: The purpose of this function is to check if the attempted move by the Rook is valid
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkRookMove(currentPos,nextPos):
    
    boardX = 'A B C D E F G H'.split()
    BoardY = '1 2 3 4 5 6 7 8'.split()
    letterlistt = []
    for letter in boardX:
        boardnums = [(letter + str(x)) for x in range(1,9)]
        letterlistt.append(boardnums)
    movelist = []
    a,b = currentPos[0],currentPos[1]
    if (b) in BoardY:
        index = BoardY.index(b)
        for x in range(8):
            movelist.append(letterlistt[x][index])
    if a in boardX:
        index = boardX.index(a)
    for x in range(8):
        movelist.append((letterlistt[index][x]))
    if b in boardX:
        index = boardX.index(b)
    for x in range(8):
        movelist.append((letterlistt[x][index]))
    if nextPos in movelist:
        valid = True
    else:
        valid = False
    return valid
        
#Purpose: The purpose of this function is to check if the attempted move by the bishop is valid.
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkBishopMove(currentPos,nextPos):
    
    boardX = 'A B C D E F G H'.split()
    letterlistt = []
    for letter in boardX:
        boardnums = [(letter + str(x)) for x in range(1,9)]
        letterlistt.append(boardnums)
    movelist = []
    a,b = currentPos[0],currentPos[1]
    boardX = 'A B C D E F G H'.split()
    letterlistt = []
    for letter in boardX:
        boardnums = [(letter + str(x)) for x in range(1,9)]
        letterlistt.append(boardnums)
    movelist = []
    a,b = currentPos[0],currentPos[1]
    
    if a in boardX:
        index = boardX.index(a)
    x = int(b)
    b = int(b)
    for y in range(0,-b):
        index = index - 1
        movelist.append((letterlistt[index][x]))
        x = x + 1
    if a in boardX:
        index = boardX.index(a)
    x = int(b)-2
    for y in range(-2,2):
        index = index - 1
        movelist.append((letterlistt[index][x]))
        x = (x - 1)
    
    if a in boardX:
        index = boardX.index(a)
    x = int(b)
    for y in range(0,-b):
        index = index + 1
        movelist.append((letterlistt[index][x]))
        x = x + 1
    if a in boardX:
        index = boardX.index(a)
    x = int(b)-2
    for y in range(-2,2):
        index = index + 1
        movelist.append((letterlistt[index][x]))
        x = (x - 1)
    if nextPos in movelist:
        valid = True
    else:
        valid = False
    return valid


#Purpose: The purpose of this function is to check if the attempted move by the queen is valid.
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkQueenMove(currentPos,nextPos):
    boardX = 'A B C D E F G H'.split()
    BoardY = '1 2 3 4 5 6 7 8'.split()
    letterlistt = []
    for letter in boardX:
        boardnums = [(letter + str(x)) for x in range(1,9)]
        letterlistt.append(boardnums)
    movelist = []
    a,b = currentPos[0],currentPos[1]
    if (b) in BoardY:
        index = BoardY.index(b)
        for x in range(8):
            movelist.append(letterlistt[x][index])
    x = int(b)
    b = int(b)

    
    if a in boardX:
        index = boardX.index(a)
    x = int(b)
    b = int(b)
    for y in range(0,-b):
        index = index + 1
        movelist.append((letterlistt[index][x]))
        x = x + 1
    if a in boardX:
        index = boardX.index(a)
    x = int(b)-2
    for y in range(0,-b):
        index = index + 1
        movelist.append((letterlistt[index][x]))
        x = (x - 1)
    if a in boardX:
        index = boardX.index(a)
    for x in range(8):
        movelist.append((letterlistt[index][x]))
    if b in boardX:
        index = boardX.index(b)
    for x in range(8):
        movelist.append((letterlistt[x][index]))
    
    if nextPos in movelist:
        valid = True
    else:
        valid = False
    return valid

#Purpose: The purpose of this function is to check if the attempted move of the king is valid
#Parameter: str(currentPos) and str(nextPos)
#Return Bool(Valid)
def checkKingMove(currentPos,nextPos):
    boardX = 'A B C D E F G H'.split()
    letterlistt = []
    for letter in boardX:
        boardnums = [(letter + str(x)) for x in range(1,9)]
        letterlistt.append(boardnums)
    movelist = []
    a,b = currentPos[0],currentPos[1]
   
    if a in boardX:
        index = boardX.index(a)
    x = int(b)-1
    for y in range(2):
        movelist.append((letterlistt[index - 1][x]))
        index = index + 2
    if a in boardX:
        index = boardX.index(a)
    x = int(b)-2
    for y in range(3):
        movelist.append((letterlistt[index - 1][x]))
        index = index + 1
    if a in boardX:
        index = boardX.index(a)
    x = int(b)
    for y in range(3):
        movelist.append((letterlistt[index - 1][x]))
        index = index + 1
    if nextPos in movelist:
        valid = True
    else:
        valid = False
    return valid



#Purpose: The purpose of this function is to check if the inputted move is valid in regards to the chosen piece
#Parameter: str(Piece) and str(currentPos) and str(nextPos)
#Return None
def checkValidMove(piece, currentPos,nextPos):
    piece = piece.title()
    currentPos = currentPos.upper()
    nextPos = nextPos.upper()
    a = checkMoved(currentPos,nextPos)
    b =checkBounds(nextPos)
    c = ''
    if a and b == True:
        if piece == "Bishop":
            c = checkBishopMove(currentPos,nextPos)
        elif piece == "Queen":
            c = checkQueenMove(currentPos,nextPos)
        elif piece == "Rook":
            c = checkRookMove(currentPos,nextPos)
        elif piece == "King":
            c = checkKingMove(currentPos,nextPos)
        else:
            c = False
    print(f'{c}\n')

#Purpose: The purpose of this function is to act as the main function for easy tests
#Parameter: str(Piece) and str(currentPos) and str(nextPos)
#Return Bool(Valid)
def main(piece, currentPos,nextPos):
    valid = checkValidMove(piece, currentPos,nextPos)
    return valid


    
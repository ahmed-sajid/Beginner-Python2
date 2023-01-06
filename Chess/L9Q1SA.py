#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L8Q1SA.py
#  
#  Purpose:   This program will determine certain times on the planet Ork.
#  ----------------------------------------------------
from graphics import *
from L8Q1SA import *

#Notice: L9Q1SA and L8Q1SA need to be in the same img folder with all the chess pieces
# or else the program wont be able to access the images for the chess pieces and player turn image

#Main Function
#Purpose: Lays foundation to start chess game by initializing pieces
#Parameter: None
#Return None
# The z variable is used to automatically switch turns every two clicks (one to select piece one to move it), although it is not
# used yet I figured when we make the pieces move it will be needed, delete just removed all pieces so they can properly be
# initialized again, finally color can be changed by changing the colors in setupBoardInfo
def mainGameM2():
    boardDict,dimensions = setupBoardInfo([50,50],500,500,['white','black'])
    imgturn = 'king2.png'
    win, boardDict,infobtn,imgturn,icon = setupBoard(boardDict,dimensions,imgturn)
    drawn = ''
    turn = ''
    z = 0
    while True:
        while True:
            y = win.getMouse()
            if y:
                break
        if False:
            break
        name = getCell(y,infobtn,dimensions,boardDict)
        if name != 'Out of Bounds':
            z = z + 1
        if name == 'RB':
            delete(drawn,win)
            turn,drawn= initializeBoard(win, boardDict)
            z = 0
            imgturn = 'king1.png'
        if turn == 0 and name!= 'Out of Bounds' and z%2==0 and z!= 0:
            imgturn = 'king1.png'
            turn = 1
        elif turn == 1 and name!= 'Out of Bounds' and z%2 == 0 and z!= 0:
            imgturn = 'king2.png'
            turn = 0
        delete(icon,win)
        c = Image(Point(85,475),imgturn)
        icon.append(c)
        c.draw(win)

#Purpose: Adds all pieces to the boar and sets it up for a game to start
#Parameter: win(graphics object), boardDict(dictionary)
#Return Turn(int), Drawn(list)(used for the delete function)
def initializeBoard(win, boardDict):
    drawn = []
    spaces_w = {}
    spaces_b = {}
    
    for y in range(8):
        l = 'A B C D E F G H'.split()
        for z in range(2,3):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            up = (temp.get('cp'))
            m = 'pawn1.png'
            c = Image(up,m)
            c.draw(win)
            drawn.append(c)
            spaces_w.update({aye:m})
    for y in range(8):
        l = 'A B C D E F G H'.split()
        for z in range(7,8):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            up = (temp.get('cp'))
            m = 'pawn2.png'
            c = Image(up,m)
            c.draw(win)
            drawn.append(c)
            spaces_b.update({aye:m})
    for y in range(8):
        l = 'A B C D E F G H'.split()
        m = ['rook2.png','knight2.png','bishop2.png', 'king2.png', 'queen2.png','bishop2.png', 'knight2.png', 'rook2.png']
        for z in range(8,9):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            up = (temp.get('cp'))
            p = (m[y])
            c = Image(up,p)
            c.draw(win)
            drawn.append(c)
            spaces_b.update({aye:p})
    for y in range(8):
        l = 'A B C D E F G H'.split()
        m = ['rook1.png','knight1.png','bishop1.png', 'queen1.png', 'king1.png','bishop1.png', 'knight1.png', 'rook1.png']
        for z in range(1,2):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            up = (temp.get('cp'))
            p = (m[y])
            c = Image(up,p)
            c.draw(win)
            drawn.append(c)
            spaces_w.update({aye:p})
    turn = 1
    return turn,drawn,spaces_b,spaces_w

#Purpose: Helper Function to delete old pieces
#Parameter: win(graphics object), drawn(list)
#Return none
def delete(drawn,win):
    for i in drawn:
        if type(i) != str:
            i.undraw()

#Purpose: Uses users mouse inputs to find where they are clicking and returns where their clicking
# either out of bounds which does nothing, RB which resets the board and Individual cells which will
# be used when we make the pieces move
#Parameter: cp(Point)(this is the users coordinates where they clicked), infobtn((dict)(information about the reset button),
# dimensions(list),boardDict(dict)
#Return Name(str)(this is where the user clicked translated from mouse coordinates)
def getCell(cp,infobtn,dimensions,boardDict):
    temple = []
    lpp = []
    temp = getbutn('sp',infobtn)
    temple.append(temp)
    temp = getbutn('ep',infobtn)
    temple.append(temp)
    temp = getsplitmouse(cp)
    lpp.append(temp)
    if (temple[0][0] <= lpp[0][0] <= temple[1][0]) and temple[0][1] <= lpp[0][1] <= temple[1][1]:
        name = 'RB'
    else:
        name = getsquare(cp,boardDict)
    return name

#Purpose: gets button coordinates to be used in getCell
#Parameter: x(str)(this is the dict key),infobtn(dict)
#Return temp(list)
def getbutn(x,infobtn):
    temp = str((infobtn.get(x)))
    temp = temp[6:-1]
    temp = temp.split(',')
    return temp

#Purpose: Another helper function for get cell,if coordinates do not correspond to the button
# this function will loop through the coordinates of each cell until it finds where the user clicked
#Parameter: x(Point)(users click coordinates),(boardDict(dict))
#Return name(str)
def getsquare(x,boardDict):
    temp = getsplitmouse(x)
    lpp = temp
    for y in range(8):
        l = 'A B C D E F G H'.split()
        for z in range(1,9):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            up,down = str(temp.get('up')),str(temp.get('lp'))
            up,down = up[6:-1], down[6:-1]
            up,down = up.split(','),down.split(',')
            if (float(up[0]) <= float(lpp[0]) <= float(down[0])) and (float(up[1]) <= float(lpp[1]) <= float(down[1])):
                name = str(aye)
                return name
            else:
                name = 'Out of Bounds'
    return name

#Purpose: helper function splits the users coordinates and appends to a list for getCell
#Parameter: wx(Point)(users click coords)
#Return temp(list)
def getsplitmouse(x):
    temp = str(x)
    temp = temp[6:-1]
    temp = temp.split(',')
    return temp

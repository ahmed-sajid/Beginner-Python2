#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L10Q1SA.py
#  
#  Purpose:   This program will determine certain times on the planet Ork.
#  ----------------------------------------------------
from graphics import *
from L9Q1SA import *
from moves import *

#Notice: L9Q1SA and L8Q1SA need to be in the same img folder with all the chess pieces
# or else the program wont be able to access the images for the chess pieces and player turn image

#Main Function
#Purpose: Lays foundation to start chess game by initializing pieces
#Parameter: None
#Return None
# The main function that puts it all together, delete just removed all pieces so they can properly be
# initialized again, finally color can be changed by changing the colors in setupBoardInfo
def mainGameM3():
    boardDict,dimensions = setupBoardInfo([50,50],500,500,['white','black'])
    imgturn = 'king2.png'
    win, boardDict,infobtn,imgturn,icon = setupBoard(boardDict,dimensions,imgturn)
    drawn = ''
    spaces = {}
    turn = 'white'
    pic = []
    while True:
        y = win.getMouse()
        try:
            name = getCell(y,infobtn,dimensions,boardDict)
            if name == 'RB':
                delete(drawn,win)
                turn,drawn,spaces_b,spaces_w= initializeBoard(win, boardDict)
                imgturn = 'king1.png'
            if name != 'Out of Bounds' and name != 'RB':
                pic.append(name)
                cellOccupied(name,spaces_b,spaces_w)
                if len(pic) == 2:
                    turn = (calcmove(win,name,boardDict,drawn,spaces_w,spaces_b,pic,turn))
                    if turn == 2:
                        imgturn = 'king2.png'
                    elif turn == 1 :
                        imgturn = 'king1.png'
                if len(pic) >= 2:
                    pic = [] 
            delete(icon,win)
            c = Image(Point(85,475),imgturn)
            icon.append(c)
            c.draw(win)
        except:
            win.close()
            return


#Purpose: Checks if an inputted move is valid and if it is, proceeds with the move and undrawing the old insance of the piece
#Parameter: win(graphobj), name(str),boardDict (dict), drawn(dict], spaces_w(dict),spaces_b(dict),pic(list),turn(int)
#Return Turn (int)
def calcmove(win,name,boardDict,drawn,spaces_w,spaces_b,pic,turn):
    lemp = spaces_w.values()
    onep = (spaces_w.get(pic[0]))
    if onep != None:
        if turn == 1:
            twop = onep
            for x in range(len(twop)):
                if twop[x].isalpha() != True:
                    index = twop.index(twop[x])
            twop = onep[:index-1]
            if isValidMove(twop,pic[0],pic[1],0) == True:
                if onep in lemp:
                    aye = str(pic[1])
                    temp = boardDict.get(aye)
                    up = (temp.get('cp'))
                    c = Image(up,onep)
                    c.draw(win)
                    drawn.append(c)
                    temp = (boardDict.get(pic[0]))
                    cp = temp.get('cp')
                    form = Image(cp, 60, 60)
                    for x in range(len(drawn)):
                        temp = drawn[x]
                        if str(form) == str(temp):
                            l = (drawn[x])
                            l = [l]
                            drawn[x] = ''
                            delete(l,win)
                    spaces_w.pop(pic[0]) 
                    spaces_w.update({pic[1]:onep})
                    turn = 2
    if turn == 2:
        lemp = spaces_b.values()
        onep = (spaces_b.get(pic[0]))
        if onep != None:
            twop = onep
            for x in range(len(twop)):
                if twop[x].isalpha() != True:
                    index = twop.index(twop[x])
            twop = onep[:index-1]
            if isValidMove(twop,pic[0],pic[1],1) == True:
                if onep in lemp:
                    aye = str(pic[1])
                    temp = boardDict.get(aye)
                    up = (temp.get('cp'))
                    c = Image(up,onep)
                    c.draw(win)
                    drawn.append(c)
                    temp = (boardDict.get(pic[0]))
                    cp = temp.get('cp')
                    form = Image(cp, 60, 60)
                    for x in range(len(drawn)):
                        temp = drawn[x]
                        if str(form) == str(temp):
                            l = (drawn[x])
                            l = [l]
                            drawn[x] = ''
                            delete(l,win)
                    spaces_b.pop(pic[0]) 
                    spaces_b.update({pic[1]:onep})
                    turn = 1
    
    return turn

#Purpose: Checks if a cell is occupied and if it is, gives info on the selected cell. I did not use this in my code
# but it could be useful when implementing the capturing mechanic
#Parameter: name(str), spaces_b(dict), spaces_w(dict)
#Return isOccupied(bool),info(str)
# The z variable is used to automatically switch turns every two clicks (one to select piece one to move it), although it is not
# used yet I figured when we make the pieces move it will be needed, delete just removed all pieces so they can properly be
# initialized again, finally color can be changed by changing the colors in setupBoardInfo
def cellOccupied(name,spaces_b,spaces_w):
    temp = (spaces_b,spaces_w)
    temp =str(temp)
    info = ''
    if name in temp:
        a = spaces_b.keys()
        b = spaces_w.keys()
        if name in a:
            info = spaces_b.get(name)
        if name in b:
            info = spaces_w.get(name)
        info = str(info)
        for x in range(len(info)):
            if info[x].isalpha() != True:
                index = info.index(info[x])
                info = info[:index+1]
                break
    return True,info

mainGameM3()
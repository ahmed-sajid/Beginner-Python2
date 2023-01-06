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
from img import *

def mainGameM2():
    boardDict,dimensions = setupBoardInfo([50,50],500,500)
    imgturn = r"C:\Users\Ahmed\Desktop\Coding\CMPT 103\img\king1.png"
    win, boardDict,infobtn,imgturn = setupBoard(boardDict,dimensions,imgturn)
    cp = []
    x = True
    while True:
        while True:
            y = win.getMouse()
            if y:
                break
        if False:
            break
        name = getCell(y,infobtn,dimensions,boardDict)
        # print(name)
        if name == 'Button':
            initializeBoard(win, boardDict,infobtn,imgturn)
            
        
    win.close()

def initializeBoard(win, boardDict):
    for y in range(8):
        l = 'A B C D E F G H'.split()
        for z in range(1,9):
            aye = (str(l[y]+ str(z)))
            temp = boardDict.get(aye)
            center = str(temp.get('cp'))
            up = up[6:-1]
            print(up)
    
    
    
    


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
        name = 'Button'
    else:
        name = getsquare(cp,boardDict)
    return name

def getbutn(x,infobtn):
    temp = str((infobtn.get(x)))
    temp = temp[6:-1]
    temp = temp.split(',')
    return temp

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
def getsplitmouse(x,):
    temp = str(x)
    temp = temp[6:-1]
    temp = temp.split(',')
    return temp

mainGameM2()
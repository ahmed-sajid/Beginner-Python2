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


#Main Function
#Purpose: Uses helper functions to draw the canvas for a chess game
#Parameter: None
#Return None
def mainGameM1():
    boardDict,dimensions = setupBoardInfo([50,50],500,500,['black','white'])
    imgturn = 'king2.png'
    win, boardDict,infobtn,imgturn = setupBoard(boardDict,dimensions,imgturn)
    x = True
    while x == True:
        cords = win.getMouse()
        if win.close():
            x = False
    return win

#Purpose: Sets up the dictionary containing the coords of each square
#Parameter: list(sp), int(width), int(height)
#Return boardDict(dict)

def setupBoardInfo(sp,width,height,color):
    dimensions = [sp,width,height]
    boardDict = {"A1":{
        'up' : Point(50,50),
        'cp' : Point(75,75),
        'lp' : Point(100,100),
        'color': color[0]},
        "A2":{
        'up' : Point(50,100),
        'cp' : Point(75,125),
        'lp' : Point(100,150),
        'color': color[1]},
        "A3":{
        'up' : Point(50,150),
        'cp' : Point(75,175),
        'lp' : Point(100,200),
        'color': color[0]},
        "A4":{
        'up' : Point(50,200),
        'cp' : Point(75,225),
        'lp' : Point(100,250),
        'color': color[1]},
        "A5":{
        'up' : Point(50,250),
        'cp' : Point(75,275),
        'lp' : Point(100,300),
        'color': color[0]},
        "A6":{
        'up' : Point(50,300),
        'cp' : Point(75,325),
        'lp' : Point(100,350),
        'color': color[1]},
        "A7":{
        'up' : Point(50,350),
        'cp' : Point(75,375),
        'lp' : Point(100,400),
        'color': color[0]},
        "A8":{
        'up' : Point(50,400),
        'cp' : Point(75,425),
        'lp' : Point(100,450),
        'color': color[1]},
        
        "B1":{
        'up' : Point(100,50),
        'cp' : Point(125,75),
        'lp' : Point(150,100),
        'color': color[1]},
        "B2":{
        'up' : Point(100,100),
        'cp' : Point(125,125),
        'lp' : Point(150,150),
        'color': color[0]},
        "B3":{
        'up' : Point(100,150),
        'cp' : Point(125,175),
        'lp' : Point(150,200),
        'color': color[1]},
        "B4":{
        'up' : Point(100,200),
        'cp' : Point(125,225),
        'lp' : Point(150,250),
        'color': color[0]},
        "B5":{
        'up' : Point(100,250),
        'cp' : Point(125,275),
        'lp' : Point(150,300),
        'color': color[1]},
        "B6":{
        'up' : Point(100,300),
        'cp' : Point(125,325),
        'lp' : Point(150,350),
        'color': color[0]},
        "B7":{
        'up' : Point(100,350),
        'cp' : Point(125,375),
        'lp' : Point(150,400),
        'color': color[1]},
        "B8":{
        'up' : Point(100,400),
        'cp' : Point(125,425),
        'lp' : Point(150,450),
        'color': color[0]},
        
        "C1":{
        'up' : Point(150,50),
        'cp' : Point(175,75),
        'lp' : Point(200,100),
        'color': color[0]},
        "C2":{
        'up' : Point(150,100),
        'cp' : Point(175,125),
        'lp' : Point(200,150),
        'color': color[1]},
        "C3":{
        'up' : Point(150,150),
        'cp' : Point(175,175),
        'lp' : Point(200,200),
        'color': color[0]},
        "C4":{
        'up' : Point(150,200),
        'cp' : Point(175,225),
        'lp' : Point(200,250),
        'color': color[1]},
        "C5":{
        'up' : Point(150,250),
        'cp' : Point(175,275),
        'lp' : Point(200,300),
        'color': color[0]},
        "C6":{
        'up' : Point(150,300),
        'cp' : Point(175,325),
        'lp' : Point(200,350),
        'color': color[1]},
        "C7":{
        'up' : Point(150,350),
        'cp' : Point(175,375),
        'lp' : Point(200,400),
        'color': color[0]},
        "C8":{
        'up' : Point(150,400),
        'cp' : Point(175,425),
        'lp' : Point(200,450),
        'color': color[1]},

        "D1":{
        'up' : Point(200,50),
        'cp' : Point(225,75),
        'lp' : Point(250,100),
        'color': color[1]},
        "D2":{
        'up' : Point(200,100),
        'cp' : Point(225,125),
        'lp' : Point(250,150),
        'color': color[0]},
        "D3":{
        'up' : Point(200,150),
        'cp' : Point(225,175),
        'lp' : Point(250,200),
        'color': color[1]},
        "D4":{
        'up' : Point(200,200),
        'cp' : Point(225,225),
        'lp' : Point(250,250),
        'color': color[0]},
        "D5":{
        'up' : Point(200,250),
        'cp' : Point(225,275),
        'lp' : Point(250,300),
        'color': color[1]},
        "D6":{
        'up' : Point(200,300),
        'cp' : Point(225,325),
        'lp' : Point(250,350),
        'color': color[0]},
        "D7":{
        'up' : Point(200,350),
        'cp' : Point(225,375),
        'lp' : Point(250,400),
        'color': color[1]},
        "D8":{
        'up' : Point(200,400),
        'cp' : Point(225,425),
        'lp' : Point(250,450),
        'color': color[0]},
        
        "E1":{
        'up' : Point(250,50),
        'cp' : Point(275,75),
        'lp' : Point(300,100),
        'color': color[0]},
        "E2":{
        'up' : Point(250,100),
        'cp' : Point(275,125),
        'lp' : Point(300,150),
        'color': color[1]},
        "E3":{
        'up' : Point(250,150),
        'cp' : Point(275,175),
        'lp' : Point(300,200),
        'color': color[0]},
        "E4":{
        'up' : Point(250,200),
        'cp' : Point(275,225),
        'lp' : Point(300,250),
        'color': color[1]},
        "E5":{
        'up' : Point(250,250),
        'cp' : Point(275,275),
        'lp' : Point(300,300),
        'color': color[0]},
        "E6":{
        'up' : Point(250,300),
        'cp' : Point(275,325),
        'lp' : Point(300,350),
        'color': color[1]},
        "E7":{
        'up' : Point(250,350),
        'cp' : Point(275,375),
        'lp' : Point(300,400),
        'color': color[0]},
        "E8":{
        'up' : Point(250,400),
        'cp' : Point(275,425),
        'lp' : Point(300,450),
        'color': color[1]},
        
        "F1":{
        'up' : Point(300,50),
        'cp' : Point(325,75),
        'lp' : Point(350,100),
        'color': color[1]},
        "F2":{
        'up' : Point(300,100),
        'cp' : Point(325,125),
        'lp' : Point(350,150),
        'color': color[0]},
        "F3":{
        'up' : Point(300,150),
        'cp' : Point(325,175),
        'lp' : Point(350,200),
        'color': color[1]},
        "F4":{
        'up' : Point(300,200),
        'cp' : Point(325,225),
        'lp' : Point(350,250),
        'color': color[0]},
        "F5":{
        'up' : Point(300,250),
        'cp' : Point(325,275),
        'lp' : Point(350,300),
        'color': color[1]},
        "F6":{
        'up' : Point(300,300),
        'cp' : Point(325,325),
        'lp' : Point(350,350),
        'color': color[0]},
        "F7":{
        'up' : Point(300,350),
        'cp' : Point(325,375),
        'lp' : Point(350,400),
        'color': color[1]},
        "F8":{
        'up' : Point(300,400),
        'cp' : Point(325,425),
        'lp' : Point(350,450),
        'color': color[0]},
        
        "G1":{
        'up' : Point(350,50),
        'cp' : Point(375,75),
        'lp' : Point(400,100),
        'color': color[0]},
        "G2":{
        'up' : Point(350,100),
        'cp' : Point(375,125),
        'lp' : Point(400,150),
        'color': color[1]},
        "G3":{
        'up' : Point(350,150),
        'cp' : Point(375,175),
        'lp' : Point(400,200),
        'color': color[0]},
        "G4":{
        'up' : Point(350,200),
        'cp' : Point(375,225),
        'lp' : Point(400,250),
        'color': color[1]},
        "G5":{
        'up' : Point(350,250),
        'cp' : Point(375,275),
        'lp' : Point(400,300),
        'color': color[0]},
        "G6":{
        'up' : Point(350,300),
        'cp' : Point(375,325),
        'lp' : Point(400,350),
        'color': color[1]},
        "G7":{
        'up' : Point(350,350),
        'cp' : Point(375,375),
        'lp' : Point(400,400),
        'color': color[0]},
        "G8":{
        'up' : Point(350,400),
        'cp' : Point(375,425),
        'lp' : Point(400,450),
        'color': color[1]},
        
        
        "H1":{
        'up' : Point(400,50),
        'cp' : Point(425,75),
        'lp' : Point(450,100),
        'color': color[1]},
        "H2":{
        'up' : Point(400,100),
        'cp' : Point(425,125),
        'lp' : Point(450,150),
        'color': color[0]},
        "H3":{
        'up' : Point(400,150),
        'cp' : Point(425,175),
        'lp' : Point(450,200),
        'color': color[1]},
        "H4":{
        'up' : Point(400,200),
        'cp' : Point(425,225),
        'lp' : Point(450,250),
        'color': color[0]},
        "H5":{
        'up' : Point(400,250),
        'cp' : Point(425,275),
        'lp' : Point(450,300),
        'color': color[1]},
        "H6":{
        'up' : Point(400,300),
        'cp' : Point(425,325),
        'lp' : Point(450,350),
        'color': color[0]},
        "H7":{
        'up' : Point(400,350),
        'cp' : Point(425,375),
        'lp' : Point(450,400),
        'color': color[1]},
        "H8":{
        'up' : Point(400,400),
        'cp' : Point(425,425),
        'lp' : Point(450,450),
        'color': color[0]},
        }
    return boardDict,dimensions

#Purpose: Sets up the board and draws the actual canvas using the information from previous function
#Parameter: boardDict(dict), dimensions(list), imgturn(string(path to image))
#Return win(graphicObj), boardDict(dict),infobtn(dict),imgturn(str)
def setupBoard(boardDict,dimensions,imgturn):
    sp = dimensions[0]
    width = dimensions[1]
    height = dimensions[2]
    win = GraphWin('',width,height)
    win.setBackground('light grey')
    for x in range(64):
            key = list(boardDict)[x]
            temp = boardDict[key]
            c = Rectangle(temp.get('up'),temp.get('lp'))
            c.setFill(temp.get('color'))
            c.draw(win)
    for x in range(8):
        key = list(boardDict)[x]
        lets = 'A B C D E F G H '.split()
        keyp = ''.join(key)
        tl = lets[x]
        b = (int(keyp[1]))
        c = Text(Point(55.75*b,25),tl)
        c.draw(win)
        c = Text(Point(25,b*55.75),b)
        c.draw(win)
    
    infobtn = {'sp': Point(375,460),
               'ep':Point(450,485)}
    button = []
    icon = []
    for x in range(2):
        key = list(infobtn)[x]
        temp = infobtn[key]
        button.append(temp)
    c = Rectangle(button[0],button[1])
    c.setFill('white')
    c.draw(win)
    c = Text(Point(410,472),'Restart')
    c.draw(win)        
    c = Image(Point(85,475),imgturn)
    c.draw(win)
    icon.append(c)
    c = Text(Point(155,476),"Player's Turn")
    c.draw(win)
    return win, boardDict,infobtn,imgturn, icon

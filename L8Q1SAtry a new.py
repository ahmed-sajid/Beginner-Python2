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
    boardDict,dimensions = setupBoardInfo([50,50],500,500)
    imgturn = r"C:\Users\Ahmed\Desktop\Coding\CMPT 103\img\king1.png"
    win, boardDict,infobtn,imgturn = setupBoard(boardDict,dimensions,imgturn)
    x = True
    while x == True:
        cords = win.getMouse()
        if win.close():
            x = False
    return

#Purpose: Sets up the dictionary containing the coords of each square
#Parameter: list(sp), int(width), int(height)
#Return boardDict(dict)

def setupBoardInfo(sp,width,height):
    dimensions = [sp,width,height]
    boardDict = {"A1":{
        'up' : Point(50,50),
        'cp' : Point(75,75),
        'lp' : Point(100,100),
        'color': 'white'},
        "A2":{
        'up' : Point(50,100),
        'cp' : Point(75,125),
        'lp' : Point(100,150),
        'color':'black'},
        "A3":{
        'up' : Point(50,150),
        'cp' : Point(75,175),
        'lp' : Point(100,200),
        'color':'white'},
        "A4":{
        'up' : Point(50,200),
        'cp' : Point(75,225),
        'lp' : Point(100,250),
        'color':'black'},
        "A5":{
        'up' : Point(50,250),
        'cp' : Point(75,275),
        'lp' : Point(100,300),
        'color':'white'},
        "A6":{
        'up' : Point(50,300),
        'cp' : Point(75,325),
        'lp' : Point(100,350),
        'color':'black'},
        "A7":{
        'up' : Point(50,350),
        'cp' : Point(75,375),
        'lp' : Point(100,400),
        'color':'white'},
        "A8":{
        'up' : Point(50,400),
        'cp' : Point(75,425),
        'lp' : Point(100,450),
        'color':'black'},
        
        "B1":{
        'up' : Point(100,50),
        'cp' : Point(125,75),
        'lp' : Point(150,100),
        'color': 'black'},
        "B2":{
        'up' : Point(100,100),
        'cp' : Point(125,125),
        'lp' : Point(150,150),
        'color':'white'},
        "B3":{
        'up' : Point(100,150),
        'cp' : Point(125,175),
        'lp' : Point(150,200),
        'color':'black'},
        "B4":{
        'up' : Point(100,200),
        'cp' : Point(125,225),
        'lp' : Point(150,250),
        'color':'white'},
        "B5":{
        'up' : Point(100,250),
        'cp' : Point(125,275),
        'lp' : Point(150,300),
        'color':'black'},
        "B6":{
        'up' : Point(100,300),
        'cp' : Point(125,325),
        'lp' : Point(150,350),
        'color':'white'},
        "B7":{
        'up' : Point(100,350),
        'cp' : Point(125,375),
        'lp' : Point(150,400),
        'color':'black'},
        "B8":{
        'up' : Point(100,400),
        'cp' : Point(125,425),
        'lp' : Point(150,450),
        'color':'white'},
        
        "C1":{
        'up' : Point(150,50),
        'cp' : Point(175,75),
        'lp' : Point(200,100),
        'color': 'white'},
        "C2":{
        'up' : Point(150,100),
        'cp' : Point(175,125),
        'lp' : Point(200,150),
        'color':'black'},
        "C3":{
        'up' : Point(150,150),
        'cp' : Point(175,175),
        'lp' : Point(200,200),
        'color':'white'},
        "C4":{
        'up' : Point(150,200),
        'cp' : Point(175,225),
        'lp' : Point(200,250),
        'color':'black'},
        "C5":{
        'up' : Point(150,250),
        'cp' : Point(175,275),
        'lp' : Point(200,300),
        'color':'white'},
        "C6":{
        'up' : Point(150,300),
        'cp' : Point(175,325),
        'lp' : Point(200,350),
        'color':'black'},
        "C7":{
        'up' : Point(150,350),
        'cp' : Point(175,375),
        'lp' : Point(200,400),
        'color':'white'},
        "C8":{
        'up' : Point(150,400),
        'cp' : Point(175,425),
        'lp' : Point(200,450),
        'color':'black'},

        "D1":{
        'up' : Point(200,50),
        'cp' : Point(225,75),
        'lp' : Point(250,100),
        'color': 'black'},
        "D2":{
        'up' : Point(200,100),
        'cp' : Point(225,125),
        'lp' : Point(250,150),
        'color':'white'},
        "D3":{
        'up' : Point(200,150),
        'cp' : Point(225,175),
        'lp' : Point(250,200),
        'color':'black'},
        "D4":{
        'up' : Point(200,200),
        'cp' : Point(225,225),
        'lp' : Point(250,250),
        'color':'white'},
        "D5":{
        'up' : Point(200,250),
        'cp' : Point(225,275),
        'lp' : Point(250,300),
        'color':'black'},
        "D6":{
        'up' : Point(200,300),
        'cp' : Point(225,325),
        'lp' : Point(250,350),
        'color':'white'},
        "D7":{
        'up' : Point(200,350),
        'cp' : Point(225,375),
        'lp' : Point(250,400),
        'color':'black'},
        "D8":{
        'up' : Point(200,400),
        'cp' : Point(225,425),
        'lp' : Point(250,450),
        'color':'white'},
        
        "E1":{
        'up' : Point(250,50),
        'cp' : Point(275,75),
        'lp' : Point(300,100),
        'color': 'white'},
        "E2":{
        'up' : Point(250,100),
        'cp' : Point(275,125),
        'lp' : Point(300,150),
        'color':'black'},
        "E3":{
        'up' : Point(250,150),
        'cp' : Point(275,175),
        'lp' : Point(300,200),
        'color':'white'},
        "E4":{
        'up' : Point(250,200),
        'cp' : Point(275,225),
        'lp' : Point(300,250),
        'color':'black'},
        "E5":{
        'up' : Point(250,250),
        'cp' : Point(275,275),
        'lp' : Point(300,300),
        'color':'white'},
        "E6":{
        'up' : Point(250,300),
        'cp' : Point(275,325),
        'lp' : Point(300,350),
        'color':'black'},
        "E7":{
        'up' : Point(250,350),
        'cp' : Point(275,375),
        'lp' : Point(300,400),
        'color':'white'},
        "E8":{
        'up' : Point(250,400),
        'cp' : Point(275,425),
        'lp' : Point(300,450),
        'color':'black'},
        
        "F1":{
        'up' : Point(300,50),
        'cp' : Point(325,75),
        'lp' : Point(350,100),
        'color': 'black'},
        "F2":{
        'up' : Point(300,100),
        'cp' : Point(325,125),
        'lp' : Point(350,150),
        'color':'white'},
        "F3":{
        'up' : Point(300,150),
        'cp' : Point(325,175),
        'lp' : Point(350,200),
        'color':'black'},
        "F4":{
        'up' : Point(300,200),
        'cp' : Point(325,225),
        'lp' : Point(350,250),
        'color':'white'},
        "F5":{
        'up' : Point(300,250),
        'cp' : Point(325,275),
        'lp' : Point(350,300),
        'color':'black'},
        "F6":{
        'up' : Point(300,300),
        'cp' : Point(325,325),
        'lp' : Point(350,350),
        'color':'white'},
        "F7":{
        'up' : Point(300,350),
        'cp' : Point(325,375),
        'lp' : Point(350,400),
        'color':'black'},
        "F8":{
        'up' : Point(300,400),
        'cp' : Point(325,425),
        'lp' : Point(350,450),
        'color':'white'},
        
        "G1":{
        'up' : Point(350,50),
        'cp' : Point(375,75),
        'lp' : Point(400,100),
        'color': 'white'},
        "G2":{
        'up' : Point(350,100),
        'cp' : Point(375,125),
        'lp' : Point(400,150),
        'color':'black'},
        "G3":{
        'up' : Point(350,150),
        'cp' : Point(375,175),
        'lp' : Point(400,200),
        'color':'white'},
        "G4":{
        'up' : Point(350,200),
        'cp' : Point(375,225),
        'lp' : Point(400,250),
        'color':'black'},
        "G5":{
        'up' : Point(350,250),
        'cp' : Point(375,275),
        'lp' : Point(400,300),
        'color':'white'},
        "G6":{
        'up' : Point(350,300),
        'cp' : Point(375,325),
        'lp' : Point(400,350),
        'color':'black'},
        "G7":{
        'up' : Point(350,350),
        'cp' : Point(375,375),
        'lp' : Point(400,400),
        'color':'white'},
        "G8":{
        'up' : Point(350,400),
        'cp' : Point(375,425),
        'lp' : Point(400,450),
        'color':'black'},
        
        
        "H1":{
        'up' : Point(400,50),
        'cp' : Point(425,75),
        'lp' : Point(450,100),
        'color': 'black'},
        "H2":{
        'up' : Point(400,100),
        'cp' : Point(425,125),
        'lp' : Point(450,150),
        'color':'white'},
        "H3":{
        'up' : Point(400,150),
        'cp' : Point(425,175),
        'lp' : Point(450,200),
        'color':'black'},
        "H4":{
        'up' : Point(400,200),
        'cp' : Point(425,225),
        'lp' : Point(450,250),
        'color':'white'},
        "H5":{
        'up' : Point(400,250),
        'cp' : Point(425,275),
        'lp' : Point(450,300),
        'color':'black'},
        "H6":{
        'up' : Point(400,300),
        'cp' : Point(425,325),
        'lp' : Point(450,350),
        'color':'white'},
        "H7":{
        'up' : Point(400,350),
        'cp' : Point(425,375),
        'lp' : Point(450,400),
        'color':'black'},
        "H8":{
        'up' : Point(400,400),
        'cp' : Point(425,425),
        'lp' : Point(450,450),
        'color':'white'},
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
    c = Text(Point(145,476),"Player's Turn")
    c.draw(win)
    return win, boardDict,infobtn,imgturn

mainGameM1()
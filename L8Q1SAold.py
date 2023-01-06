#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L5Q123SA.py
#  
#  Purpose:   This program will determine certain times on the planet Ork.
#  ----------------------------------------------------
from graphics import *
#This is for question 1
#Purpose: Converts total seconds into Ork time format
#Parameter: int(seconds), int(mode)
#Return str(time)
def mainGameM1():
    return

#Purpose: Sets up the dictionary containing the coords of each square
#Parameter: list(sp), int(width), int(height)
#Return boardDict(dict)
def setupBoardInfo(sp,width,height):
    a = sp[0]
    b = sp[1]
    boardDict = {}
    boardDict.update({'Bstart':[a,b],'Bend':[width - a,height-b]})
    win = GraphWin('',width,height)
    d = [boardDict.get('Bstart'),boardDict.get('Bend')]
    cords = []
    
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
        'color':'black'}}
    for x in range(8):
        key = list(boardDict)[x]
        temp = boardDict[key]
        c = Rectangle(temp.get('up'),temp.get('lp'))
        c.setFill(temp.get('color'))
        c.draw(win)
    win.getMouse()
    
    
    
    
setupBoardInfo([50,50],500,500)
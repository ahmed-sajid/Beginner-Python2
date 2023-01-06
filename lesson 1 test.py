from graphics import *


def setupScreen(title,width,height,lines = False):
    win = GraphWin(title,width,height)
    r = Rectangle(Point(200,200),Point(400,400))
    red = color_rgb(255,0,0)
    r.setFill(red)
    r.draw(win)
    white = color_rgb(255,255,255)
    r = Rectangle(Point(275,200),Point(325,300))
    r.setFill(white)
    r.setOutline(white)
    r.draw(win)
    r = Circle(Point(300,300),25)
    r.setFill(white)
    r.setOutline(white)
    r.draw(win)
    win.getMouse()

setupScreen('',600,600)
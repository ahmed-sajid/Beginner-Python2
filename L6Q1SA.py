#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L6Q1SA.py
#  
#  Purpose:   This program will extract the information from a python file and display the results
#  ----------------------------------------------------
from graphics import *

#Purpose: Gets all text information from python file and saves it
#Parameter: str(filename)
#Return list(data)

def loadData(filename):
    file = open(filename,"r")
    data = [ ]
    line = file.readline()
    while(line):
        data.append(line.rstrip())
        line = file.readline()
    file.close()
    return data


#Purpose: Finds the end of a function name in a string
#Parameter: str(name)
#Return int(index)
# I did not end up using this function.

def findEndofName(name):
    for x in range(len(name)):
        if name[x].isalpha() == False and name[x].isspace() == False:
            index = name.index(name[x])
            index = int(index)
            break
    return index

#Purpose: Gets all the function information and stores it into lists
#Parameter: list(data)
#Return list(fname),list(fparam),list(output)

def getFunctions(data):
    fname= []
    fparam = []
    output = []
    marker1 = 'def'
    marker2 = 'return'
    p = []
    for x in range(len(data)):
        if marker1 in data[x] and ':' in data[x]:
            a = str(data[x])
            for i in range(len(a)):
                if a[i].isalpha() != True and a[i].isspace() != True:
                    index = a.index(a[i])
                    fname.append(a[4:index])
                    fparam.append(a[index:int(len(a))-1])
                    break
        elif marker2 in data[x] and '=' not in data[x]:
            b = str(data[x])
            index = int(b.index(marker2)) + 7 
            output.append(b[index:int(len(b))])
    
    return fname, fparam, output

#Purpose: Draws the margins for the page using a scale of 8.5 x 11 inches
#Parameter: GraphicObj(win),int(height),int(width)
#Return None

def drawMargins(win,height,width):
    c = Line(Point(width//8.5,height//22), Point(width-(width//8.5),height//22))
    c.draw(win)
    c = Line(Point(width//8.5,height-(height//22)), Point(width-(width//8.5),height-(height//22)))
    c.draw(win)
    c = Line(Point(width//8.5,height//22), Point(width/8.5,height-(height//22)))
    c.draw(win)
    c = Line(Point(width-(width//8.5),height//22), Point(width-(width//8.5),height-(height//22)))
    c.draw(win)
    c = Line(Point(width//8.5,height//7), Point(width-(width//8.5),height//7))
    c.draw(win)
    return None

#Purpose: Draws draft lines on the outer rim of the window to assign a deadzone
#Parameter: GraphicObj(win),int(height),int(width), bool(lines)
#Return GraphicObj(win)

def drawDraftLines(win,height,width,lines = False):
    if lines == True:
        c = Line(Point(1,1), Point(width-1,1))
        c.draw(win)
        c = Line(Point(1,height-1), Point(width-1,height-1))
        c.draw(win)
        c = Line(Point(1,1), Point(1,height-1))
        c.draw(win)
        c = Line(Point(width-1,0), Point(width-1,height))
        c.draw(win)
        drawMargins(win,height,width)
    return win
            
#Purpose: Initializes and draws the canvas
#Parameter: GraphicObj(win),int(height),int(width), bool(lines)
#Return GraphicObj(win)

def setupScreen(title,width,height,lines = False):
    win = GraphWin(title,width,height)
    drawDraftLines(win,height,width,lines)
    drawTitle(win,height,width,title)
    return win

#Purpose: Draws the title onto the canvas
#Parameter: GraphicObj(win),int(height),int(width), str(title)
#Return None

def drawTitle(win,height,width,title):
    message = Text(Point(width//2,height//11),title)
    message.draw(win)
    return None

#Purpose: Draws the function information on the canvas
#Parameter: list(fname),list(fparam),list(output),GraphicObj(win),int(width),int(height)
#Return None

def drawFunctionInfo(fname,fparam,output,win,width,height):
    y = 0
    z =(height - (height//6))//(len(fname))
    print(z)
    for x in range(len(fname)):
        message = Text(Point(width//4 +len(fname[x]*2),((height/6.5)) + y),f'Name : {(fname[x])}')
        message.draw(win)
        message = Text(Point(width//4 + len(fparam[x]*2),((height/6.5)) + y+20 ) ,f'Param : {(fparam[x])}')
        message.draw(win)
        # I added this because I was testing on old labs I did and noticed I was sometimes getting an error
        # because I didn't have a output statement in every function so I added a simple error check
        if 0 <= x < len(output):
            if output[x] != '':
                message = Text(Point(width//4 + len(output[x]*2),((height/6.5)) + y+40) ,f'Return : {(output[x])}')
                message.draw(win)
            else:
                message = Text(Point(width//4,((height/6.5)) + y+40) ,f'Return : None')
                message.draw(win)
        else:
            message = Text(Point(width//4,((height/6.5)) + y+40) ,f'Return : None')
            message.draw(win)
        y = y + z
    return None

#Purpose: Main function will put it all together
#Parameter: str(title),int(height),int(width), bool(lines)
#Return None

def main(title,width,height,name,lines=False):
    data = loadData(name)
    win = setupScreen(title,width,height,lines)
    fname, fparam,output = getFunctions(data)
    drawFunctionInfo(fname,fparam,output,win,680,880)
    win.getMouse()
    win.close()
    return None
main('KILL ME I WANT TO DIE',8.5*80,11*80,'L4Q1SA.py',True)
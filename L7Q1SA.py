#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   76Q1SA.py
#  
#  Purpose:   This program will extract the information from a python file and display the results graphically
#  ----------------------------------------------------
from graphics import *


def loadData(filename):
    file = open(filename,"r")
    data = [ ]
    line = file.readline()
    while(line):
        data.append(line.rstrip())
        line = file.readline()
    file.close()
    return data


#Purpose: Formats the raw data into header and elements
#Parameter: data (str,list)
#Return list(listt),list(elements)
def FormatRawData(data):
    listt = data[0]
    listt = listt.split(',')
    combined = {}
    elements = []
    for x in range(len(listt)):
        leep = []
        for z in range(1,len(data)):
            temp = data[z]
            temp = temp.split(',')
            if 0 <= x <= len(temp):
                if temp[x] == '':
                    leep.append('None')
                leep.append(temp[x])
            else:
                leep.append('None')
        elements.append(leep) 
    return listt, elements


#Purpose: Creates a dictionary with the given info
#Parameter: (list(a)), list(b)
#Return dict(ouch),list(filter)
def make_dict(a,b):
    ouch = {}
    for x in range(len(a)):
        ouch.update({a[x]:b[x]})
    filter = []
    for i in range(len(ouch['Province'])):
        if (ouch['Province'][i]) == 'Alberta':
            filter.append(i)  
    return ouch,filter


#Purpose: converts longitude and latitude to a base x and y
#Parameter: int(long), int(lat)
#Return int(x), int(y)
def ConvertCoords(long,lat):
    longlow,longhigh,xhigh,xlow,latlow,lathigh,yhigh,ylow = -120,-110,456,0,49,60,866,0
    x = ((long-longlow)/(longhigh-longlow))*(xhigh-xlow) + xlow
    y = ((lat-latlow)/(lathigh-latlow))*(yhigh-ylow)+ylow
    y = 866 - y
    return x,y


#Purpose: Graphs all the data over a map of alberta
#Parameter: list(pix)
#Return None
def visualizeData(pix):
    win = GraphWin('Alberta,Canada',456,866)
    img = Image(Point(228,433),r"C:\Users\Ahmed\Desktop\Coding\CMPT 103\alberta_openMap.gif")
    img.draw(win)
    for ent in pix:
        x,y = ent
        c = Circle(Point(x,y),4)
        c.draw(win)
    win.getMouse()
    
    
#Purpose: Main function puts it all together. The data was broken in the original file so 
# I had to fix some of it. Ill attack my csv file so you can test it with my data
#Parameter: none
#Return none
def main():
    data = (loadData('pipeline_incidents_clean.csv'))
    a,b = FormatRawData(data)
    spills,filter = make_dict(a,b)
    c = a.index('Longitude')
    pix = []
    for x in range(1):
        longg,latt = b[c],b[c-1]
        for i in filter:
            long = float(longg[i])
            lat = float(latt[i])
            long,lat = ConvertCoords(long,lat)
            pix.append((long,lat))
    visualizeData(pix)
    
main()
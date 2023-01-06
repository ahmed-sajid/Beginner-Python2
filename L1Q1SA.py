#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L1Q1SA.py
#  
#  Purpose:   This program will determine information based on
#  a given date on a Gregorian Calendar. 
#  ----------------------------------------------------
import math


# This function will calculate the century based on inputted year

def calcCentury(year):
    year = int(year)
    century = int((year*0.01)) + 1
    return century

# This function calculates where the month falls in the year and gives it a 1-12 value

def calcMonth(month):
    month = month.title()
    numbered = "1 2 3 4 5 6 7 8 9 10 11 12".split()
    listt = 'March April May June July August September October November December January February '.split()
    if month in listt:
        index = listt.index(month)
    month = str(numbered[index])
    return month

# This function fixes the year for certain periods of time to match the gregorian calendar

def fixYear(year, month):
    year = str(year)
    year = year[::]
    if (month == '11') or (month == '12') and year == '00':
        year = 99
    
    return year

# This function will calculate what day of the week it was on the inputted date

def calcWeekday(day,month,year):
    
    day = int(day)
    year = int(year)
    m = int((calcMonth(month)))
    y = int(fixYear(year,month))
    c = int(calcCentury(year))
    #print(f'{day} {y} {m} {c}')
    if y == 00 and (m == 11 or m == 12) :
        c = c - 1
    #w = (day + (2.6*m - 0.2)-2*(c-1)+y+(y/4)+((c-1)/4))%7
    w = (day + (2.6*m-0.2) - (c - 1)*2 + y + (y//4)+((c-1)//4))%7
    w = int(w)
    
    listt = ' Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.split()
    dotw = listt[w]
    return dotw

# This function will determine wether or not that year was a leap year 

def isLeapYear(year):
    x = int(year)
    y = 4
    z = 0
    if (x%4 == 0 and x%100 != 0) or (x%400 == 0):
        isleap = True
    else:
        isleap = False

    return isleap

# This function will calculate wether the month has 30, 31, 28, or 29 days.

def calcDaysinMonth(month,year):
    month = str(month).title()
    year = int(year)
    leap = isLeapYear(year)
    days31 = 'January March May July August October December'.split()
    days30 = 'April June September November'.split()
    if month == 'February' and leap == False:
        days = 28
    elif month == 'February' and leap == True:
        days = 29
    if month in days31:
        days = 31
    elif month in days30:
        days = 30
    return days

# This function will take all the deducted data so far and combine it into an easily readable list

def printInformation(day,month,year):
    print(f'Date\t: {day} {month} {year}')
    century = calcCentury(year)
    print('Century\t:',century)
    leapstat = isLeapYear(year)
    print(f'Is a Leap Year\t: {leapstat}')
    daynum = calcDaysinMonth(month,year)
    print(f'Days in Month\t: {daynum}')
    wday = calcWeekday(day,month,year)
    print(f'Weekday\t: {wday}')

print(calcWeekday(12,'january',2022))
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

#This is for question 1
#Purpose: Converts total seconds into Ork time format
#Parameter: int(seconds), int(mode)
#Return str(time)
def orkTime(seconds,mode = 36):
    s = 34596
    hr =(seconds/s)
    min = ((((seconds%s)/s) * 186))
    sec = (seconds%186)
    if mode != 72:
        if hr >= 18:
            suffix = 'PM'
        else:
            suffix = 'AM'
    hr,min,sec = int(hr),int(min),int(sec)
    hr,min,sec = (str(hr).zfill(2),str(min).zfill(3),str(sec).zfill(3))
    if mode != 72:
        print(f'{hr}:{min}:{sec} {suffix}')
    else:
        print(f'{hr}:{min}:{sec}')

#Purpose: inputs a time and converts to 72 hour time
#Parameter: str(time)
#Return str(time72)
def convert72hours(time):
    b = ''.join(time)
    y = []
    for i in range(len(b)):
        if b[i].isalpha() == True:
            y.append(b[i])
    b = ''.join(y)
    b = str(b).upper()
    
    time = time.split(':')
    if b == 'PM':
        time[0] = int(time[0]) + (36)
        time[0] = str(time[0])
    x = str(time)
    y = []
    z = 1
    for i in range(len(x)):
        if x[i].isdigit() == True:
            y.append(x[i])
            z = z + 1
            if z%3 == 0 and z != 9:
                y.append(':')
    x = ''.join(y)
    time72 = x
    return time72

#Purpose: Converts from hr-min-sec to seconds
#Paramaters: str(time)
#Return int(totalseconds)
def convert2seconds(time):
    time = (convert72hours(time))
    x = ''.join(time)
    y = []
    for i in range(len(x)):
        if x[i].isalpha() != True:
            y.append(x[i])
    x = ''.join(y)
    x = x.split(':')
    hr = int(x[0]) * (186*186)
    min = int(x[1]) * 186
    sec = int(x[2])
    total = hr + min + sec
    total = int(total)
    return total


#This is for question 2
#Purpose: Determins the times elapsed in seconds between 2 times 
#Parameter: str(time1), str(time2)
#Return int(time)
def timeElapsed(a,b):
    x = convert2seconds(a)
    y = convert2seconds(b)
    time = y - x
    time = int(time)
    print(time)
    return time

#This is for question 3
#Purpose: Determins the times elapsed in seconds between many times 
#Parameter: str(*times (tuple))
#Return list(secondElapsed)
def durations(*times):
    x = 2
    y = 0
    elapsed = []
    for i in range(len(times)//2):
        a,b = times[y:x]
        t1= timeElapsed(a,b)
        x = x + 2
        y = y + 2
        elapsed.append(t1)
    return elapsed

(orkTime(1245455))
#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L4Q1SA.py
#  
#  Purpose:   This program will determine the value of the resistance of a 4 band resistor based on fixed values corresponding to the colors.
#   
#  ----------------------------------------------------


#Purpose: This function will break the given input into 4 seperate colors
#Parameter: str(colourBands)
#Return list(colourList)
def splitColourString(string):
    split = []
    temp = []
    for x in range(len(string)):
        if string[x].isupper() == True:
            temp = []
            temp.append(string[x])
            x = x + 1
            if 0 <= x < len(string):
                if string[x].isupper() != True:
                    temp.append(string[x])
            split.append(temp)
    colourList = []
    for x in range(len(split)):
        a = (''.join(split[x]))
        colourList.append(a)
    return colourList


#Purpose: The purpose of this function is to conver the list of colours into their respective numerical values
#Parameter: list(colourList)
#Return list(valueList)
def determineValues(colorList):
    color = 'K Br R O Y G B V Gr W Au Ag'.split()
    value = ' 0 1 2 3 4 5 6 7 8 9 -1 -2'.split()
    tolerance = '0 1 2 0 0 0.5 0.25 0.10 0.05 0 5 10'.split()
    valueList = []
    index = 0
    for x in range(len(colorList)-1):
        if colorList[x] in color:
            index = color.index(colorList[x])
        valueList.append(value[index])
    if colorList[3] in color:
        index = color.index(colorList[3])
    valueList.append(tolerance[index])
    return valueList


#Purpose: The purpose of this function is to convert the given values into a single number and a tolerance
#Parameter: list(valueList)
#Return: float(value), float(tolerance)
def value2Float(valueList):
    c = int(''.join(valueList[0:2]))
    d = int(valueList[2])
    x = float(c*(10**d))
    y = float(valueList[3])
    return x, y


#Purpose: The purpose of this function is input the given bands of colour and output the proper value and tolerance that corresponds to the given colours.
#Parameter: str(colourBands)
#Return: float(value), float(tolerance)
def color2Value(colourBands):
    colourList = splitColourString(colourBands)
    valueList = determineValues(colourList)
    value,tolerance = value2Float(valueList)
    return value,tolerance


#Purpose: The purpose of this function is act as the main function that will be used to put all the previous helper functions together
#Parameter: float(value), float(tolerance)
#Return str(dataString)
def formatString(value,tolerance):
    if value < 10**3:
        suffix = ''
    elif (10**3) <= value < 10**6:
        suffix = 'K'
        value = value/(10**3)
    elif (10**6) <= value:
        suffix = 'M' 
        value = value/(10**6)
    dataString = str((f'The resistor has a value of: {value} {suffix}Ω ± {tolerance}%'))
    return dataString



#Purpose: The purpose of this function is act as the main function that will be used to put all the previous helper functions together
#Parameter: None
#Return None
def main():
    colourBands = str(input('Please enter a string: '))
    value,tolerance = color2Value(colourBands)
    dataString = formatString(value,tolerance)
    print(dataString)
    print()



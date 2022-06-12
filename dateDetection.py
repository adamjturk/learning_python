#!/usr/bin/env python3
#dateDetection.py - takes any copied amount of text, finds all dates matching 
#MM/DD/YYYY format, checks their validity, and if valid, adds them to a list

from operator import le
import pyperclip, re

#create regex for valid dates
dateRegex = re.compile(r'''(
    (\d{2})+    
    /
    (\d{2})+
    /
    (\d{4})
)''', re.VERBOSE)

#find matches in clipboard text 
text = str(pyperclip.paste())

#empty list to store found dates
matches = []
#use for loop to iterate through information
for groups in dateRegex.findall(text):
    #when a match is found, a tuple is created with each piece of info.
    #we want to take the first position of that tuple
    #matches.append(groups[0]), if it is valid
    month = int(groups[1])
    day = int(groups[2])
    year = int(groups[3])
    month30 = [4,6,9,11]
    month31 = [1,3,5,7,8,10,12]
    valid = True

    #checking basic months and days
    if month > 12 or month < 1:
        valid = False 
    elif month in month30 and (day > 30 or day < 1):
        valid = False
    elif month in month31 and (day > 31 or day < 1):
        valid = False

    #checking leap years for february
    leapYear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leapYear = True
        else:
            leapYear = True

    #checking if february month is valid
    if leapYear:
        if month == 2 and (day > 29 or day < 1):
            valid = False
    else:
        if month == 2 and (day > 28 or day < 1):
            valid = False

    #if date passes all tests, gets added to matches
    if valid:
        matches.append(groups[0])

#prints all valid dates collected     
print('Dates collected:\n' + str(matches))


        
        


#detect if dates are valid

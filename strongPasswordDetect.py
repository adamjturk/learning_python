#function that detects if argument is a 'strong' password
#strong password in this program is defined as:
    #at least 8 characters long
    #contains both upper and lower case letters
    #has at least 1 digit

import re

isValid = True

def strongPassDetect(password):
    #first checks if password is less than 8 characters
    if len(password) < 8:
        isValid = False
        print('Password must be at least 8 characters')
    else:
        #create criteria to search for using regex
        regexPassLower = re.compile(r'[a-z]')
        regexPassUpper = re.compile(r'[A-Z]')
        regexPassDigit = re.compile(r'[0-9]')
        #search for at least 1 lower case letter
        if regexPassLower.search(password) == None:
            isValid = False
            print('Password must include at least 1 lower case letter')
        #search for at least 1 upper case letter
        if regexPassUpper.search(password) == None:
            isValid = False
            print('Password must include at least 1 upper case letter')
        #search for at least 1 digit
        if regexPassDigit.search(password) == None:
            isValid = False
            print('Password must include at least 1 number')
        

print('Whats your password?')
response = input() 
strongPassDetect(response)

if isValid:
    print('Password is strong!')
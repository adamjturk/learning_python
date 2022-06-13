#write a function that does the same things as strip(), but using regex

import re

#if remove argument is left blank when called, will remove the whitespace characters
#otherwise, will remove characters passed in remove

def stripRegex(string,remove):
    #if second argument is blank, remove whitespaces
    if remove == '':
        searchSpaces = re.compile(r'\s')
        mo = searchSpaces.sub('',string)
        print(mo)
    #else, remove the character of remove argument
    else:
        searchOther = re.compile(remove)
        mo = searchOther.sub('',string)
        print(mo)
        

stripRegex('hello','e')
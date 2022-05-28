#purpose of function is to receive a list as a parameter, then return a string
#that has its entries separated by a comma. Last entry has the word 'and' in front
#of it to signal the end
def listfunc(param):
    #uses a counter to tell when the last entry of the list will come up
    counter = 1
    for i in range(len(param)):
        if counter < len(param):
            print(param[i] + ', ',end='')
            counter = counter + 1
        else:
            print('and ' + param[i])


#code that creates a list to start with
someList = []
print('Please enter some things you would like to be in the list: ' +
' , or press enter to stop')
while True:
    entry = input()
    if entry == '':
        break
    someList = someList + [entry]

#function call
listfunc(someList)

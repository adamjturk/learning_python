def listfunc(param):
    counter = 1
    for i in range(len(param)):
        if counter < len(param):
            print(param[i] + ', ',end='')
            counter = counter + 1
        else:
            print('and ' + param[i])


someList = []
print('Please enter some things you would like to be in the list: ' +
' , or press enter to stop')
while True:
    entry = input()
    if entry == '':
        break
    someList = someList + [entry]

listfunc(someList)

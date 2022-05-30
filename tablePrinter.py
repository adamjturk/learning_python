#take a list of lists of strings and print them neatly

tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]


#function definition
def printTable(argument):

    measure = 0
    adjust = 0

    #find longest word
    for i in range(len(argument)):
        for k in range(len(argument[i])):
            if len(argument[i][k]) > measure:
                measure = len(argument[i][k])
    
    #make table right adjusted based on longest word
    for i in range(len(argument)):
        for k in range(len(argument[i])):
            if len(argument[i][k]) < measure:
                adjust = measure - len(argument[i][k])
                argument[i][k] = ' ' * adjust + argument[i][k]

    
    #print table
    for i in range(len(argument[0])):
        for k in range(len(argument)):
            print(argument[k][i],end='')
        print('\t')


#function call
printTable(tableData)
chessBoard = {'a8': 'brook','b8':'bknight', 'c8': 'bbishop', 'd8': 'bking',
              'e8': 'bqueen', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
              'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
              'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
              'a1': 'wrook','b1':'wknight', 'c1': 'wbishop', 'd1': 'wking',
              'e1': 'wqueen', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
              'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
              'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn'}


def isValidChessBoard(argument):
    #counter
    bcount = 0
    wcount = 0
    isValid = True

    ##check if each player has 1 king##

    for i in argument.values():
        if i == 'bking':
            bcount += 1
        elif i == 'wking':
            wcount += 1
    if bcount and wcount <= 1:
        print('Both players have at least 1 king')
    else:
        print('There is an incorrect number of king pieces on the board')
        isValid = False
    #reset count
    bcount = 0
    wcount = 0

    ##check if each player has at most 16 pieces##

    #create a list of dictionary values, the names of the pieces
    listValues = []
    listPieces = ['pawn','knight','bishop','rook','king','queen']
    bpawnCount = 0
    wpawnCount = 0

    for i in argument.values():
        listValues = listValues + [str(i)]
    #loop goes through each value to check owner of each piece, checking for piece count
    for i in range(len(listValues)):
        #need to get the first letter of each value, so assign them to a variable
        word = listValues[i]
        #checking the first letter to see if its a black or white piece
        if word[0] == 'b':
            bcount += 1
        elif word[0] == 'w':
            wcount += 1
        #if piece is labeled anything other than w or b, invalidates board
        else:
            print('Invalid color of piece. Must be labeled "w" or "b"')
            isValid = False
    #loop to check for pawn count
    for i in range(len(listValues)):
        word = listValues[i]
        if word[0] == 'b' and word[1] == 'p':
            bpawnCount += 1
        if word[0] == 'w' and word[1] == 'p':
            wpawnCount += 1
    #loop to check piece names
    for i in range(len(listValues)):
        word = listValues[i]
        pieceName = word[1:]
        if pieceName not in listPieces:
            print('Invalid piece name.')
            isValid = False
 
    #checks final count
    if (bcount and wcount <= 16) and (bpawnCount and wpawnCount <= 8):
        print('Valid amount of black and white pieces, including pawns.')
    else:
        print('Invalid number of black or white pieces.')
        isValid = False
    #reset counter
    bcount = 0
    wcount = 0

    ##check if pieces are on valid spaces##
    
    #create a list of keys
    listKeys = []
    #create lists of valid positions on board
    validAlph = ['a','b','c','d','e','f','g','h']
    validNums = ['1','2','3','4','5','6','7','8']
    for i in argument.keys():
        listKeys = listKeys + [i]
    
    #check lists for validity
    for i in range(len(listKeys)):
        pos = listKeys[i]
        if (str(pos[0]) not in validAlph) or (str(pos[1]) not in validNums):
            print('There is a piece in an invalid position.')
            isValid = False
    print('All pieces are in valid positions.')





    #final check, if true, chess board is valid. returns true value
    if isValid:
        return True

print('SUMMARY\n---------')
if(isValidChessBoard(chessBoard)):
    print('--------------\nFINAL RESULT\n--------------')
    print('Chess board is valid.')
else:
    print('--------------\nFINAL RESULT\n--------------')
    print('Chess board is invalid')
    

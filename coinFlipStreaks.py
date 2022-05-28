#Purpose of program: see how many times a streak of 6 heads or tails is flipped
#in 100 coin flips

import random
numberOfStreaks = 0
listOfFlips = []
countH = 0
countT = 0
#conductst the entire experiment a certain number of times
for experimentNumber in range(50):
    #generates list of heads or tails for 100 coin flips:
    for count in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            listOfFlips = listOfFlips + ['H']
        else:
            listOfFlips = listOfFlips + ['T']
    #check for streaks:
    for i in range(len(listOfFlips)):
        #if the list entry is a 'H' for heads, increases heads counter and resets
        #tails counter
        if listOfFlips[i] == 'H':
            countH += 1
            countT = 0
            #after counters update, if heads counter is at 6, adds a streak to 
            #numberOfStreaks
            if countH == 6:
                numberOfStreaks += 1
        #does the same thing for tails that heads did above ^
        else:
            countH = 0
            countT += 1
            if countT == 6:
                numberOfStreaks += 1

#print total number of streaks (6 heads or tails in a row)
print('Total streaks: ' + str(numberOfStreaks))


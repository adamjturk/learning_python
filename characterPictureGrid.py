#This program takes an image from a list of lists, and prints a different 
#layout to display another image

#grid initialization 
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

#nested for loops to achieve new print
for i in range(len(grid[0])):
    for slot in range(len(grid)):
        print(grid[slot][i],end='')
    #prints new line at the end of each new row
    print(end='\n')

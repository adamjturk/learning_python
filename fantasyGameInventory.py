##Purpose of program##
#Use a dictionary to store items in a fantasy game character's inventory, then
#write a function that displays the inventory in a proper manner
#write another function that takes a dictionary and list as parameters,
#and adds the contents of the list to the dictionary

#dictionary
inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

#function that displays inventory
def displayInventory(argument):
    print('Inventory:')
    totalItems = 0
    for k,v in argument.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total number of items: ' + str(totalItems))

print('----BEFORE----')
displayInventory(inventory)

#function that adds list to dictionary
def addToInventory(inventory, addedItems):
    #search in the list of new items to see if they're in the dict or not 
    for i in range(len(addedItems)):
        #if they are, update the new count
        if addedItems[i] in inventory.keys():
            currentStock = inventory.get(addedItems[i],0)
            inventory[addedItems[i]] = currentStock + 1
        #if they aren't, add item with new count
        elif addedItems[i] not in inventory.keys():
            inventory.setdefault(addedItems[i], 1)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragonLoot)
print('----AFTER----')
displayInventory(inventory)
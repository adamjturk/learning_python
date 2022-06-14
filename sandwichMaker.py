#This program uses pyinputplus for input validation to create a sandwich maker

import pyinputplus as pyip

#variables to use as prompts
breadPrompt = 'What kind of bread would you like?\n'
proteinPrompt = 'What kind of protein would you like?\n'
cheesePrompt = 'Would you like cheese?\n'
cheeseTypePrompt = 'What kind of cheese would you like?\n'

#dictionary used as data structure to store all prices
prices = {'wheat': 1.2, 'white': 1, 'sourdough': 1.5, 'chicken': 2, 'tofu': 2.5, 
          'turkey': 1.5, 'ham': 1.5, 'cheddar': 1, 'swiss': 1.2, 'mozzarella': 1.5,
          'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tomato': 1}

#will be used to calculate total amount at the end
total = 0

print('Welcome to the sandwich maker')
#get bread
breadType = pyip.inputMenu(['wheat','white','sourdough'],breadPrompt)
total += prices[breadType]

#get protein
proteinType = pyip.inputMenu(['chicken','turkey','ham','tofu'])
total += prices[proteinType]

#get cheese or no cheese
cheese = pyip.inputYesNo(cheesePrompt)
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar','swiss','mozzarella'], cheeseTypePrompt)
    total += prices[cheeseType]

#get toppings
mayo = pyip.inputYesNo('Would you like mayo?\n')
if mayo == 'yes':
    total += prices['mayo']
mustard = pyip.inputYesNo('Would you like mustard?\n')
if mustard == 'yes':
    total += prices['mustard']
lettuce = pyip.inputYesNo('Would you like lettuce?\n')
if lettuce == 'yes':
    total += prices['lettuce']
tomato = pyip.inputYesNo('Would you like tomato?\n')
if tomato == 'yes':
    total += prices['tomato']


#final step, must choose at least 1 sandwich
numberSand = pyip.inputInt(prompt='How many sandwiches would you like?\n', min=1)
print('Your total is $' + str((total * numberSand)))




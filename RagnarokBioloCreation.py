# Ragnarok Online: Biolo potion creation calculator
# Current Potions available: Greater Plant Bottle (for very personal uses)

# Potion Functions
def greaterPlantBottle(amount):
    global potionName
    potionName = 'Greater Plant Bottle'
    global itemsNeeded
    itemsNeeded = {'Plant Bottle': 10 * amount, 'Mandragora Flowerpot': 5 * amount, 'Thorn Plant Seed': 2 *amount, 'Blood Sucker Plant Seed' : 2 * amount, 'Beaker': 1 * amount}
    return itemsNeeded

def plantBottle(amount):
    global potionName
    potionName = 'Plant Bottle'
    global itemsNeeded
    itemsNeeded = {'Medicine Bowl': amount, 'Empty Bottle': amount, 'Maneater Blossom': amount * 2}
    return itemsNeeded

# Table function
def itemsTable():
    if creationAmount == 1:
        print('\n To create ' + str(creationAmount), '' + potionName, ' you will need: \n')
        for k, v in itemsNeeded.items():
            print(k.ljust(30, '.') + str(v).rjust(4))
    else:
        print('\n To create ' + str(creationAmount), '' + potionName + 's', 'you will need: \n')
        for k, v in itemsNeeded.items():
            print(k.ljust(30, '.') + str(v).rjust(4))

# Results Function
def results():
    if 'Plant Bottle' in itemsNeeded:
        itemsTable()
        global creationAmount
        creationAmount = int(itemsNeeded.get('Plant Bottle'))
        plantBottle(itemsNeeded.get('Plant Bottle'))
        itemsTable()
    else:
        itemsTable()


# What potion you want to make \\ this is for when I add more options \\ currently useless
potionName = ''

# Skill check + how many
print('What level is your Bionic Pharmacy Skill? (1-5)')
skillLevel = int(input())
if skillLevel == 0:
    print('You need at least Bionic Pharmacy lv 1 to create Biolo potions.')
elif skillLevel > 5:
    print('Your skill level has been set to the maximum (5)')
    skillLevel == 5
else:
    print('Your skill level has been set to ' + str(skillLevel))
skillLevel = skillLevel + 10
print('How many potions you want to create?')
creationAmount = int(int(input())/skillLevel) 

# add option to restart if wanted
# add expections handling

# Redirect to the Greater Plant Bottle branch
itemsNeeded = {}
greaterPlantBottle(creationAmount)

# Results // changing the amount for aesthetic purposes
creationAmount = creationAmount * skillLevel
results()

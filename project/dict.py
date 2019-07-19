# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
#     print('Enter a name: (blank to quit')
#     name = input()
#     if name == '':
#         break;
    
#     if  name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


import pprint
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')

message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message: 
    count.setdefault(character, 0) 
    count[character] = count[character] + 1
pprint.pprint(count)


theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# printBoard(theBoard)   
     
#pprint.pprint(theBoard)  

#def printBoard(board):
 #   print(board['top-L'] + '|' + board['top-M'] + '|'

# printfBoard(theBoard)

allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12}, 
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
    }

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items:" + str(item_total))

displayInventory(stuff)


def addToInventory(inventory, addedItems):
    dicts = {}
    for idx in range(len(addedItems)):
        dicts.setdefault(addedItems[idx],inventory.get(addedItems[idx], 0))
    return dicts

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
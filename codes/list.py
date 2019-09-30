import copy
# catNames = []
# while True:
#     print("enter the name of cat "+ str(len(catNames)+1) + 'Or enter nothing to stoop.')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]
# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

# spam = ['hello', 'hi', 'howdy', 'heyas']
# print(spam.index('hello'))
# [1, 2, 3] + ['A', 'B', 'C']

# spam.insert(1,'chicken')
# print(spam)

# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)

# name = 'Zophie a cat'
# newName = name[0:7] + 'the' + name[8:12]

# print(tuple(['cat', 'dog', 5]))
# print(list(('cat', 'dog', 5)))

# spam = ['A', 'B', 'C', 'D']
# cheese = copy.copy(spam)
# cheese[1] = 42
# print(cheese)
# print(spam)


# def dotcharacter(cDots):
#    # copys = copy.copy(cDots)
#    # cDots.insert(len(cDots)-1,'and')
#     lastObj = cDots[-1]
#     tmp = 'and ' + lastObj 
#     del cDots[len(cDots)-1]
#     cDots.append(tmp)
#     return cDots 

# spam = ['apples', 'bananas', 'tofu', 'cats']
# print(dotcharacter(spam))

def chacterNet():
    grid = [
        ['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]
    row = len(grid)
    col = len(grid[0])
    for i in range(col):
        for j in range(row):
            print(grid[j][i],end='')
        print('')    

chacterNet()
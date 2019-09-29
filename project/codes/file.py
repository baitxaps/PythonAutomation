#! /usr/bin/env python3

import os
import shelve
import pyperclip
import sys
import pprint
import myCats
import random

print(os.path.join('usr', 'bin', 'spam'))

myfile = ['account.txt', 'details.cvs', 'invite.docx']
for filename in myfile:
    print(os.path.join('usr/bin/spam', filename))

# 当前工作目录
print(os.getcwd())

# 利用 os.chdir()改变它
os.chdir('/Users/jishuyanfa-ios/Desktop')
print(os.getcwd())

# 创建新文件夹
# os.makedirs('/Users/jishuyanfa-ios/Desktop/pyfolder')

print(os.path.abspath('.'))
print(os.path.abspath('./Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

# os.path.relpath(path, start):
# 将返回从 start 路径到 path 的相对路径的字符串。 如果没有提供 start，就使用当前工作目录作为开始路径
print(os.path.relpath('/Users/jishuyanfa-ios/Desktop', '/Users/jishuyanfa-ios'))
print(os.path.relpath('/Users/jishuyanfa-ios', '/Applications/Microsoft'))

path = '/Applications/Microsoft'
# 返回一个字符串，它包含path参数中最后一个斜杠 之前的所有内容
print(os.path.basename(path))
# 将返回一个字符串，它包含 path 参数 中最后一个斜杠之后的所有内容
print(os.path.dirname(path))

# 获得这两个字符串的元组:('/Applications', 'Xcode.app')
calcFilePath = '/Applications/Xcode.app'
print(os.path.split(calcFilePath))

tuples = (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
print(tuples)

print('/usr/bin'.split(os.path.sep))


#查看文件大小和文件夹内容
sizes = os.path.getsize(calcFilePath)
print(sizes)
# 调用 os.listdir(path)将返回文件名字符串的列表，包含 path 参数中的每个文件
# (请注意，这个函数在 os 模块中，而不是 os.path)。
datas = os.listdir('/Applications/')
print(datas)


def totalPathSize(path):
    totalSize = 0
    for filename in os.listdir(path):
        totalSize = totalSize + os.path.getsize(os.path.join(path, filename))
    print(totalSize)


totalPathSize('/Applications/')

#参数所指的文件或文件夹存在
existsPath = os.path.exists(calcFilePath)
print(existsPath)

#参数存在，并且是一个文件
existsFile = os.path.isfile(calcFilePath)
print(existsFile)

#参数存在，并且是一个文件夹
existsDir = os.path.isdir(calcFilePath)
print(existsDir)

# 用open()函数打开文件
helloFile = open('/Users/jishuyanfa-ios/desktop/vcCode/py.txt', 'r')
#helloCount = helloFile.read()
#print(helloCount)
# 从该文件取得一个字符串的列表。列表中的 每个字符串就是文本中的每一行
content = helloFile.readlines()
helloFile.close()
print(content)

writeTest = open('/Users/jishuyanfa-ios/desktop/vcCode/test.txt', 'a')
writeTest.write("hello,test!\n")
writeTest.close()
readTest = open('/Users/jishuyanfa-ios/desktop/vcCode/test.txt')
content = readTest.read()
readTest.close()
print(content)

shelfFile = shelve.open('/Users/jishuyanfa-ios/desktop/vcCode/test.data')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('/Users/jishuyanfa-ios/desktop/vcCode/test.data')
type(shelfFile)
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
print(shelfFile['cats'])
shelfFile.close()

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])

'''
project 1

'''


def quizFuntion():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
                'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
                'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 
                'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 
                'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 
                'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
                'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
                'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
                'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
                'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    # Generate 35 quiz files.
    for quizNum in range(35):
        # TODO: Create the quiz and answer key files.
        quizFile = open('/Users/jishuyanfa-ios/Desktop/vcCode/quize/capitalsquiz%s.txt' % (quizNum + 1), 'w')
        answerKeyFile = open('/Users/jishuyanfa-ios/Desktop/vcCode/quize/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
        # TODO: Write out the header for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        # TODO: Shuffle the order of the states.
        # 利用 random.shuffle()函 数，创建了美国州名的随机列表
        states = list(capitals.keys())
        random.shuffle(states)

        # TODO: Loop through all 50 states, making a question for each.
        for questionNum in range(50):
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers, 3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write the question and the answer options to the quiz file.
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
        
            # Write the answer key to a file.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

        quizFile.close()
        answerKeyFile.close()


quizFuntion()      



'''
project 2

'''

mcbShelf = shelve.open('/Users/jishuyanfa-ios/desktop/vcCode/mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
# TODO: List keywords and load content.

mcbShelf.close()



# 1.相对路径是相对于当前工作目录。
# 2.绝对路径从根文件夹开始，诸如/或 C:\。
# 3.os.getcwd() 函数返回当前工作目录。os.chdir() 函数改变当前工作目录。 
# 4.文件夹. 是当前文件夹，.. 是父文件夹。
# 5.C:\bacon\eggs 是目录名，而 spam.txt 是基本名称。
# 6.字符串 'r' 对应读模式，'w' 对应写模式，'a' 对应添加模式。 
# 7.已有的文件用写模式打开，原有内容会被删除并完全覆写。
# 8.read() 方法将文件的全部内容作为一个字符串返回。readlines() 返回一个字
# 符串列表，其中每个字符串是文件内容中的一行。
# 9.shelf 值类似字典值，它有键和值，以及 keys() 和 values() 方法，类似于同名 的字典方法。
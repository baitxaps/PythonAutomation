#! /usr/bin/env python3
# coding: utf-8

import pyautogui
import time
import pyperclip

def pyautoguiTest():
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    print(pyautogui.size())
    width, height = pyautogui.size()

    # for i in range(10):
    #     pyautogui.moveTo(100, 100, duration=0.25) 
    #     pyautogui.moveTo(200, 100, duration=0.25) 
    #     pyautogui.moveTo(200, 200, duration=0.25) 
    #     pyautogui.moveTo(100, 200, duration=0.25)
        # pyautogui.moveRel(100, 0, duration=0.25) 
        # pyautogui.moveRel(0, 100, duration=0.25) 
        # pyautogui.moveRel(-100, 0, duration=0.25) 
        # pyautogui.moveRel(0, -100, duration=0.25)

    s = pyautogui.position()
    e = pyautogui.position()
    print(s,e)

   # pyautogui.scroll(200)
    numbers = ''
    for i in range(200):
        numbers = numbers + str(i) + '\n'
    pyperclip.copy(numbers)     #剪贴板中将 保存 200 行数字 
    #time.sleep(5); pyautogui.scroll(100)

    #获取屏幕快照
    im = pyautogui.screenshot()
    im.getpixel((0, 0))
    im.getpixel((50, 200)) # return RGB:(130, 135, 144)
    pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

    # 图像识别
    print(pyautogui.locateOnScreen('drawing.png'))
    list(pyautogui.locateAllOnScreen('drawing.png'))
    pyautogui.center((643, 745, 70, 29))
    pyautogui.click((678, 759))

    #控制键盘
    pyautogui.click(100, 100); pyautogui.typewrite('Hello world!',0.25)

    # 键名
    pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
    pyautogui.click(100, 100)
    pyautogui.typewrite('In IDLE, ctrl-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('ctrl', '3')

#pyautoguiTest()    


def mouseNow():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

            pixelColor = pyautogui.screenshot().getpixel((x, y))
            positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
            positionStr += ', ' + str(pixelColor[1]).rjust(3)
            positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'

            print(positionStr, end='')
            
            #print(positionStr)
            #print(len(positionStr), end='', flush=True)
            print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone.')


#mouseNow() 


def spiralDraw():
    #pyautogui.click(10, 5)
    time.sleep(5)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2) # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2) # move down
        pyautogui.dragRel(-distance, 0, duration=0.2) # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2) # move up



#spiralDraw()    


def formFiller():
    nameField = (648, 319)
    submitButton = (651, 817)
    submitButtonColor = (75, 141, 249)
    submitAnotherLink = (760, 224)
    formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]
    pyautogui.PAUSE = 0.5

    for person in formData:
    # Give the user a chance to kill the script.
        print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<') 
        time.sleep(5)
        # Wait until the form page has loaded.
        while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
            time.sleep(0.5)
            print('Entering %s info...' % (person['name']))
            pyautogui.click(nameField[0], nameField[1])
            # Fill out the Name field.
            pyautogui.typewrite(person['name'] + '\t')
            # Fill out the Greatest Fear(s) field.
            pyautogui.typewrite(person['fear'] + '\t')

            # Fill out the Source of Wizard Powers field.
            if person['source'] == 'wand':
                pyautogui.typewrite(['down', '\t'])
            elif person['source'] == 'amulet':
                pyautogui.typewrite(['down', 'down','\t'])
            elif person['source'] == 'crystal ball':    
                pyautogui.typewrite(['down', 'down','down', '\t'])
            elif person['source'] == 'money':
                pyautogui.typewrite(['down', 'down','down', 'down', '\t'])

            # Fill out the RoboCop field.
            if person['robocop'] == 1:    
                pyautogui.typewrite([' ', '\t'])
            elif person['robocop'] == 2:
                pyautogui.typewrite(['right', '\t'])
            elif person['robocop'] == 3:
                 pyautogui.typewrite(['right', 'right', '\t'])   
            elif person['robocop'] == 4:
                 pyautogui.typewrite(['right', 'right', 'right', '\t'])
            elif person['robocop'] == 5:
                 pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')
    # Click Submit.
    pyautogui.press('enter')
    # Wait until form page has loaded. print('Clicked Submit.') 
    time.sleep(5)
    #  Click the Submit another response link. 
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])


formFiller()
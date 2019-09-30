#! /usr/bin/env python3
# coding: utf-8

import time
import datetime

import requests, os, bs4, threading

import subprocess


print(time.time())
print(datetime.datetime.now())
# datetime.datetime(2019, 9, 27, 11, 10, 49, 55, 53)
# dt = datetime.datetime(2019, 9, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)


def calcProd():
    product = 1
    for i in range(1, 100):
        product = product * i
    return product


# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))


# print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
# input()
# print('Started.')
# startTime = time.time()
# lastTime = startTime
# lapNum = 1
# try:
#     while True:
#         input()
#         lapTime = round(time.time() - lastTime, 2)
#         totalTime = round(time.time() - startTime, 2)
#         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
#         lapNum += 1
#         lastTime = time.time()  # reset the last lap time
# except KeyboardInterrupt:
#     print('\nDone.')

def pauseDate(): 
    halloween2019 = datetime.datetime(2019, 8, 31, 0, 0, 0)
    while datetime.datetime.now() < halloween2019:
        time.sleep(1)
        print(datetime.datetime.now())

    oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
    oct21st.strftime('%Y/%m/%d %H:%M:%S')
    print(oct21st)
    print(oct21st.strftime('%I:%M %p'))
    print(oct21st.strftime("%B of '%y"))

    #
    datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
    datetime.datetime(2015, 10, 21, 0, 0)
    print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
    datetime.datetime(2015, 10, 21, 16, 29)
    print(datetime.datetime.strptime("October of '15", "%B of '%y"))
    datetime.datetime(2015, 10, 1, 0, 0)
    print(datetime.datetime.strptime("November of '63", "%B of '%y"))
    print(datetime.datetime(2063, 11, 1, 0, 0))


#pauseDate() 


def takeANap():
    print('Start of program.')
    time.sleep(5)
    print('Wake up!')


#threadObj = threading.Thread(target=takeANap)
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# threadObj.start()
# print('End of program.')

# 多线程 XKCD 下载程序
def downloadXkcd(startComic, endComic):
    # 行创建了一个目录来保存漫画
    os.makedirs('xkcd', exist_ok=True)
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        #Beautiful Soup查看每一页的 HTML
        soup = bs4.BeautifulSoup(res.text)
        #找到漫画图像
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            print('Downloading image %s...' % (comicUrl))
            imageUrl = "http:" + comicUrl
          
            res = requests.get(imageUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# downloadThreads = []
# for i in range(0, 1400, 100):
#     downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
#     downloadThreads.append(downloadThread)
#     downloadThread.start()
# # 等待所有线程结束
# for downloadThread in downloadThreads:
#     downloadThread.join()
# print('Done.')




def subprocessFunction():
    fileObj = open('/Users/jishuyanfa-ios/desktop/vcCode/test.txt', 'w')
    fileObj.write('Hello world!')
    fileObj.close()
    subprocess.Popen(['open', '/Applications/Calculator.app/'])


#subprocessFunction()


# 倒计时
def countdown():
    timeLeft = 3
    while timeLeft > 0:
        print(timeLeft, end='')
        time.sleep(1)
        timeLeft = timeLeft - 1
    subprocess.Popen(['open', '/Users/jishuyanfa-ios/Desktop/vcCode/automate_online-materials/alarm.wav'])


countdown()    
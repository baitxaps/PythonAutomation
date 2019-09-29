#! /usr/bin/env python3
# coding: utf-8

import time
import datetime


def calcProd():
    # Calculate the product of the first 100,000 numbers. 
    product = 1
    for i in range(1, 10):
        product = product * i
        time.sleep(1)
    return product


# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))


def Display():
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()
    print('Started.')
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        print('\nDone.')


#Display()



#! /usr/bin/env python3
# coding: utf-8



import traceback
# 使用日志模块
import logging


# 取得反向跟踪的字符串
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
        print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)


# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An exception happened: ' + str(err))



def tryTest():
    try:
        raise Exception('This is the error message.')
    except Exception as exc:
        print(exc)
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')


# 断言
# 你可以禁用 Python 程序中的 assert 语句，从而稍稍提高性能。
# 从终端窗口运行 Python 时，在 python 或 python3 之后和.py 文件之前加上-O 开关。这将运行程序的 优化版本，跳过断言检查。



def assertTest(podBayDoorStatus):
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'


assertTest("open")


#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


def loggingTest(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


logging.debug(loggingTest(5))
logging.debug('End of program')

# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to recover!')



# 1.assert(spam >= 10, 'The spam variable is less than 10.')
# 2.assert(eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!') 或 assert(eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!')
# 3.assert(False, 'This assertion always triggers.')
# 4.为了能调用 logging.debug()，必须在程序开始时加入以下两行:
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# 5.为了能利用 logging.debug() 将日志消息发送到文件 programLog.txt 中，必须 在程序开始时加入以下两行:
# import logging
# >>> logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# 6.DEBUG、INFO、WARNING、ERROR 和 CRITICAL
# 7.logging.disable (logging.CRITICAL)
# 8.可以禁用日志消息，不必删除日志函数调用。可以选择禁用低级别日志消息。可以创建日志消息。日志消息提供了时间戳。
# 9.Step 按扭让调试器进入函数调用。Over 按钮将快速执行函数调用，不会单
# 步进入其中。Out 按钮将快速执行余下的代码，直到走出当前所处的函数
# 10.在点击 Go 后，调试器将在程序末尾或断点处停止
# 11.断点设在一行代码上，在程序执到到达该行时，它导致调试器暂停
# 12.要在 IDLE 中设置断点，就在代码行上单击右键，从弹出菜单中选择 Set Breakpoint

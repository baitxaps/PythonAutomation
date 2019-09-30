#! /usr/bin/env python3
# coding: utf-8

import webbrowser
import sys
import os
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import logging # 使用日志模块

#webbrowser.open('http://inventwithpython.com/')

# if len(sys.argv) > 1:
# # Get address from command line.
#      address = ' '.join(sys.argv[1:])
# else:
#     #address = pyperclip.paste()
#     pass
#webbrowser.open('https://www.google.com/maps/place/' + address)


def requestWeb():
    #logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    #res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    res.status_code == requests.codes.ok

    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()

    # logging.debug(len(res.text))
    # logging.debug(res.text[:250])


'''
<!-- This is the example.html example file. -->

<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
'''


def htmlParsing(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    noStarchSoup = bs4.BeautifulSoup(res.text)
    type(noStarchSoup)

#htmlParsing('http://nostarch.com')


def localHtmlParsing():
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile.read())
    elems = exampleSoup.select('#author')

    try:
        print(type(elems))
        print(len(elems))
        print(type(elems[0]))
        print(elems[0].getText())
        print(str(elems[0]))
        print(elems[0].attrs)

        pElems = exampleSoup.select('p')
        print(str(pElems[0]))
        print(pElems[0].getText())
        print(pElems[1].getText())
        print(pElems[2].getText())

    except Exception as exc:
        print(exc)
    # logging.debug(type(elems))
    # logging.debug(lem(elems))
    # logging.debug(type(elems[0]))
    # logging.debug(elems[0].getText())
    # logging.debug(str(elems[0]))
    # logging.debug(elems[0].attrs)
#localHtmlParsing()


def parsingTag():
    soup = bs4.BeautifulSoup(open('example.html'))
    spanElem = soup.select('span')[0]
    print(str(spanElem))

    print(spanElem.get('id'))

    eq = spanElem.get('some_nonexitent_addr') is None
    print(eq)
    print(spanElem.attrs)

#parsingTag()


'''
<a href="/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;
cad=rja&amp;uact=8&amp;ved=0CCgQFjAA&amp;url=http%3A%2F%2Fwww.crumm
y.com%2Fsoftware%2FBeautifulSoup%2F&amp;ei=LHBVU_XDD9KVyAShmYDwCw &amp;
usg=AFQjCNHAxwplurFOBqg5cehWQEVKi-TuLQ&amp;sig2=sdZu6WVlBlV SDrwhtworMA"
onmousedown="return rwt(this,'','','','1','AFQjCNH AxwplurFOBqg5cehWQEVKi- TuLQ',
'sdZu6WVlBlVSDrwhtworMA','0CCgQFjAA','','',event)"
data-href="http://www. crummy.com/software/BeautifulSoup/">
<em> BeautifulSoup</em>: We called him Tortoise because he taught us.</a>
'''

'''
project
“I’m Feeling Lucky”Google 查找
'''


def googleParse():
    print("googling...")
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text)

    # Open a browser tab for each result.
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))

#googleParse()


'''
project
下载所有 XKCD 漫画
'''


def downloadXKCDCartoon():
    url = 'http://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
    while not url.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

            # iter_content()方法在循环的每次迭代中，返回一段内容。每一段都是 bytes 数据
            # 类型，你需要指定一段包含多少字节。10 万字节通常是不错的选择，所以将 100000 作为参数传递给 iter_content()

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # Get the Prev button's url.
        # Get the Prev button's url.
        # soup.select('input[type="button"]') 所有名为<input>, 并有一个ype属性其值为button的元素
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    print('Done')

#downloadXKCDCartoon()


'''
project
用 selenium 模块控制浏览器
爬虫之--mac安装selenium遇到的坑:https://www.jianshu.com/p/783ad3108d4e

'''


def selenium():
    browser = webdriver.Firefox()
    type(browser)
    browser.get('http://inventwithpython.com')
    try:
        elem = browser.find_element_by_class_name('jumbotron')
        print('Foun <%s> element with that class name!' % (elem.tag_name))
    except Exception as exc:
        print('Was not able to find an element with that name. %s' % (exc))

    # linkElem = browser.find_element_by_link_text('Buy Print/Ebook Bundle')
    # type(linkElem)
    # linkElem.click()
    # cmd = browser.find_element_by_id('cmd')
    # cmd.send_keys(Keys.ENTER)
    #passwordElem = browser.find_element_by_id('Passwd')
    #passwordElem.send_keys('12345')
    #passwordElem.submit()


selenium()


def submitEvent():
    # browser = webdriver.Firefox()
    # browser.get('http://gmail.com')
    # emailElem = browser.find_element_by_id('Email')
    # emailElem.send_keys('not_my_real_email@gmail.com')
    # passwordElem = browser.find_element_by_id('Passwd')
    # passwordElem.send_keys('12345')
    # passwordElem.submit()

    browser = webdriver.Firefox()
    browser.get('http://nostarch.com')
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)  # scrolls to bottom
    htmlElem.send_keys(Keys.HOME)  # scrolls to top

#submitEvent()




'''
1.简单描述 webbrowser、requests、BeautifulSoup 和 selenium 模块之间的不同。
2.requests.get()返回哪种类型的对象?如何以字符串的方式访问下载的内容?
3.哪个 Requests 方法检查下载是否成功?
4.如何取得 Requests 响应的 HTTP 状态码?
5.如何将 Requests 响应保存到文件?
6.要打开浏览器的开发者工具，快捷键是什么?
7.在开发者工具中，如何查看页面上特定元素的 HTML?
8.要找到 id 属性为 main 的元素，CSS 选择器的字符串是什么?
9.要找到 CSS 类为 highlight 的元素，CSS 选择器的字符串是什么?
10.要找到一个<div>元素中所有的<div>元素，CSS 选择器的字符串是什么?
11.要找到一个<button>元素，它的 value 属性被设置为 favorite，CSS 选择器
的字符串是什么?
12.假定你有一个Beautiful Soup的Tag对象保存在变量spam中，针对的元素是
<div>Hello world!</div>。如何从这个 Tag 对象中取得字符串'Hello world!'?
13.如何将一个 Beautiful Soup 的 Tag 对象的所有属性保存到变量 linkElem 中?
14.运行 import selenium 没有效果。如何正确地导入 selenium 模块?
15.find_element_*和 find_elements_*方法之间的区别是什么?
16.Selenium 的 WebElement 对象有哪些方法来模拟鼠标点击和键盘击键?
17.你可以在 Submit 按钮的 WebElement 对象上调用 send_keys(Keys.ENTER)，但
利用 selenium，还有什么更容易的方法提交表单?
18.利用 selenium 如何模拟点击浏览器的“前进”、“返回”和“刷新”按钮?
'''

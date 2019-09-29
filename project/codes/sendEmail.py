#!/usr/bin/env python3
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.yeah.net'
browser = webdriver.Firefox()  # 打开浏览器
browser.get(url)
time.sleep(2)

iframe = browser.find_element_by_tag_name("iframe")
browser.switch_to.frame(iframe)

emailElem = browser.find_element_by_name('email')
emailElem.send_keys('not-a-real-email-address')  # 调用send_keys()方法填写表单

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys('****')

loginElem = browser.find_element_by_id('dologin')
loginElem.click()  # 模拟鼠标点击登录
time.sleep(2)  #
browser.switch_to.default_content()

writeElem = browser.find_element_by_id('_mail_component_23_23')
writeElem.click()  #模拟鼠标点击登录
time.sleep(2)

recipientElem = browser.find_element_by_class_name('nui-editableAddr-ipt')
recipientElem.send_keys('bawfnhaps@163.com')
subjectElem = browser.find_element_by_xpath("//*[@class='nui-ipt-input'and @type = 'text' and @tabindex = '1']")
subjectElem.send_keys('Hello!')

mainbodyFrame = browser.find_element_by_xpath("//iframe[contains(@class,'APP-editor-iframe')]")
browser.switch_to.frame(mainbodyFrame)
mainbodyElem = browser.find_element_by_class_name('nui-scroll')
mainbodyElem.send_keys('Hello! World!')
browser.switch_to.default_content()

sendElem = browser.find_elements_by_class_name('nui-btn-text')[2]
sendElem.click()
time.sleep(5)
browser.quit()

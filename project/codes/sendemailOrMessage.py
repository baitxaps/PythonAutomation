#! /usr/bin/env python3
# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def sendemail():
    sender = 'baitxaps@126.com'
    receiver = '331681151@qq.com'
    subject = '放假通知'
    smtpserver = 'smtp.126.com'
    username = 'baitxaps@126.com'
    password = ' '

    msg = MIMEText('大家关好窗户', 'plain', 'utf-8') # 中文需参数‘utf-8'，单字节字符不需要
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'baitxaps@126.com'
    msg['To'] = "331681151@qq.com"

    #smtpObj = smtplib.SMTP('smtp.126.com', 587)
    smtpObj = smtplib.SMTP_SSL(smtpserver, 465)
    type(smtpObj)
    print(smtpObj.ehlo())
#  smtpObj.starttls()
    print(smtpObj.login(username, password))
    smtpObj.sendmail(sender, [receiver], msg.as_string())
    print(smtpObj.quit())


# sendemail()


# def receiveImap():
#     imapObj = imapclient.IMAPClient('imap.126.com', ssl=True)
#     print(imapObj.login('baitxaps@126.com', ''))
#     imapObj.select_folder('INBOX', readonly=True)
#     UIDs = imapObj.search(['SINCE 05-Jul-2017'])
#     print(UIDs)

#     rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
#     message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
#     print(message.get_subject())
#     message.get_addresses('from')
#     message.get_addresses('to')
#     message.get_addresses('cc')
#     message.get_addresses('bcc')
#     #message.text_part != None
#     message.text_part.get_payload().decode(message.text_part.charset)
#     #message.html_part != None
#     message.html_part.get_payload().decode(message.html_part.charset)
#     imapObj.logout()


# receiveImap()

# 返回邮箱中的最新邮件
def get_email_content():
  
    username = '邮箱账号'
    password = '邮箱密码（客户端授权码非登陆密码）'
 
# 邮件服务器地址,以下为网易邮箱
    pop3_server = 'pop.126.com'

    # 开始连接到服务器
    server = poplib.POP3(pop3_server)

    # 打开或者关闭调试信息，为打开，会在控制台打印客户端与服务器的交互信息
    server.set_debuglevel(1)

    # 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    print(server.getwelcome().decode('utf8'))

    # 开始进行身份验证
    server.user(username)
    server.pass_(password)

    # 返回邮件总数目和占用服务器的空间大小（字节数）， 通过stat()方法即可
    email_num, email_size = server.stat()
    print("消息的数量: {0}, 消息的总大小: {1}".format(email_num, email_size))

    # 使用list()返回所有邮件的编号，默认为字节类型的串
    rsp, msg_list, rsp_siz = server.list()
    print("服务器的响应: {0},\n消息列表： {1},\n返回消息的大小： {2}".format(rsp, msg_list, rsp_siz))

    print('邮件总数： {}'.format(len(msg_list)))

    # 下面单纯获取最新的一封邮件
    total_mail_numbers = len(msg_list)
    rsp, msglines, msgsiz = server.retr(total_mail_numbers)
    #print("服务器的响应: {0},\n原始邮件内容： {1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))

    msg_content = b'\r\n'.join(msglines).decode('gbk')

    msg = Parser().parsestr(text=msg_content)
    print('解码后的邮件信息:\n{}'.format(msg))

    # 关闭与服务器的连接，释放资源
    server.close()
    return msg

# 解析邮件主题
def parser_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    print('邮件主题： {0}'.format(value))
    return value

# 解析邮件来源
def parser_address(msg):
    hdr, addr = parseaddr(msg['From'])
    # name 发送人邮箱名称， addr 发送人邮箱地址
    name, charset = decode_header(hdr)[0]
    if charset:
        name = name.decode(charset)
    print('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))

# 解析邮件内容
def parser_content(msg):
    content = msg.get_payload()

    # 文本信息
    #content_charset = content[0] # 获取编码格式
    content_charset = content[0].get_content_charset() # 获取编码格式

    text = content[0].as_string().split('base64')[-1]
    text_content = base64.b64decode(text).decode(content_charset) # base64解码

    # 添加了HTML代码的信息
    content_charset = content[1].get_content_charset()
    text = content[1].as_string().split('base64')[-1]
    html_content = base64.b64decode(text).decode(content_charset)

    print('文本信息: {0}\n添加了HTML代码的信息: {1}'.format(text_content, html_content))


if __name__ == '__main__':
    # 返回解码的邮件详情
    msg = get_email_content()
    # 解析邮件主题
    parser_subject(msg)
    # 解析发件人详情
    parser_address(msg)
    # 解析内容
    parser_content(msg)

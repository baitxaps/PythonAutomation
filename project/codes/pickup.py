#! python
# coding: utf-8
##创建一个疯狂填词（Mad Libs）程序，它将读入文本文件，并让用户在该文本文件中出现ADJECTIVE、NOUN、ADVERB 或VERB 等单词的地方，加上他们自
#己的文本。例如，一个文本文件可能看起来像这样：
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN wasunaffected by these events.
#程序将找到这些出现的单词，并提示用户取代它们。
#Enter an adjective:
#silly
#Enter a noun:
#chandelier
#Enter a verb:
#screamed
#Enter a noun:
#pickup truck
#以下的文本文件将被创建：
#The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.
#结果应该打印到屏幕上，并保存为一个新的文本文件。


# 程序代码如下：
import re
f1 = open('words.txt','r')
strf1 = f1.read()
print("原文件内容为：")
print(strf1)
#将字符串以空格为分隔符生成一个列表
strf1_list = strf1.split()
#去除列表中元素结尾的逗号和句号，并获取有逗号和句号的元素索引和值保存在一个字典中
i = 0
j = {}
for strs in strf1_list:
    if '.' in strs or ',' in strs:
        j[i]=strs
        strf1_list[i] = strs[:-1]
    i += 1
print("打印出没有句号和逗号的列表")
print(strf1_list)
print("打印出有句号有逗号的元素索引和值")
print(j)
f1.close()
# 由于原文件需要被替换的单词都是大写的英文单词
#  使用正则表达式找出原文件中所有将被替换的单词
replist = re.findall(r'[A-Z]{2,}',strf1)
print("原文件中将被替换的单词为：")
print(replist)
for rep in replist:
    #元音字母开头的字母提示信息不一样
    if rep[0] in 'AEIOU':
        inputstr = input("Enter an %s " % rep)
    else:
        inputstr = input("Enter a %s " % rep)
    print(inputstr)
    # 先将替换后的单词插入到原列表对应的位置
    strf1_list.insert(strf1_list.index(rep),inputstr)
    # 再将原先的单词删除
    strf1_list.remove(rep)
#将上面去除逗号或句号的元素后面将逗号或句号添加回去，根据j字典可以准确找到结尾有逗号或句号的元素
for key,value in j.items():
   strf1_list[key] = str(strf1_list[key]) + str(value[-1])
# 将列表转换为字符串
newstr = ' '.join(strf1_list)
print("替换后的内容为：") #
print(newstr)
# 将新的字符串写入文件b.txt中，并打印到屏幕
f2 = open('b.txt','w+')
f2.write(newstr)
f2.close()
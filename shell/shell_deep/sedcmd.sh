#! /bin/bash
# sed 入门
#流编辑 ，替换是最主要的功能

# 基本语法：sed ‘样式命令’ 文件
# 样式：正则表达式、数据行的范围
# 命令:d(用来删除指定样式的行),p(显示出来),s(替换)
# 选项:-i(对文件的内容进行修改),-n

#boat.txt：
#Row,row,row your boat
#Row,row,row your boat,gently down the stream.
#Merrily,merrily,merrily,merrily,life id but a dream.
#Row,row,row your boat,over we go.
#Row,row,row, 123
#Row your boat,back we go.
#Row,row,row your boat,home we go.

#第1行和第4行删除,并没有对文件进行修改,1,4是样式，d是命令
sed '1,4d' boat.txt

#-i(对文件的内容进行修改)
#sed -i '1,4d' boat.txt

#正则表达式，把含有row的行全部删除
#!d把没有row的删除
sed '/row/d' boat.txt
sed '/row/!d' boat.txt

#把含有数字的删除 大括号要转义
#{3}:三个数字
sed '/[0-9]\{3\}/d' boat.txt

#删除空行
# 开头:^,马上就结束$.(^$:开头和结尾的地方什么都没有)
sed '/^$/d' boat.txt

#p,把有123的显示出来,但没有123的也显示了出来
sed '/123/p' boat.txt

#-n 只显示123,-n和p一般一起使用
sed -n '/123/p' boat.txt

#s 替换.把row换成hello,但每一行只换一个,如果全都换掉，要加g
# 如果不区分大小写加上i
sed  's/row/hello/' boat.txt
sed  's/row/hello/g' boat.txt
sed  's/row/hello/gi' boat.txt # ? bad flag in substitute command: 'i'

#/row 替换/;即删除一行中row
sed  's/row//g' boat.txt
sed  's/row,//g' boat.txt
#结果：
#Row,, your boat
#Row,, your boat,gently down the stream.
#Merrily,merrily,merrily,merrily,life id but a dream.
#Row,, your boat,over we go.
#Row,,,123
#Row your boat,back we go.
#Row,, your boat,home we go.

#^.. :开头的2个字符删除,2个点表示2个字符
#..$ :开头的2个字符删除
sed  's/^..//g' boat.txt
sed  's/..$//g' boat.txt


#把row 变成rowed
#\1代表找到的每一个row，(后加ed,变成rowed)
sed  's/\(row\)/\1ed/g' boat.txt

#把从AAA到DDD之前的row行用hello替换
#指定行的范围
sed  '/AAA/,/DDD/s/row/hello/g' boat.txt
#sed  '/AAA/,/DDD/s/row/hello/gi' boat.txt
#sed: 1: "/AAA/,/DDD/s/row/hello/gi": bad flag in substitute command: 'i'
#替换前:
#Row,row,row your boat
#Row,row,row your boat,gently down the stream.
#Merrily,AAA merrily,merrily,merrily,life id but a dream.
#Row,row,row your boat,over we go.
#Row,row,row,123,DDD
#Row your boat,back we go.
#Row,row,row your boat,home we go.
#替换后:
#Row,row,row your boat
#Row,row,row your boat,gently down the stream.
#Merrily,AAA merrily,merrily,merrily,life id but a dream.
#Row,hello,hello your boat,over we go.
#Row,hello,hello,123,DDD
#Row your boat,back we go.
#Row,row,row your boat,home we go.

#指定行的范围2-4行的row 替换hello
sed '2,4s/row/hello/g' boat.txt
#sed '2,4s/row/hello/gi' boat.txt

#2g 每一行第二个之后替换hello
sed 's/row/hello/2g' boat.txt
#sed: 1: "s/row/hello/2g": more than one number or 'g' in substitute flags

#正则表达式可以用冒号和竖线
sed 's:row:hello:g' boat.txt
sed 's|row|hello|g' boat.txt

#把每个找到的单词加上方括号,小括号,Mac下不起作用
#[&]：表示找到的单词
# \w代表一个字母,+多个字母
sed 's/\w\+/[&]/g' boat.txt
sed 's/\w\+/(&)/g' boat.txt

# 数字 + 数字. （\2 \1:子串匹配标记）找到的数字交换位置
sed 's/\([0-9]\{3\}\) \([0-9]\{3\}\)/\2 \1/' boat.txt
#Row,row,row,DDD,456 123
#Row,row,row,DDD,123 456

# set '1,4d' boat.txt 与 cat boat.txt | sed '1,4d' 功能一样
cat boat.txt | sed '1,4d'

#两个sed 命令用 |
sed '1,4d' boat.txt | sed 's/row/hello/g' boat.txt#不起效果

#样式命令用 ;分隔
sed '1,4d;s/row/hello/g' boat.txt


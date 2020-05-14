#! /bin/bash
# 用tr进行转换 (tr:translate)

#转换 tr [options] set1 set2: set1转换成set2
#options: -d ,-c -s
# 字符集:
# alnum(字母和数字),alpha(所有的字母),cntrl(非打印的控制字符),digit(所有的数字)
# graph(图形字符),lower(小写字母),print(可打印的字符),punct(标点符号)
# space(空白字符) ,upper(大写字母),xdigit(16进制数)

echo "HELLO WHO IS THIS"

#结果: hello who is this
echo "HELLO WHO IS THIS" | tr 'A-Z' 'a-z'

#结果: 87654 相当于加密
echo  12345 | tr '0-9' '9876543210'

#结果:12345 .还原
echo 87654 | tr '9876543210' '0-9'

# 制表符变成空格
cat test.txt | tr '\t' ' '

# 制表符,换行 变成空格
cat test.txt | tr '\t\n' ' '

# -d 删除,找到'0-9'这些字符删除,结果:hello  world
echo "hello 123 world 456" | tr -d '0-9'

# -c:取反，与字人符集一起使用；如下，不是'0-9'、空格、换行符进行删除
#结果: 1  2  4
echo hello 1 char 2 next 4 | tr -d -c '0-9 \n'

# -s用来做压缩,把多个空格用一个空格来表示，结果：GNU is not UNIX. Recursive right ?
echo "GNU is    not UNIX. Recursive right ?" | tr -s ' "

# 把多个换行用一个换行来表示
cat test2.txt | tr -s '\n'

cat test3.txt | echo $(tr '\n' '+') 0

# 把多个数字相加 ,转换成数学运算 $[ ]
cat test3.txt | echo $[ $(tr '\n' '+') 0 ]

#test3.txt:
#1
#2
#3
#4
#5

# 所有小写变成大写,用字符集
echo "this is a test" | tr '[:lower:]' '[:upper:]'

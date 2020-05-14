#! /bin/bash
# 用 grep 在文件中搜索文本

# grep / egrep(专门使用正则表达式)
#搜索文本文件的内容:通配符、正则表达式
#选项：
# -E,-o,-v,-c
# -n,-b,-l,-L
# -R,-i,-e,-f
# --include --exclude
# -z,-q
# -A,-B,-C

# 搜索test1.txt 文中a字符
grep "a" test1.txt
#or
grep a test1.txt
#多个文件
grep a test.txt test1.txt test2.txt

#-E:正则
grep -E "[0-9]+" test1.txt

grep -E "[0-9]+ [a-z]" test1.txt

#egrep 直接跟正则表达式,一行一行进行搜索
egrep "[a-z]+ [a-zA-Z]+" test1.txt

# 只输出找到的:字母 空格
egrep "[a-z]+ [a-zA-Z]+" test1.txt -o

# -v搜索没有的字符串,-v a，没有a的全显示
grep -v a test1.txt

# -c 搜索带字符有多少行,test1.txt带a的有多少行
grep -c a test1.txt

#-o：输出所有的a的字符
grep -o a test1.txt
#a
#a
#a
#a
#a
#a
#a

#统计
grep -o a test1.txt | wc -l

# -n显示行,有a字符的行号
grep -n a  test1.txt

# -l 有a字符的文件名进行显示,-L 没有a字符的文件名进行显示
grep -l a  test.txt test1.txt test2.txt
grep -L a  test.txt test1.txt test2.txt

# -R 递归的方式进搜索
grep -R -n "main()" /usr

#-i 不分大小写的搜索
grep -i A test1.txt

# -e 多个字符一起搜索 'a'与'的' 一起搜
grep -e a -e 的 test1.txt

# --include 只对某文件搜索 eg:只对.h文件搜索
grep /usr -R -n --include "*.h"

grep /usr -R -n --include "*.{c,cpp,h}"


# --exclude 不对某文件搜索 eg:不对c,cpp.h文件搜索
grep /usr -R -n --exclude "*.{c,cpp,h}"

#-q 搜索到的字符串不显示,怎么知道没有有搜到用 echo$?,如果是0,表示搜索到
grep -q a test1.txt

# -A后面的3行都显示出来.-B前面的2行显示出来 -C:前面的，后面的一起
# 如果显示出来了，后面的3行，前面的2行都显示出来
grep -n -A 3 -B 2 的 test1.txt
grep -n -C 3 的 test1.txt

grep a*  -l

# Z把文件名接起来
grep a*  -lZ

#grep a*  -lZ | xargw -0 rm


# ./grepcmd.sh a test1.txt
if [ $# -ne 2 ];
then
    echo "$0 match_test filename"
    exit
fi
match_test=$1
filename=$2
grep -q $match_test $filename
if [ $? -eq 0 ];
then
    echo "the text exits in the file"
else
    echo 'the text does not exist ih the file'
fi

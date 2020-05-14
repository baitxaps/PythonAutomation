#! /bin/bash
#正则表达式

#基本组成：
    #^ ,$,.[],[^],[-],? + ,*,()
    #(n),{n,},{n,m},|,\
#字符类
    #[:alnum:](数字和字母),[:alpha:](字母),[:blank:],[:digit:]
    #[:lower:],[:upper:],[:punct:](标点符号),[:space:](空格或回车换行)
#元字符
    #\b(一个单词的边界，左边界或右边界),\B(非单词边界),\d(单个数字字符),\D(单个非数字字符),
    #\w(每个单词字符,数字、字母、下划线),\W(每个单词字符,不是数字、字母、下划线),
    #\n(换行),\s(单个空白字符),\S(不是空白字符),\r(回车)

# ^某一行的开头 $某一行的结尾
egrep "^a" test1.txt -n
egrep "a$" test1.txt -n

# cook or cool,方括号的任一个
egrep "coo[k1]" test1.txt -n

egrep "coo[a-z]" test1.txt -n

#[^pl],不是p或l
egrep "a[^pl]" test1.txt -n

#两个数字一个空格
egrep "[0-9] [0-9]" test1.txt -n

# +一个或多个数字
egrep "[0-9]+ [a-z]" test1.txt -n --color=auto

#[0-9]{3}:3个数字
egrep "[0-9]{3} [a-z]" test1.txt -n --color=auto

#[0-9]{3,}:大于等于3个数字
egrep "[0-9]{3,} [a-z]" test1.txt -n --color=auto

#[0-9]{1,3}:1个到3个数字
egrep "[0-9]{1,3} [a-z]" test1.txt -n --color=auto

#[0-9]? 1个或没有
egrep "[0-9]? [a-z]" test1.txt -n --color=auto

#[0-9]* 0个或多次
egrep "[0-9]* [a-z]" test1.txt -n --color=auto

#(apple|computer) apple或computer
egrep "(apple|computer)" test1.txt -n --color=auto

#(d(o|a)t|computer):dot,dat,computer
egrep "(d(o|a)t|computer)" test1.txt -n --color=auto

#[[:digit:]]数字 ,[[:eipha:]]:字母
egrep "[[:digit:]]+ [[:alpha:]]+" test1.txt -n

#\b(一个单词的边界，左边界或右边界),\B(非单词边界)
#\bapple :以apple开头的单词,\bapple\b :匹配整个apple
egrep "\bapple\b" test1.txt -n

#结果:dappled
egrep "\Bapple\B" test1.txt -n

#\d(单个数字字符),\D(单个非数字字符)

#邮件地址. +表示多个,
egrep "[a-z0-9_]+@[a-z0-9]+\.[a-z]+" test1.txt -n

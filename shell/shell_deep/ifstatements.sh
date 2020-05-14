#! /bin/bash
#if语句

#if...;then
#...
#elif...;then
#...
#else
#...
#fi

# 一行，分号分隔三部分
if ((2<10));then echo "true"; fi

#(echo "trun")后分号可省
if ((2<10));then
    echo "true"
fi

#分号可省
if ((2<10))
then
echo "true"
fi

# 测试：./ifstatements.sh 90 90
#两个小括号，复合命令。必须要用两个小括号,如果不用小括号，用let
declare -i a a
a=$1;b=$2
if((a<b));then
    echo "$a 小于 $b"
elif((a>b));then
    echo "$a 大于 $b"
else
    echo "$a 等于 $b"
fi


if let "a<b" ;then
    echo "$a 小于 $b"
elif let "a>b";then
    echo "$a 大于 $b"
else
    echo "$a 等于 $b"
fi

if grep -q ^chen /ect/passwd; then
    echo 'chen this account exist'
fi


if [ -d /root/tmp ];then
    echo '/root/tmp document exist'
else
    echo '/root/tmp document no exist'
fi

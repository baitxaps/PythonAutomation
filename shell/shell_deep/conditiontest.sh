#! /bin/bash
#条件测试
# -q 是安全模式

#执行命令的结果
if grep -q "bash" out.txt; then
    echo "find bash in file out.txt"
else
    echo "not find"
fi

#执行命令的结果取反
if ! grep -q "bash" out.txt; then
    echo "not find"
else
    echo "find bash in file out.txt"
fi


#两个小括号的复合命令 \< 对符号进行转义，不然是输入
if ((20\<30));then
    echo true
fi

if((0));then
    echo true
else
    echo false
fi

if ((20 && 30));then
    echo true
fi

#用两个中括号
if [[ "str">"xyz" ]];then
    echo "str >"
else
    echo "str<"
fi

#用两个中括号，字符串双引号可不写
if [[ str>xyz ]];then
    echo str 大
else
    echo str 小
fi

# 用内置命令test进行比较
if test "str" \> "xyz" ;then
    echo str 大
else
    echo str 小
fi

# 用内置命令test进行比较 简写
if [ "str" \> "xyz" ];then
    echo str 大
else
    echo str 小
fi

#-a是and -o是or
#out.txt是否可读 并且myout.txt可执行
if [ -r out.txt -a -x debug.sh ];then
  echo 文件可读可执行
fi

if [ -r out.txt -o -x out.sh ];then
    echo 文件可读或可执行
fi


#可简写
if [ -e out.txt ];then
    echo 文件存在
fi
#简写
[ -e out.txt ] && echo 文件存在


if [ -e out.txt ] ;then
    echo 文件存在
else
    echo 文件不存在
fi
#简写
[ -e out.txt ] && echo 文件存在 || echo 文件不存在

#out.txt不存在 执行(echo 文件不存在)语句
[ -e out.txt ] || echo 文件不存在


a="str"
if [[ $a == "???" ]];then
    echo true
fi
# ???不加引号或双引号是通配符
if [[ $a == ??? ]];then
echo true
fi

str='abc 123 987 what u want.'
if [[ "$str" == * ]];then
    echo 真
fi

# 以. ? ! 结尾的 !转义
if [[ "$str" == *[.?\!] ]];then
 echo 真
fi

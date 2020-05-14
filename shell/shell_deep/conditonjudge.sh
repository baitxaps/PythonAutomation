#! /bin/bash
#条件判断

#文件属性的条件判断
# -f,-x,-d,-e,-c,-b,-w,-r,-L
# 文件是否存在:-e
# 文件路径或文件名:-f
# 文件是不是可执行的文件：-x
# 是不是目录:-d
# 是不是字符设备:-c
# 是不是块设备:-b
# 文件是否可写:-w
# 文件是否可读:-r
# 文件是不是符号链接:-L

#算术运算的条件判断
# -eq,-ne,-lt(小于:less than),-le(小于等于:less eaual),-gt(大于:greater than),-ge

#字符串的条件判断
# -z(字符串是空，长度为0),-n(字符串非空),==,=,!=,<,>
# == 和 = 一样


#文件属性的条件判断
if [ -e out.txt ];then
    echo file exist
fi

fpath="etc/passwd"
if [ -e $fpath ];then
    echo File exist;
else
    echo Does not exist;
fi

# $?:文件执行完了，看结果:$?
# 结果是1,不正常，退出
[ -e "/etc/hosts" ] || (echo '/ect/hosts 文件不存在')
if [ "$?" -eq 1 ];then
    exit
fi
echo 文件存在,继续执行

#算术运算的条件判断
# 声明一个整数变量
declare -i len
a=20
if [ $a -eq 20 ];then
    echo "变量a等于20"
fi

if [ $a -gt 10 ];then
    echo "变量a大于10"
fi

# 字符串比较
if [ $"LOGNAME" != "root" ];then
    echo 需要使用root权限执行
fi

if [ "Bill" > "Apple" ];then
    echo "Bill > Apple"
fi

str="Bill"
if [ -n $str ];then
  echo 字符串长度大于0
fi

str=''
if [ -z $str ];then
    echo 一个空字符串，长度为0
fi

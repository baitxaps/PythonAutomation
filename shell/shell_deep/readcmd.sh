#! /bin/bash
#read 命令
# 读键盘：read -n; read -s ;read -p ;read -t ;read -d
# 读文件：
    #使用cat 和管首进行读到
    #使用输入重定向进行读取

#-p 省掉echo进行提示
#echo -n "Enter your name: "
read -p "Enter your name:" name
echo "hello $name,welcome to my program"

# -t在规定的时间内，如 在5秒内输入内容,如没有输入内容，则显示sorry,too slow"
if read -t 5 -p "pls enter your name: " name
then
    echo "hello $name ,welcome to my script"
else
    echo "sorry,too slow"
fi

#-n 指定输入内容的个数
#如下面，指定了个数，不用回车
read -n 1 -p "Do u want to continue[Y/N]? " answer
case $answer in
    Y|y)
        echo "fine,continue";;
    N|n)
        echo "OK ,bye";;
    *)
        echo "error choice";;
esac

# -s 一般输入密码,不显示
read -s -p "Enter your password: " pass
echo "your passwrod:$pass"

# -d 指定一个定界符，作为输入结束，如:输入不用敲回车,一敲冒号就结束
echo "输入:"
read -d ":" var
echo $var




#使用cat和管首进行读到
echo "方法一"
count=1
cat readcmd.sh | while read line
do
echo -e "Line  $count: \t$line"
    count=$[ $count+1 ]
done

#输入重定向进行读取
echo "方法二"
count=1
while read line
do
    echo -e "$count:\t$line"
    count=$[ $count+1 ]
done < readcmd.sh

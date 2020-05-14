#! /bin/bash
#获取终端信息

#tput cols # 显示终端宽度
#tput lines # 显示行数
#tput longname #打印终端名称
#tput cup 10 10 #调整光标位置到10行10列
#tput setb 0 #调整终端背景颜色 编号： 0-n
#tput setf 0 #调整前景颜色
#tput bold #调整字体
#tput smul #命令行下划线
#tput rmul #关闭下划线

#输入密码时隐藏输入密码
echo "Enter password: "
stty -echo #关闭显示(密码)
read password
stty echo #打开显示
echo
echo password read.


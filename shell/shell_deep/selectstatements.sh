#! /bin/bash
#select 语句 经常做一些功能程序
#双重功能：循环+选择

#select...in...
#do
#...
#done

# ctrl+d/c退出
# PS3='请选择:' 修改#?为请选择
PS3='请选择:'
#IFS=' ' 可以不写，默认是空格
menu="新增 修改 删除 查找 安装 初始化"
#select 进行循环，一项一工项按次序排列出来
select choice in $menu
do
#REPLY 是自动的，编号
    echo "你选择的是: $REPLY, 选择的项目是:$choice"
#加break只能选一次,打断循环
    break
done


# 当前文件夹列出来
select f in *
do
    echo "你选择的是: $REPLY, 选择的项目是:$f"
done


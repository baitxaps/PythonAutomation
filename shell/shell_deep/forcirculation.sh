#! /bin/bash
#for循环
# 和C语言一样的for循环
# 处理列表数据的for循环:数之字序列/字符序列/文本字符串


# 和C语言一样的for循环
declare -i i s
for((i=1;i<=10;i++))
do
    echo $i
done


for((i=1;i<=100;i++))
do
    let s+=i
done
echo $s


# 处理列表数据的for循环:数之字序列/字符序列/文本字符串
# 环境变量IFS 处理字符分隔,默认是空白符、空格、回车换行符、制表
data="name,sex,rollno,location"
#原来IFS值保留
oldIFS=$IFS
IFS=","
for item in $data;
do
    echo $item
done
IFS=$oldIFS


line="root:x:0:0:root:/root:/bin/bash"
oldIFS=$IFS;
IFS=":"
count=0
for item in $line;
do
    [ $count -eq 0 ] && user=$item
    [ $count -eq 6 ] && shell=$item
    let count++
done;
IFS=oldIFS
echo $user\'s  shell is $shell;


#数之字序列
for i in 1 2 3 4 5;
do
    echo $i
done
echo
echo

for i in {10..20}
do
    echo $i
done


#字符序列
for c in {a..h}
do
    echo $c
done

#更表根目录下所的文件
DIR="/Users"
for f in $(ls $DIR)
do
    echo $f
done

DIR="/Users"
cd $DIR
for f in $(ls $DIR)
do
#如果是文件夹，查看占用磁盘空间大小
    [ -d $f ] && du -s $f
done

#无穷循环,ctrl+c exit
for ((;1;))
do
    echo "circulation :$i times"
done

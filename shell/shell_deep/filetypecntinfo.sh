#! /bin/bash
#文件类型统计信息

#文件类型信息
#file -b filename
#工作原理
#declare -A statarray;
#<(find $path -type f -print)
#${!statarray[@]}

#file test3.txt #test3.txt: ASCII text

#-b 只显示文件的类型:ASCII text
#file -b test3.txt

#如果文件类型信息太长，可用-d加字符分隔,-f取哪一列
#如逗号分隔，取第一列
#file -b test3.txt | cut -d,-f1


# 对文件夹文件相同类型的文件进行统计 ./filetypecntinfo.sh /usr
# 对当前文件进行统计./filetypecntinfo.sh .

#检查参数是否合法
if [ $# -ne 1 ];
then
    echo $0 basepath;
    exit -1
fi
path=$1
declare -a statarray;

while read line;
do
    ftype=`file -b "$line" | tr -s ' '|cut -d' ' -f1`;
#    ftype=`file -b "$line" | cut -d, -f1`;
echo $ftype
  let statarray["$ftype"]++;
#小括号表示子shell、子进程 ,子进程的输出:<(find $path -type f -print)
#< 再利用输入重定向 转给while循环
done < <(find $path -type f -print);

echo ================= file types and counts =================
# 得到数组中所有的索引:!statarray[@]
for ftype in "${!statarray[@]}";
do
#{statarray["$ftype"] 数量
echo $type : ${statarray["$ftype"]}
done


cat file|tr -s ' '|cut -d' ' -f2


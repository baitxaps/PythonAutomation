#! /bin/bash
# 玩转 xargs

#标准输入->命令行参数
#选项:-n,-d,-I,-O
#结合find 使用xargs

# cmd1 | xargs cmd2 arg1 arg2
# 通过管道第二个命令不能接受第一个命令的标准输出,第二个命令只能接收参数，就不能通过管道连起来,就要用xargs

# 多行文本变成单行
#cat example.txt | xargs

#-n指定行数,没有指定默认一行
#cat example.txt | xargs -n 3

# -d 以指定某个为分隔符,显示：split split split。Mac下没有此选项
#echo 'splitXsplitXsplit' | xargs -d X
#echo 'splitXsplitXsplit' | xargs -d X -n 2

# $* 显示所有的命令行参数 ./xargs arg1 arg2 => arg1 arg2 #
echo $* '#'

#把args.txt 内容 变成1 行参数给xargs.sh
#cat args.txt | xargs -n 1 ./xargscmd.sh
#cat args.txt | xargs  ./xargscmd.sh

#./xargscmd.sh -p arg1 -l  参数-p -l 固定，但arg1变化,写法如下：
#: -I {} 大括号输出的每一个会在 -p {} -l 替换掉
#cat args.txt | xargs -I {} ./xargscmd.sh -p {} -l

# -print0 斜杆和斜杠之前没有\n 是\0,看不见的
find . -type f -name "*2.txt" -print0 | xargs -0 rm -f

#print0 :
#./file2.txt./file1.txt./all_x_files.txt./english_a.txt./file1_aa.txt./file2_a.txt./english.txt./args.txt./example.txt./descriptor_test.txt./file1_a.txthairongchen:shairhahairhairhairhairhairhairhairhairhahairongchen:shell (master #)$

#print:
#./file2.txt
#./file1.txt
#./all_x_files.txt
#./english_a.txt
#./file1_aa.txt
#./file2_a.txt
#./english.txt
#./args.txt
#./example.txt
#./descriptor_test.txt
#./file1_a.txt

#wc -l 统计有文件有多少行
find /usr -type f -name "*.c" -print0 | xargs -0 wc -l

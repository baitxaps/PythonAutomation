#! /bin/bash
#用 cat进行拼接

# cat file1 file2 file3...
# cat -file.txt
# echo ... | cat -file.txt
# echo -s file
# cat file | tr -s '\n'
# cat -t file
# cat -n file
# ls -l | cat -n

#两个文件串连输出,原文件并没有修改,
cat file1.txt file2.txt

# -代表标准输入,也就是键盘 ,ctrl+d 退出.原文件并没有修改
cat -file1.txt file2.txt

echo "Text throught stdin" | cat - file1.txt

#-s 把多行空行变成只有一行空行,原文件并没有修改
cat -s file1.txt

# tr -s '\n' 把所有的空行都删除进行显示,原文件并没有修改
cat  file1.txt | tr -s '\n'

# -t 把制表符用特殊的符号显示出来
cat -t file1.txt

# -n 显示加行号
cat -n file1.txt

ls -l | cat -n

cat -s -n file1.txt file2.txt


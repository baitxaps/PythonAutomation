#! /bin/bash
#读取命令序列输出

#管道和过滤器
#ls | cat -n
#ls -l | cat -n

ls |cat -n >out.txt

# 命令序列保存到变量
# 子shell读命令序列的输出
cmd_output=$(ls | cat -n)
echo $cmd_output

# 反引用
cmd_output2=`ls | cat -n`
echo $cmd_output2

# 子shell读命令序列的输出 用双引号
out="$(cat text.txt)"
echo $out

# 用子shell生成一个独立的进程,改变的是子进程的路径，当前路径并没有改变
pwd
(cd /bin; ls);
pwd

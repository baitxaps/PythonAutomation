
#! /bin/bash
#使用别名

alias lm='ls -l | more' # lm 代替 ls -l | more
unalias lm

alias rm='rm -i' # 删除进行确认提示
unalias rm
\rm #调用真正命令,不用别名



#! /bin/bash
#列出网络上所有的活动主机

#使用：ping
#使用：fping

#-c:指定ping的次数
#ping -c 5 192.168.0.107

#for ip in 192.168.0.{1...255}
#do
## 加快执行速度：
##():小括号放在子shell中执行的。255个子线程并行工作，加个wait，主线程等待子线程全部结束
#(
## &>/dev/null:输出重定向null
#    ping $ip -c 2 &>/dev/null;
##检查是否ping通
#    if [ $? -eq 0 ];
#    then
#        echo $ip is alive
#    else
#        echo $ip 不通
#    fi
#)
#done
#wait

ip=192.168.0.
for n in `seq 1 254`
do
(
    # &>/dev/null:输出重定向null
    ping -c 2 $ip$n &> /dev/null;
    #检查是否ping通
    if (($?==0));
    then
        echo $ip$n is alive
    else
        echo $ip$n 不通
    fi
)
done
wait


#fping -g:所有的区段 -a:打印所有活动的IP
#2标准错误输出
# 192.168.0.1/24:与192.168.0.1 192.168.0.255写法一样
fping -a 192.168.0.1 192.168.0.255 -g
fping -a 192.168.0.1 192.168.0.255 -g 2>/dev/null
fping -a 192.168.0.1/24 -g 2>/dev/null

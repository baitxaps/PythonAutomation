#! /bin/bash
#调试脚本

# 用echo
# bash -x ./debut.sh 所有的行都echo
# 在代码中用:set -x,set+x 夹在中间的代码才echo
# 使用环境变量：_dubug, 在命公行中输入:_DEBUG=on ./dubug.sh


#_DUBUG ==NO,当有参数时输入，否则什么都不做
function DEBUG()
{
    [ "$_DEBUG" == "on" ] && $@ || :
}

start=$(date +%s) #记录当前多少秒
echo -n Count:
tput sc; #保存光标的位置
count=0;
while true;
do
    #set -x;
    if [ $count -lt 10 ]; #count>10循环,否则退出
    then
        let count++;
        sleep 1;#延时1s
        tput rc;#光标还原
        tput ed;#从光标当前位置到后面所有清空,如果1-40,递增不用，如40-1,要用清空
        echo -n $count;# -n不用换行
    else
    #exit 0;#退出整个脚本
        break;
    fi
    #set +x;
done
echo #加多一个换行
end=$(date +%s)

DEBUG echo $start
DEBUG echo $end

difference=$(( end - start ))
echo Time taken to execute commands is $difference seconds.

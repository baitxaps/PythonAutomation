#! /bin/bash
#日期和延时
#date # 显示当前日期
#date +%s #1970 0时0分0秒到现在多少秒,叫纪元时 eg:1544367357
##date --date "2015-12-08" +%s #1970 0时0分0秒 到2015-12-08 时间段
#date +%a #当前星期 ：五
#date +%A #当前星期 ：星期五
#
#date +%b #当前月 ：12月
#date +%B #当前月 ：十二月 （大写）
#
#date +%d #当前日 ：25
#date +%D #当前日 ：12/09/18
#
#date +%y #当前年 ：18
#date +%Y #当前年 ：2018
#
#date +%h #当前时 ：12
#date +%H #当前时 ：23 24小时制
#
#date +%M #当前分 ：09
#date +%S #当前秒 ：09
#date +%s #1970 0时0分0秒到现在多少秒,叫纪元时 eg:1544367357
#
#date "+%Y %b %d" #2018 12 09

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

difference=$(( end - start ))
echo Time taken to execute commands is $difference seconds.

#! /bin/bash
#while 和 until 循环

#while...
#do
#...
#done

#until...
#do
#...
#done

declare -i i s

s=0
for ((i=1;i<=100;i++))
do
    let s+=i
done
echo $s


i=1
s=0
while ((i<=100))
do
    let s+=i
    let i++
done
echo $s


i=1
s=0
#当i大于100停止循环
until ((i>100))
do
let s+=i
let i++
done
echo $s

# while 读文件，每次读一行
while read line
do
    echo $line
done < whileuntilcirculation.sh


#显示密码文件
#cat /etc/passwd

oldIFS=IFS;
IFS=':'
#_displaypolicyd:*:244:244:Display Policy Daemon:/var/empty:/usr/bin/false
while read f1 f2 f3 f4 f5 f6 f7
do
    echo "帐号:$f1,login Shell: $f7"
done < "/etc/passwd"
IFS=oldIFS

#无穷循环
#while((1)) = while true = while
# until((0))= until false

#while true
#do
#done

#until false
#do
#
#done



#! /bin/bash
#变量和环境变量

fruit=apple
count=5
echo "we have $count ${fruit}"

no1=4
no2=5
let result=no1+no2
echo $result

#cat englist | tr '\n' '\0'
 
var=1234
echo ${#var} #4

if [ $UID -ne 0 ];then
	echo Non root user. pls run as root.
else
	echo "Root user"
fi
 

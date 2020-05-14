#! /bin/bash
#通过Shell进行数学运算

#简单的运算，只能是整数，不能小数
no1=12;
no2=12;
let result1=no1+no2;
result2=$[no1+no2];
result3=$((no1+no2));
echo $result1;
echo $result2;
echo $result3;

#expr：计算表达式或正则匹配
result=`expr 3 + 5`;
echo $result;

result=$(expr $no1+9);
echo $result;

#bc 高级运算，整数、小数都可以
#bc
#4*0.54;
#10^3;
#sqrt(100);
#quit

echo "4*0.56" | bc;

#no=54;
#result= 'echo "$no * 1.5" | bc'
#echo $result

echo "scale=2;10/3"|bc; #scale=2 输出两位小数

no=100
echo "obase=2;$no" | bc # obase=2 10进制输出为二进制

no=11101001
echo "obase=10;ibase=2;$no" | bc #ibase=2:指定输入为了2进制，2进制输出为10进制

echo "sqrt(100)" | bc;
echo "10^3" | bc;

#! /bin/bash
#循环控制

for((i=1;i<10;i++))
do
if [ $i -eq 6 ];then break; fi
    echo $i
done
echo "over"


# 只能退出1层
for((i=1;i<10;i++))
do
    for((j=1;j<10;j++))
    do
        r=$((i+j))
        if [ $r -eq 19 ] ;then break;fi
        echo $r
    done
done

# 2个for嵌套同时退出，应该加break 2 ,三个for嵌套同时退出 加break 3.
for((i=1;i<10;i++))
do
    for((j=1;j<10;j++))
    do
        r=$((i+j))
        if [ $r -eq 19 ] ;then break 2;fi
    echo $r
    done
done


echo "Tyr continue..."
for((i=1;i<=10;i++))
do
    if [ $i -eq 6 ];then continue;fi
    echo $i
done

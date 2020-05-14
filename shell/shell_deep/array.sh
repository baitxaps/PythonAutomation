#! /bin/bash
#数组和关联数组

# 普通数组
a=(10 20 30 40 50 60)
echo ${a[0]}
echo ${a[5]}

b[0]='text1'
b[1]='test2'
b[2]='text3'
echo ${b[0]}
echo ${b[1]}
echo ${b[2]}

index=2
echo ${a[$index]}

echo ${b[@]}
echo ${b[*]}  # (*、@ 索引，所有的数据全部显示)
echo ${#a[*]} # (#a[*] 显示数组所有的个数)
echo ${!a[*]} # 显示a数据中所有的下标

# 关联数组
declare -a fruits #fruits数组名，用字符串做索引
fruits=([apple]=`100 dollars` [orange]=`150 dollars`)
echo "Apple costs ${fruits[apple]}"
echo ${fruits[orange]}

#echo ${fruits[*]}
#echo ${!fruits[*]}
echo ${#fruits[*]}

declare -a dic
dic=([key1]="value1" [key2]="value2" [key3]="value3")
echo ${!dic[*]}
echo ${dic[key1]}
echo ${dic[key2]}
echo ${dic[key3]}

#for key in ${!dic[*]};do
#echo "$key: ${dic[$key]}"
#done

#tuple=(value1 value2 value3)
#echo ${tuple[*]}

#! /bin/bash
#条件判断

#case ...in
#...)
#.....;;
#...)
#....;;
#*)
#...;;
#esac


#echo "input: "
#read num
#echo "the input data is $num"
#
#if [ $num -eq 1 ];then
#    echo "January"
#elif [ $num -eq 2 ];then
#    echo "Feburay"
#elif [ $num -eq 3 ];then
#    echo "March"
#fi
#
#
#case $num in
# 1)
#    echo "January"
#    ;;
# 2)
#    echo "Febuary"
#    ;;
# 3)
#    echo "March";;
# *)
#    echo "其他所有的情况适配"
#    ;;
#esac


#不区分大小写
shopt -s nocasematch
echo "Enter your name: "
read yname
case $yname in
    Jack | John | Joe)
        echo "well..."
        echo "Lone time no see."
        echo "How do you do?"
        ;;
    mary | May)
        echo "Nice to meet you ."
        ;;
    c*)
        echo "Long time no see."
        ;;
    *)
        echo "hi!"
        ;;
esac

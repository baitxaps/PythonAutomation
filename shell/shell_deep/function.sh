#! /bin/bash
#函数和参数

#全局变量和局部变量
#函数的结束状态
#函数参数

# function 关键字可以不写
function getline()
{
    local i=0
    while read line
    do
        let ++i
    if (($i >10));then
        echo "已起过10行,停止执行"
        #return 只要不是0即可
        return 3
    fi
    done < $file
    echo "$fine 一共有$i 行"

    return 0
}

function getline_test()
{
    local i=0
    while read line
    do
        let ++i
        if (($i >100));then
            echo "已起过100行,停止执行"
            return 3
        fi
        #$1 表示接受第一个参数
        done < $1
    echo "$fine 一共有$i 行"
    return 0
}

# 把第二个参数输入到第一个参数里
appendfile() {
    echo "$2" >> "$1"
}

foo() {
    echo $1,$2
#不知道参数有多少个，用$@，原来是多少个还是多少个；用@*，所有参数是一个字符串
    echo "$@"
    echo "$*"
    return 0
}


#file 全局变量 传参给函数
file="function.sh"
getline
# echo $?:查看命令结束的状态,正常结束为0 函数的结束状态也一样
if [ $? -eq 3 ];then
    echo 'getline()提前结束'
elif [ $? eq 0 ];then
    echo 'getline()正常结束'
fi

# function.sh一个参数
getline_test "function.sh"

# hello 字符串输出到tmp.txt文件中
appendfile "tmp.txt" "hello"
appendfile "tmp.txt" "world"
appendfile "tmp.txt" "too"
echo 'appendfile()结束'

foo "a" "10" "hello" "dog" "cat" "99"
echo 'foo()结束'

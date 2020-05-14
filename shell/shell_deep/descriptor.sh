#! /bin/bash
# 文件描述符和重定向

#cat -n descriptor_test.txt # -n 加行号 ,空行也加
#cat -b descriptor_test.txt # -b 加行号 ,空行不加
#cat -s descriptor_test.txt # -s 两个连续两个之空行变成一个空行
cat -e descriptor_test.txt # -e 每一行后面加$,后面表示有多少空格

echo "This is  a smaple text 1" > echo.txt
echo "This is  a sample text 2" >> echo.txt #>> 追加方式
echo "This is  a sample text 2" 1>> echo.txt #>> 追加方式 1是文件描述符，可以不写
# 0 标准输入 1 标准输出 2 标准错误
#ls + 2> out.txt
#cat e* 2> err.txt
#cat e* 2> /dev/null #错误信息扔掉，不会保留
#cat e* 1> out.txt 2> err.txt #错误信息扔掉，不会保留

#cat e* 1> out.txt 2> out.txt #重定向到同一个文件 可以简写为:cat e* 2>&1 out.txt
cat a* 2>&1 out.txt #cat e* 2>&1 out.txt简写: cat e* &> out.txt
#cat a* &> out.txt

cat a* |  tee out.txt | cat -n # tee 把一份传递到文件 并把一份拷山贝到管到传下去
cat a* |  tee -a out.txt | cat -n # -a：进行追加模式到文件，不会覆盖

exec 3<input.txt # 创建一个新的描述符3,是文件描述符 <:重定向输入
#cat <&3
#cat 3>&- # 每次输出都进行改写

exec 4>myout.txt #打开一个文件myout.txt 指定文件描述符4
echo hello 4 >&4 #向4文件描述符中输入 “hello 4"
#exec 4>&-



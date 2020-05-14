#! /bin/bash
#awk 入门，用于处理数据流

#基本语法：awk "BEGIN{ ... } pattern { ... } END { ... }"
#特殊变量:NR,NF,$0,$1,$2(NR 当前处理的是第几行 ,NF这一行一共有几列)
#将外部变量传给awk
#用getline读取行
#设置字段定界符
#从awk中读取命令输出
#在awk中使用循环

#{print}:中间部分用来读取文件,print文件中的每一行读出来
#BEGIN{} END{}可以省略掉
awk 'BEGIN{print "Start"} {print} END{print "End"}' test3.txt


#test3.txt 内容：
#one
#two
#Three
#Four
#Five

#BEGIN{} END{}可以省略掉
awk '{print} END{print "End"}' test3.txt
awk '{print}' test3.txt

# 中间部分：'/^T.+/' {print}，以T开头内容进行显示
awk 'BEGIN{print "Start"} '/^T.+/' {print} END{print "End"}' test3.txt

#结果：5
#awk可以用上变量
awk 'BEGIN{i=0} {i++} END{print i}' test3.txt

# 以F开头
awk 'BEGIN{i=0} '/^F.+/'{i++} END{print i}' test3.txt

# begin and end 省掉
awk ''/^F.+/'{print}' test3.txt

#test3.txt 内容：
#one    oNe onE
#Two tWo    twO
#Three tHree thRee
#Four fOur foUr
#Five fIve fiVe
#对列进行处理.输出第1､3列
awk '{print $1,$3}' test3.txt

#显示所有进程
ps auxw

#结果，对于这样的数据，非常适合用awk来处理
#USER               PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND
#root                97   9.9  0.2  4350120  13824   ??  Ss   10:21下午   0:05.95 /usr/libexec/opendirectoryd
#_windowserver      180   6.4  1.2  5651116  99016   ??  Ss   10:22下午  19:45.96 /System/Library/PrivateFrameworks/SkyLight.framework
#_coreaudiod        178   3.2  0.2  4314728  15608   ??  Ss   10:22下午   5:19.02 /usr/sbin/coreaudiod
#hairongchen       2535   1.7  1.4  5103116 115312   ??  S     4:38下午   1:41.98 /Applications/Movist.app/Contents/MacOS/M

#显示所有的进程Id
ps auxw | awk '{print $2}'

#显示内存的使用情况
cat  /proc/meminfo

# 显示总内存 mac下找不到路径
#cat  /proc/meminfo | awk '/MemTotal/{print $2}'

#得到电脑的IP地址
ifconfig
#结果：
#o0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
#options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
#inet 127.0.0.1 netmask 0xff000000
#inet6 ::1 prefixlen 128
#inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
#nd6 options=201<PERFORMNUD,DAD>
#gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
#stf0: flags=0<> mtu 1280
#EHC26: flags=0<> mtu 0
#EHC29: flags=0<> mtu 0
#XHC20: flags=0<> mtu 0

ifconfig | grep 'inet'
#ifconfig | grep 'inet 地址:'
#结果：
#inet 127.0.0.1 netmask 0xff000000
#inet6 ::1 prefixlen 128
#inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
#inet 192.168.0.107 netmask 0xffffff00 broadcast 192.168.0.255
#inet6 fe80::3c8d:beff:fee2:313f%awdl0 prefixlen 64 scopeid 0xa
#inet6 fe80::53d5:af92:716f:a617%utun0 prefixlen 64 scopeid 0xe

ifconfig | grep 'inet' | grep 'netmask'
#结果：
#inet 127.0.0.1 netmask 0xff000000
#inet 192.168.0.107 netmask 0xffffff00 broadcast 192.168.0.255

ifconfig | grep 'inet' | grep 'netmask' | awk '{print $2}'
#结果：
#127.0.0.1
#192.168.0.107

#如果结果是 地址:192.168.241.133 则
#-F:冒号做分隔符
#ifconfig | grep 'inet' | grep 'netmask' | awk '{print $2}'| awk -F: '{print $2}'

# 密码文件,
# 指定分隔符可用-F 或在 BEGIN{FS=":"}
cat /ect/passwd
awk -F: '{print $3,$4}' /etc/passwd
awk 'BEGIN{FS=":"} {print $3,$4}' /etc/passwd

#test3.txt：
#one    oNe onE
#Two tWo    twO
#Three tHree thRee thREe threE
#Four fOur foUr fouR
#Five fIve fiVe

# NR 当前处理的是第几行 ,NF这一行一共有几列
awk '{print NR,NF}' test3.txt
#结果
#1 3
#2 3
#3 5
#4 4
#5 3


#getline,读到第一行被扔掉了,把剩下所有的行进行了循环
awk 'BEGIN{getline;} {print}' test3.txt
#结果
#Two tWo    twO
#Three tHree thRee thREe threE
#Four fOur foUr fouR
#Five fIve fiVe


#用读到的行进行输出,第1行的第1列:
awk 'BEGIN{getline;print $1} {print}' test3.txt

#awk 'BEGIN{getline;getline;print $1} {print}' test3.txt

# getline输出，保存在变量cmdout里,并把cmdout打印出来
echo | awk '{ "grep root /ect/passwd" | getline cmdout; print cmdout }'



# awk中使用循环
awk 'BEGIN{print "Start"} '/^T.+/' {print;for(x=0;x<3;x++){print x}} END{print "End"}' test3.txt
#结果:
#Start
#Two tWo    twO
#0
#1
#2
#Three tHree thRee thREe threE
#0
#1
#2
#End

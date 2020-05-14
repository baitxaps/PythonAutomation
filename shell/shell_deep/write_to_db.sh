#! /bin/bash

# ./write_to_db.sh studentsdata.csv
USER="root"
PASS="root"

if [ $# -ne 1 ];
then
    echo $0 DATAFILE
    echo
    exit 2
fi
data=$1

while read line;
do
    oldIFS=$IFS
    IFS=,
    #line拆分成数组
    values=($line)
    #一行有4列
#    echo ${values[0]}
    #空格变成#，前后加上双引号
    values[1]="\"`echo ${values[1]} | tr ' ' '#'`\""
#    echo ${values[1]}
#    echo ${values[2]}
    #最后一列变成双引号
    values[3]="\"`echo ${values[3]}`\""
#    echo ${values[3]}
    IFS=$oldIFS
    #整个数组变成字符串,(tr ' #' ', '):空格变成逗号，#变成空格
    query=`echo ${values[@]} | tr ' #' ', '`

#    mysql -u$USER Students <<EOF
#    INSERT INTO students VALUES($query);
#    EOF
mysql -u$USER Students <<EOF
INSERT INTO students VALUES($query);
EOF

# echo $query
done < $data;
echo Wrote data into DB

#mysql -uroot Students
#select * from students

#读入：
#1,NAvin M,98,CS
#2,Kavya N,70,CS
#3,Nawaz O,80,CS

#echo ${values[1]}输出:
#1
#NAvin M
#98
#CS

#空格变成#：
#1
#"NAvin#M"
#98
#CS

#最后一列变成双引号:
#1
#"NAvin#M"
#98
#"CS"

#整个数组变成字符串:
#1 "NAvin#M" 98 "CS"
#2 "Kavya#N" 70 "CS"
#3 "Nawaz#O" 80 "CS"
#4 "Hari#S" 80 "EC"
#5 "Ales#M" 50 "EC"
#6 "Neenu#j" 70 "EC"
#7 "Bob#A" 30 "EC"
#8 "Anu#M" 90 "AE"
#9 "Sru" 89 "AE"
#10 "Andrew" 89 "AE"

#空格变成逗号，#变成空格:
#1,"NAvin M",98,"CS"
#2,"Kavya N",70,"CS"
#3,"Nawaz O",80,"CS"
#4,"Hari S",80,"EC"
#5,"Ales M",50,"EC"
#6,"Neenu j",70,"EC"
#7,"Bob A",30,"EC"
#8,"Anu M",90,"AE"
#9,"Sru",89,"AE"
#10,"Andrew",89,"AE"

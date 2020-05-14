#! /bin/bash

USER="root"
PASS="root"

# tail -n +2:第一行不要
depts=`mysql -u$USER Students <<EOF | tail -n +2
SELECT DISTINCT mark FROM students;
EOF`

echo ${depts}

for d in $depts
do
echo Department: $d
result="`mysql -u$USER Students <<EOF
SELECT name,dept from students WHERE mark="$d" ORDER by dept DESC
EOF`"
echo "$result"
echo
done



#+------+
#| mark |
#+------+
#| CS   |
#| EC   |
#| AE   |
#+------+

#mysql> select * from students
#-> ;
#+------+---------+------+------+
#| id   | name    | dept | mark |
#+------+---------+------+------+
#|    1 | NAvin M | 98   | CS   |
#|    2 | Kavya N | 70   | CS   |
#|    3 | Nawaz O | 80   | CS   |
#|    4 | Hari S  | 80   | EC   |
#|    5 | Ales M  | 50   | EC   |
#|    6 | Neenu j | 70   | EC   |
#|    7 | Bob A   | 30   | EC   |
#|    8 | Anu M   | 90   | AE   |
#|    9 | Sru     | 89   | AE   |
#|   10 | Andrew  | 89   | AE   |
#+------+---------+------+------+


#shell (master #)$ ./read_db.sh
#CS EC AE
#Department: CS
#name    dept
#NAvin M    98
#Nawaz O    80
#Kavya N    70
#
#Department: EC
#name    dept
#Hari S    80
#Neenu j    70
#Ales M    50
#Bob A    30
#
#Department: AE
#name    dept
#Anu M    90
#Sru    89
#Andrew    89

#SET @i:=0;加名字
#SET @i:=0;
#SELECT @i:=@i+1 as rank,name,dept from students WHERE mark="$d" ORDER by dept DESC
#EOF

#! /bin/bash
#从Bash中读写MySQL数据库

#3个脚本:
#创建数据库和数据表
#插入数据到数据表中
#查询数据库

#登录数据库
#mysql -uroot

#创建数据库和数据表
USER="root"
PASS="root"
# 从<<EOF开始到EOF结束,在中间操作sql
#2> /dev/null:错误重定向
mysql -u$USER <<EOF 2> /dev/null
#mysql -u$USER -p$PASS
CREATE DATABASE Students;
EOF
#检查是否成功
[ $? -eq 0 ] && echo Create DB || echo DB already exist

mysql -u$USER Students <<EOF 2> /dev/null
CREATE TABLE students(
id int,
name varchar(100),
mark varchar(10),
dept varchar(4)
);
EOF
[ $? -eq 0 ] && echo Create table students || echo students already exist

mysql -u$USER Students <<EOF
DELETE FROM students;
EOF

#ALTER TABLE students ADD mark int  not null;
#ALTER TABLE students MODIFY mark varchar(10);




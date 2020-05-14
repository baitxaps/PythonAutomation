#! /bin/dash
#MySQL 管理

#创建数据库
#创建用户、分配权限、修改口令
#五个常用命令:
#mysql,mysqladmin,mysqldump(备份),mysqlimport(原还),mysqlshow

mysql -u root mysql
show databases;
#不能使用下面这些数据库，否则会破坏mysql服务器
#+--------------------+
#| Database           |
#+--------------------+
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#+--------------------+

#创建数据库testdb;
create database testdb;

show databases;
#+--------------------+
#| Database           |
#+--------------------+
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#| testdb             |
#+--------------------+

use testdb;
show tables;
#Empty set (0.01 sec)

#创建表
create table children(childno integer auto_increment not null primary key,fname varchar(30),age integer);

show tables;
#+------------------+
#| Tables_in_testdb |
#+------------------+
#| children         |
#+------------------+
#1 row in set (0.00 sec)

select * from children;
#Empty set (0.01 sec)

#插入数据
insert into children(fname,age) values('Bill',12);
#Query OK, 1 row affected (0.09 sec)
insert into children(fname,age) values('Jenny',14);
insert into children(fname,age) values('John',10);
insert into children(fname,age) values('Jack',11);
select * from children;

#+---------+-------+------+
#| childno | fname | age  |
#+---------+-------+------+
#|       1 | Bill  |   12 |
#|       2 | Jenny |   14 |
#|       3 | John  |   10 |
#|       4 | Jack  |   11 |
#+---------+-------+------+
#4 rows in set (0.00 sec)



#创建用户:创建新的用户，新的口令给别人用
# all:所有的权限 on:数据库(所有的数据库：*.*)
# to:后接用户名 @'localhost':只能在本机使用,不能通过网络
# testdb.*:testdb中所有的对象
# identified by:后接密码

grant all on testdb.* to `bill`@`localhost` identified by `bill`;
#You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'privileges on testdb.* to `bill`@`localhost`' at line 1

#create user 'bill'@'localhost' identified by '123456';
#grant select privileges on testdb.* to `bill`@`localhost`;

#看表的字段
desc user;

select user,host ,Password_reuse_history  from user;
#+------------------+-----------+------------------------+
#| user             | host      | Password_reuse_history |
#+------------------+-----------+------------------------+
#| bill             | localhost |                   NULL |
#| laowang          | localhost |                   NULL |
#| mysql.infoschema | localhost |                   NULL |
#| mysql.session    | localhost |                   NULL |
#| mysql.sys        | localhost |                   NULL |
#| root             | localhost |                   NULL |
#+------------------+-----------+------------------------+
#6 rows in set (0.00 sec)

delete from user where user = 'bill' and  host = 'localhost';

# 修改密码
update user set password=passwrod('test') where user = 'bill';


#在cmd下：hairongchen:~ (master #)$
# mysqladmin  -u root -p version
#查看版本，状态(当前服务器的状态),改密码
mysqladmin  -u root  version
mysqladmin  -u root  status
mysqladmin  -u bill -p password 123


#mysqldump(备份),mysqlimport(原还)
mysqldump -u root testdb > testdb.bak

#显示
mysqlshow -u root
#+--------------------+
#|     Databases      |
#+--------------------+
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#| testdb             |
#+--------------------+

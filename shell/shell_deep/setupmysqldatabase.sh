#! /bin/bash
#安装 MySQL 数据库

#使用homebrew安装MySQL:https://www.cnblogs.com/chenmo-xpw/p/6102933.html
brew install mysql

#启动MySQL
bash mysql.server start

# 查mysql是否在运行
sudo netstat -tap | grep mysql

# sql登录,-p：要输入密码
mysql -u root -p

#退出
quit

select * from db;

#显示当前有多少个数据库
show databases;
mysql> show databases;
#+--------------------+
#| Database           |
#+--------------------+
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#+--------------------+
#4 rows in set (0.00 sec)

#使用哪个数据库,使用mysql
use mysql;

#显示有多少个表
show tables;
#+---------------------------+
#| Tables_in_mysql           |
#+---------------------------+
#| columns_priv              |
#| component                 |
#| db                        |
#| default_roles             |
#| engine_cost               |
#| func                      |
#| general_log               |
#| global_grants             |
#| gtid_executed             |
#| help_category             |
#| help_keyword              |
#| help_relation             |
#| help_topic                |
#| innodb_index_stats        |
#| innodb_table_stats        |
#| password_history          |
#| plugin                    |
#| procs_priv                |
#| proxies_priv              |
#| role_edges                |
#| server_cost               |
#| servers                   |
#| slave_master_info         |
#| slave_relay_log_info      |
#| slave_worker_info         |
#| slow_log                  |
#| tables_priv               |
#| time_zone                 |
#| time_zone_leap_second     |
#| time_zone_name            |
#| time_zone_transition      |
#| time_zone_transition_type |
#| user                      |
#+---------------------------+
#33 rows in set (0.00 sec)


select host,db user from db;

#p后跟密码,直接登录到mysql数据库
mysql -u root -proot mysql
mysql -u root -p mysql

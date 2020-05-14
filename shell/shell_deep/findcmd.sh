#! /bin/bash
# find

# 根据文件名或正则表达式匹配搜索
# 否定参数
# 基于目录深度的搜索
# 根据文件类型搜索
# 根据文件时间进行搜索
# 基于文件的大小的搜索
# 删除匹配的文件
# 基于文件权限和所有权的匹配搜索
# 结合find执行命令或动作
# 让跳find过特定的目录

cd /usr
# find .当前文件下查找所有文件,包含文件夹下的文件,ctrl+c :exit
find .

# -name只对文件名进行查找。 找到扩展名是txt的文件，并打印出来
find /usr -name ".txt" -print
find /usr -name ".c" -print

#-i不区分大小写
find /usr -iname "*.x" -print

#查找.x or .c 的文件 -o:或者 \:转义
find /usr \( -name "*.x" -o -name "*.c" \) -print

#查找svc的文件夹或文件名
find /usr -path "*svc*" -print

# 正则表达式查找 类型:标准类型,-regex后跟正则表达式 Mac下bash:-regextype "posix-egrep" 出现find: -regextype: unknown primary or operator
find /usr  -regextype "posix-egrep" -regex '.*(\.c|\.x)$' -print

# -i不区分大小写
find /usr  -regextype "posix-egrep" -iregex '.*(\.c|\.x)$' -print

# 不用正规，用name和通配符
find /usr \( -name "*.x" -o -name "*.c" \) -print

# !否定,不是.h的文件全部显示
find /usr ! -name "*.h" -print

# 点代表当前的文件夹,f代表所有普通文件，不包括文件夹
find . -type f -print

# d 查找当前文件下所有文件夹，只显示文件夹
find . -type d -print

# -maxdepth 最大深度1, 不查找子目录
find /usr  -maxdepth 1 -type f -print

# -maxdepth 最大深度2, 查找当前文件及儿子文件夹下的文件
find /usr -maxdepth 2 -name "*.h" -print

# -mindepth 最小深度3, 从孙子文件夹开始找，爸爸和儿子不找
find /usr -mindepth 3 -name "*.h" -print

# -mindepth 最小深度3, 从第三层开始找，找一层.
find /usr -mindepth 3 -maxdepth 1 -name "*.h" -print

# -atime -7 找最近7天时间之内访问文件 ,+7 or 7表示大于7天访问过文件
find . -type f -atime -7 -print
find . -type f -atime +7 -print

# -mtime:修改的文件 -ctime:变化时间,文件元数据改的时间,如权限
find . -type f -mtime 7 -print
find . -type f -ctime 7 -print

# -cmin 分钟 文件元数据改的时间,如权限
find . -type f -cmin 7 -print

#-newer 找比out.txt新的文件
find . -type f -newer out.txt -print

#-size 找大于size 大小的文件 eg:+2M,+2G,-2G,3M
find . -type f -size +2k -print

#-delete 找到的文件进行删除
find . -type f -name "*.tmp" -delete

#-exec 后接命令eg:cp,cat,mv,chmod 再以分号结束 ,分号要转义 {}所有文件，
#最后输出放在一个文件里all_x_files.txt
find /usr -name ".c" -exec cat{} \;>all_x_files.txt
#copy 到OLD文件夹里
find /usr -name ".c" -exec cp {} OLD \;

#-prune :某文件不用找，过滤跳过,如跳过"/root"
find  . -path "/root" -prune -o -type d -print

#-perm 644 找644文件权限的
find . -type f -perm 644 -print
find /usr -type f -name "*.c" ! -perm 666 -print


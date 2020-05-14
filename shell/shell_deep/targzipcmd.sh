#! /bin/bash
#归档和压缩

#使用 tar 归档
# tar -cf...
# tar -rvf ...
# tar -tvf...
# tar -xf ... -C ...
# tar -AF ...
# tar -uvf...
# tar -df ...
# tar -f ... --delete...
# tar -cf ... excclude...

#使用gzip压缩,可对任何文件进行压缩,每一次只能压缩一个文件
# gzip ...
# gunzip ...
# tar -czvf ...
# tar -xzvf ...
# tar -cavf ...
# tar -xavf ...

ls
#-c:创建新的归档文件 -f:指定文件名,f一定要写在最后 ,*.txt:要要归档的文件
tar -cf harry.tar *.txt

#-v：显示详细信息.显示哪些文件归档了
tar -cvf harry.tar *.txt

#-t：查看归档文件里面有哪些文件
tar -tvf harry.tar

# 后指定要归档的文件名
tar -cvf harry.tar test1.txt test2.txt test3.txt

#-r：向归档文件中追加归档文件
tar -rvf harry.tar md5.txt
tar -tf harry.tar

#-x 从归档文件中提取文件 -C：提取指定到新的文件夹中
#新建一个文件夹，把harry.tar 拷贝到新建一个文件夹中
tar -xf harry.tar
#-C指定到上一级目录中的cut文件夹
tar -xf harry.tar -C ../cut
#提取指定的文件:md5.txt test1.txt
tar -xvf harry.tar md5.txt test1.txt


tar -cvf 1.tar *.txt
tar -cvf 2.tar *.txt
#-A:归档文件合并,1.tar 2.tar 合并到1.tar中
tar -Af 1.tar 2.tar

#-u:归档文件追加,如果归档中的文件,与追加的文件不一样,就新追加的文件替换旧的
tar -uvf harry.tar test1.txt

#--delete:归档文件的文件删除,mac下没有--delete
tar -f harry.tar --delete test1.txt

#--exclude:归档不包括某个文件,mac下没有--exclude
#*:当前文件下所有的文件
tar -cvf harry.tar * --exclude "*.txt"
#tar -cvf harry.tar *

# 压缩test1.txt,压缩后是:test1.txt.gz,test1.txt被删除
# 多个文件的话，先归档，再压缩
gzip test1.txt
gzip harry.tar

#解压缩
gunzip harry.tar.gz

#-l看压缩文件中的信息
gzip -l harry.tar.gz
#compressed uncompressed  ratio uncompressed_name
#26578       177664  85.0% harry.tar

#-z:归档的同时进行压缩
#-a:根据文件名自动判断压缩格式
tar -czvf 1.tar.gz *txt
tar -cavf 1.tar.gz *txt

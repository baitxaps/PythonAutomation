#! /bin/bash
#查找并删除重复文件:内容完全相同，但文件名不同

#使用下列命令
# ls awk md5sum sort cat xargs uniq comm tee rm

# -lS 大s 会按照文件的大小排序:
#hairongchen:shell (master #)$ ls -lS
#total 144
#-rwsr-sr-x@  1 hairongchen  staff  785 12 11 22:20 whileuntilcirculation.sh
#drwxr-xr-x  24 hairongchen  staff  768 12 12 22:17 shell_deep
#-rwxr-xr-x@  1 hairongchen  staff  763 12 12 22:09 cat_a.sh
#-rw-r--r--@  1 hairongchen  staff  227 12 12 21:01 english.txt
#-rw-r--r--@  1 hairongchen  staff  227 12 12 21:01 english_a.txt
#-rwxr-xr-x@  1 hairongchen  staff  161 12 12 22:20 finddelrepeatfile.sh
#-rw-r--r--@  1 hairongchen  staff  160 12 12 21:41 tmp.txt
#-rw-r--r--@  1 hairongchen  staff   60 12 12 22:05 file1.txt
#-rw-r--r--@  1 hairongchen  staff   60 12 12 22:05 file1_a.txt
#-rw-r--r--@  1 hairongchen  staff   60 12 12 22:05 file1_aa.txt
#-rw-r--r--@  1 hairongchen  staff   52 12  9 15:01 descriptor_test.txt
#----------   1 hairongchen  staff    9 12  9 15:35 a1
#----------   1 hairongchen  staff    9 12  9 15:35 a1_a
#-rw-r--r--   1 hairongchen  staff    9 12  9 15:35 a2
#-rw-r--r--   1 hairongchen  staff    9 12  9 15:35 a2_b
#-rw-r--r--   1 hairongchen  staff    9 12  9 15:36 a3
#-rw-r--r--   1 hairongchen  staff    9 12  9 15:36 a3_c
#-rw-r--r--   1 hairongchen  staff    6 12 12 21:48 file2.txt
#-rw-r--r--   1 hairongchen  staff    6 12 12 21:48 file2_a.txt

# 第一个getline 读取第一行total 144，删除
# 第二个getline 读取 -rwsr-sr-x@... 我们要文件大小$5 和文件名$9

ls -lS | awk 'BEGIN {
    getline; getline;
    name=$9;size=$5
}
{
    #处理下面所有行
    # size 是第一个文件大小，$5是第二个文件的大小
    name2=$9;
    if(size==$5)
    {
        #比较name1和name2文件的校验和
        command1="md5sum "name1;
        command2="md5sum "name2;
        #校验和保存下来
        command1 | getline s; csum1=$1;
        command2 | getline s; csum2=$1;
        #command1 | getline s; print s;
        #command2 | getline s; print s;
        if(csum1==csum2)
        {
            print name1;print name2
        }
    }
    size=$5;name1=name2;
# 用sort 来进行排序,要不重复的文件名，保存到一个文件里:duplicate_files
}' | sort -u > duplicate_files

#duplicate_files把再进行一次md5,再进行排序,对重复的文件只取一个:uniq -w是hash值取前32位,
cat duplicate_files | xargs -I {} md5sum {} | sort -u | uniq -d | awk '{print $2}' |sort -u > dumplicate_sample
#cat duplicate_files | xargs -I {} md5sum {} | sort | uniq -w 32 | awk '{print $2}' | sort -u > dumplicate_sample

echo Removing...
comm duplicate_files dumplicate_sample -2 -3 | tee /dev/stder | xargs rm
echo Removing duplicates files successfully.

#校验和打印:
#hairongchen:shell (master #)$ ./finddelrepeatfile.sh
#670f6bffc35e78484d8d4e9de2c765dc  english.txt
#670f6bffc35e78484d8d4e9de2c765dc  english_a.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_a.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_a.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_aa.txt
#md5sum.c:140: Could not open file 'a1': Permission denied
#91f4f9c4cece2ca0d9166c589b14c132  file1_aa.txt
#md5sum.c:140: Could not open file 'a1_a': Permission denied
#91f4f9c4cece2ca0d9166c589b14c132  file1_aa.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_aa.txt
#d621d315bfd568b6983eea302932396f  a2
#d621d315bfd568b6983eea302932396f  a2
#d621d315bfd568b6983eea302932396f  a2_b
#d621d315bfd568b6983eea302932396f  a2_b
#137e8c19de7b8f9e6e891bb36f4d64f4  a3
#137e8c19de7b8f9e6e891bb36f4d64f4  a3
#137e8c19de7b8f9e6e891bb36f4d64f4  a3_c
#3d709e89c8ce201e3c928eb917989aef  file2.txt
#3d709e89c8ce201e3c928eb917989aef  file2_a.txt


#hairongchen:shell (master #)$ cat duplicate_files
#english.txt
#english_a.txt
#file1.txt
#file1_a.txt
#file1_aa.txt
#file2.txt
#file2_a.txt

#sort:
#hairongchen:shell (master #)$ ./finddelrepeatfile.sh
#3d709e89c8ce201e3c928eb917989aef  file2.txt
#3d709e89c8ce201e3c928eb917989aef  file2_a.txt
#670f6bffc35e78484d8d4e9de2c765dc  english.txt
#670f6bffc35e78484d8d4e9de2c765dc  english_a.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_a.txt
#91f4f9c4cece2ca0d9166c589b14c132  file1_aa.txt

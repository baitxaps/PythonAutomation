#! /bin/bash
# 校验和
# 最常用的两种检验和算法:md5(消息摘要算法,32个字符) ,sha1(安全哈稀算法，40个字符)
# 文件完整性测试:文件传输，系统备份，系统维护

md5sum test.txt #cefcf43343faacd5f335213168667231  test.txt
md5sum test.txt > test.md5

# 文件校验,是否一样:test.txt: OK
md5sum -c test.md5

# 很多文件校验
#cefcf43343faacd5f335213168667231  test.txt
#75738cb9b93e2c70c1ac67eac8912324  test2.txt
#a7b1ac3a2b072f71a8e0d463bf4eb822  test3.txt
md5sum test.txt test2.txt test3.txt

md5sum test.txt test2.txt test3.txt >> test_all.md5

# 检查
md5sum -c test_all.md5
#test.txt: OK
#test2.txt: OK
#test3.txt: OK

# 文件很多时用find
find . -type f -name "*.txt" -print0 | xargs -0 md5sum >> all.md5


#sha1 使用方法和md5一样
sha1sum test.txt >> test1.sha1
#7d8a4f01e8db4bd4849faf6dd813d7a29268da7f  test.txt
sha1sum -c test1.sha1
#test.txt: OK

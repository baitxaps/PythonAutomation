#! /bin/bash
#解析网站数据

#工作原理 : lynx(其实是一个游览器),grep,sed,awk
#示例:演员表
# http://www.johntorres.net/Boxofficefemalelist.html

#https://habilis.net/lynxlet/
#Absolute Path
#% /Applications/Lynxlet.app/Contents/Resources/lynx/bin/lynx
#Shell Alias

#% alias lynx='/Applications/Lynxlet.app/Contents/Resources/lynx/bin/lynx'
#% lynx
#Include lynx on the PATH
#% PATH=$PATH:/Applications/Lynxlet.app/Contents/Resources/lynx/bin
#% lynx

#Create a Symbolic link to lynx in a directory on the PATH
#% sudo ln -s /Applications/Lynxlet.app/Contents/Resources/lynx/bin/lynx /usr/bin/lynx
#% lynx

#lynx http://www.johntorres.net
#lynx -dump http://www.baidu.com | grep -o "Rank-.*"
lynx -dump http://www.baidu.com | grep -o "http.*"
sed 's/Rank-//;s/\[[0-9]\+]]//'
sort -nk 1

awk '
{
    for(i=3;i<=NF;i++) {
        $2=$2" " $i
    }
#固定4位左对齐
    printf "%-4s %s\n",$1,$2;
}' > actresslist.txt

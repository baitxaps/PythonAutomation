#! /bin/bash
# This shell looks through all the files in the current
# directory for some string,and then prints the names of 
# those files to the standard output.
# Shell脚本快速入门
for file in *
do 
 if grep -q Shell $file
 then 
   echo $file
 fi

done


who | wc -l
ls

echo the current date/time is
date

echo my name is
whoami


exit 0


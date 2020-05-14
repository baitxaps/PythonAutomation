#! /bin/bash
#终端打印
echo "welcom to Shell"
printf "Hello World\n"

echo -e "1\t2\t3"
printf "%5s %10s %4s\n" No Name Mark

printf "\n\n\n"

printf "%-5s %-10s %-4.2f\n" 1 Sarath 80.3435
printf "%-5s %-10s %-4.2f\n" 2 James  90.32435
printf "%-5s %-10s %-4.2f\n" 3 Jeff 88.3435 

echo -e "\e[1;31m this is red text \e[0m"

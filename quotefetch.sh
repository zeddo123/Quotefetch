#!/bin/bash
python3 fetch.py

b=$'\033[m'
y=$'\033[1;33m'

cpu=$(cat /proc/cpuinfo | grep "model name" | cut -d ' ' -f5 | head -1)

shell=$(basename $SHELL)

quote=$(<quote.txt)

distro=$(hostnamectl | cut -d: -f2 | sed -n "6p")
#$(uname -r | cut -d '-' -f3)

user=$USER
cat<< END

$quote
$y SHELL:$shell$b 	$y Distro:$distro$b
$y User:$user$b 	$y CPU:$cpu    
END
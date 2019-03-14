#!/bin/bash
python fetch.py

b=$'\033[m'
y=$'\033[1;33m'

cpu=$(cat /proc/cpuinfo | grep "model name" | cut -d ' ' -f5 | head -1)
shell=$(basename $SHELL)
quote=$(<quote.txt)
distro=$(uname -r | cut -d '-' -f3)

cat<< END

$quote
	$y SHELL:$shell$b 	$y Distro:$distro$b
	$y CPU:$cpu$b
END
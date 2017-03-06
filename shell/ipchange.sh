#!/bin/sh

touch ip.txt
BEFORE=`cat ip.txt`
IPADDRESS=`curl -s 1212.ip138.com/ic.asp |  iconv -f gb2312 -t utf-8 |  grep -oe '\[\(.*\)\]' | sed 's/\[//g' | sed 's/\]//g'`
if [ "$IPADDRESS" == "$BEFORE" ]
then
  echo "`date -u` not changed"
else
  echo $IPADDRESS > ip.txt
  curl -s http://semidream.com:10001/?text=${IPADDRESS}&to=oregami@163.com > /dev/null 2>&1
fi


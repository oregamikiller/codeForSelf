#!/bin/sh


GITREPOPATH='/Users/oregami/repos/oregamikiller.github.io'

GITCOMMOND=`which git`

cd $GITREPOPATH
$GITCOMMOND pull --rebase
touch $GITREPOPATH/ip.html
BEFORE=`cat ip.html`
IPADDRESS=`curl -s 1212.ip138.com/ic.asp |  iconv -f gb2312 -t utf-8 |  grep -oe '\[\(.*\)\]' | sed 's/\[//g' | sed 's/\]//g'`
if [ "$IPADDRESS" == "$BEFORE" ]
then
  echo "`date -u` ip地址未变化"
else
  
  echo $IPADDRESS > ip.html
  $GITCOMMOND add ip.html
  $GITCOMMOND  ci -m"ip change"
  $GITCOMMOND  push origin
fi

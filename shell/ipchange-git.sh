#!/bin/sh


GITREPOPATH='/Users/oregami/oregamikiller.github.io'

GITCOMMOND=`which git`

cd $GITREPOPATH
$GITCOMMOND pull --rebase
touch $GITREPOPATH/ip.html
BEFORE=`cat ip.html`
IPADDRESS=`curl -s 1212.ip138.com/ic.asp |  iconv -f gb2312 -t utf-8 |  grep -oe '\[\(.*\)\]' | sed 's/\[//g' | sed 's/\]//g'`
if [ "$IPADDRESS" == "$BEFORE" ]
then
  echo "`date -u` not changed"
else
  
  echo $IPADDRESS > ip.html
  #/usr/local/bin/git add ip.html
  #/usr/local/bin/git ci -m"ip change"
  #/usr/local/bin/git push origin
fi

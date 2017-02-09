#!/bin/sh

cd /jffs/scripts
mkdir -p .ip/
touch .ip/ip.txt
touch .ip/1.log
touch .ip/email.txt

IPADDRESS=$(/sbin/ifconfig ppp0 | sed -n 's/.*inet addr:\([^ ]*\).*/\1/p')
OLDIP=`cat .ip/ip.txt`

if [ $IPADDRESS == $OLDIP ]
then
  echo "`date -u` not changed"
else
  echo $IPADDRESS > .ip/ip.txt
  echo "$OLDIP=>$IPADDRESS" >> .ip/email.txt
  /usr/sbin/sendmail -S"smtp.126.com" -f"XXX@126.com" XXX@126.com -au"XXX" -ap"PPP" < .ip/email.txt
  echo "`date -u` changed" >> .ip/1.log
  echo "Send email successfully!"
fi

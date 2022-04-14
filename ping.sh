#!/bin/bash
file=/test_log/ping.log
DATE=/usr/bin/date
PING=/usr/bin/ping

$PING www.fommos.com -c 3
if [[ $? -eq 0 ]];then
	echo "`$DATE`: www.fommos.com is exist" >> $file
else
	echo "`$DATE`: www.fommos.com is not exist" >> $file
fi

#!/bin/bash

# 临时关闭selinxux
setenforce 0
# 关闭selinux
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

# 修改ssh端口
sed -i "s/#Port 22/Port 10888/g" /etc/ssh/sshd_config
# 重启sshd
systemctl restart sshd

# 安装netstat,lsof等网络工具
yum install -y net-tools lsof
#!/bin/bash

# 临时关闭selinxux
setenforce 0
# 关闭selinux
sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

# 修改ssh端口
sed -i "s/#Port 22/Port 10888/g" /etc/ssh/sshd_config
# 重启sshd
systemctl restart sshd
# firewalld开放sshd端口
firewall-cmd --add-port=10888/tcp --permanent
# firewalld开放80，443端口
firewall-cmd --add-port=80/tcp --add-port=443/tcp --permanent
# 重新加载firewalld配置
firewall-cmd --reload

# 安装netstat,lsof等网络工具
yum install -y net-tools lsof

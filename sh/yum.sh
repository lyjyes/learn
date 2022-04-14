#!/bin/bash
# 安装网络工具
yum install -y net-tools

# 下载nginx的rpm包
rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
# 安装nginx
yum install -y nginx

#!/bin/bash
# 检查mariadb是否安装
check=$(rpm -qa | grep mariadb)
# 安装则删除
if [[ -n $check ]];then
        rpm -e --nodeps $check
else
        echo "no mariadb"
fi

# 安装mysql依赖
yum install -y libaio net-tools
# 给tmp提升权限
#chmod -R 777 /tmp

# 安装mysql
rpm -ivh mysql-community-client-5.7.17-1.el7.x86_64.rpm mysql-community-libs-5.7.17-1.el7.x86_64.rpm mysql-community-common-5.7.17-1.el7.x86_64.rpm mysql-community-server-5.7.17-1.el7.x86_64.rpm

# 初始化mysql
mysqld --initialize --user=mysql

# 修改配置文件的字符集
sed -i "$ a character_set_server=utf8" /etc/my.cnf

# 查看初始化后root的密码
passwd=$(awk '/password/ {print $NF}' /var/log/mysqld.log)

# 启动mysql
systemctl start mysqld

echo "mysql root passwd: $passwd"



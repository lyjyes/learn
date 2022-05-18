#!/bin/bash
# jenkins工程拉取代码的目录或者代码目录
code_dir="/var/lib/jenkins/workspace/monitor"
# 打包的时间戳文件名
date=web-$(date +%F-%H-%M-%S)

# 用于打包的函数
code_tar(){
    cd ${code_dir} && tar zcf /opt/${date}.tar.gz ./*
}

# 用于远程发送文件的函数
code_scp(){
    scp /opt/${date}.tar.gz usa_server:/opt/code
}

# 用于远程解压的函数
code_zxf(){
    ssh usa_server "mkdir /opt/code/${date} && tar zxf /opt/code/${date}.tar.gz -C /opt/code/${date}"
}

# 用于远程创建软链接的函数
code_ln(){
    ssh usa_server "cd /usr/share/nginx/ ; rm -rf monitor && ln -s /opt/code/${date} /usr/share/nginx/monitor "
}

# 主函数，用于跑函数
main(){
    code_tar;
    code_scp;
    code_zxf;
    code_ln;
}

main
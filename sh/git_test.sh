#!/bin/bash
# 进入项目
cd /d/learngit/test_dev
# 新建分支
git branch beta
# 切换分支
git checkout beta
# 添加文件
echo "test sh to git push" >> test.txt
# 本地提交
git add .
git commit -m "add file" 
# 拉取master最新资源
git pull origin master
# 切换回master
git checkout master
# 合并分支
git merge beta -m "add file"
# 上传
git push origin master
# 删除beta分支
git branch -d beta
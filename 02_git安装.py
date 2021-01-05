安装
sudo apt-get install git

git 可以看见命令

2）运行如下命令

3)创建版本库，初始化
git init

(bj18_py3) yyc@yyc-Lenovo-G50-45:~/bj18/git_test$ git init
已初始化空的 Git 仓库于 /home/yyc/bj18/git_test/.git/


4） 版本创建和回退
1---   git add code.txt

2----  git commit -m '版本'
# git commit -m '版本一'
-m 后面是版本信息
查看版本记录
git log



HEAD版本
HEAD^前一个版本
HEAD^^ 前两个版本
HEAD~1 当前版本前一个版本
HEAD~100 当前版本前100个版本

git reset --hard HEAD^  # 回到上一个版本


git reser --hard 版本编号  # 回到前面更新的版本


gir reflog 查看前面的操作

git status查看分支



管理修改  它只会提交暂存区的修改创建版本


6) git 撤销修改

1----

git checkout -- 文件名  # 丢弃工作区改动

2-----

如果加到暂存区
取消暂存 git reset HEAD 文件名


7)-------对比文件的不同

1---
对比工作区的文件和版本库的文件不同
git diff HADE -- 文件名字

---  对应HADE 版本
+++  对应工作区的


2----对比两个版本的不同
对比HEAD 和HEAD前一个版本文件名的区别
git difff HEAD HEAd^ -- 文件名


对比 HEAD前一个版本  和现在版本的文件区别

git diff HEAD^ HEAD -- 文件名



8)-----删除文件

1---
rm 文件名

# git checkout -- 文件名  可以丢弃改动
2---
把删除的改动放到暂存区
git rm 文件名

# 想回来先取消暂存
git reset HEAD 文件名
然后再丢弃改动 git checkout 文件名


要删除要提交修改

git rm 文件名,删除进暂存区
git commit -m "删除"



git log --pretty=oneline # 简短的显示版本


--------------------------------git  分支管理

概念 两条流水线、平行宇宙..

创建分支
git 每次提交时间线
主分支HEAD 先指向现在的master（主分支）然后指向版本

# git branch查看分支

创建新的分支
git checkout -b dev  
切换到一个新分支 dev
# 新建一个指针dev指向这个新分支，切换就是HEAD指向这个分支的dev

切换
git checkout master

# 合并分支.快速合并 把HEAD往前移动
git merge dev


#  删除分支

git braach -d dev
删除dev分区



# 解决冲突
git status 找到冲突文件
手动修改然后
git add 文件名
git commit -m '解决冲突'

查看分支情况
git log --graph --pretty=oneline

----分支管理策略

git merge dev  # dev分支 合并分支
合并时不能快速合并。在谈窗输入说明

git merge --no--ff -m '禁止用快速合并，新的提交'  dev


#-------------bug 分支

每一个bug通过一个新的分支修复，修复后合并

git 提供一个stash 功能

----
git branch 查看分支
git checkout -b dev 创建分支

git status 查看

git stash 把工作现场保存

-----切换到出bug分支

--创建零时分支
git checkout -b bug-001

修复bug
在bug-001提交
git commit -m '修复bug'

回到分支，合并
# git checkout master 切换分支,看不出
应该禁止快速合并
git merge --no--ff -m '修复bug' bug-001

删除bug-001分支
git branch -d bug-001

回到分支dev
git status

git stash list 保存工作现场列表
恢复
git stash pop 回到工作现场


#  ----githbu 创建仓库
yycyyccc

分布式
中央服务器保存完整代码

去git官网注册然后登入

--创建藏库  NEW....
仓库描述

默认public每个人可以看到
private 收费的

Insitalize....readme 创建redeme文件

add.gitgnoe...选择python忽然。pyc

github添加ssh账户
点击账户头像下拉三角  settings
--
SSH and GPG keys.

new ssh KEY

把电脑ssh公钥复制过来

在～ 下vim .gitconfig

--------------------------------------
[user]
    email = 邮箱
    name = 用户名

[user]
        email = 1050653794@qq.com
        name = yycyyyccc
----------------------------------------
# 创建公钥
ssh-keygen -t rsa -C '邮箱'
。。。告诉文件路径，两次回车就行

ssh-keygen -t rsa -C 1050653794@qq.com


cd .ssh
id_rsa 私钥
cat id_rsa.pub 查看公钥，复制到网站添加公钥

#-----克隆项目

在git首页，cloe or downlad
  use ssh
  复制地址

cd bj18
git clone 复制的地址  #  复制到当前文件夹

克隆出错,执行这两句
eval "$(ssh-agn -s)"
ssh -add



上传分支

git checkout -b smart 创建smart分支
git status查看分支


git add views.py 
git commit -m '创建视图'

提交本地


推送。。。。。
git push origin 分支名称

本地分支跟踪远程
git branch --set-updtream-to=origin/smart smart
设置smart跟踪远程的smart

修改后提交
git commit -m ''

远程拉取

git pull origin smart 
把远程分支拉取smart代码




#------------列表
列表元素类型为string

按插入顺序排序

#-增加
lpush a1  a b c

左侧插入
lpush key value1 value2....

右侧插入
rpush key value1 value2...

在。。之前插入
linsert a1 before b 3 # 往a1 key b的前面添加 3


lrange a1 0 5  #  a1 key 里面下标0---5的数据

#  获取

返回列表范围内的元素
start、stop为元素下标索引

索引从左侧开始，第一个元素为0


索引可以的负数，表示从尾部开始计数， 如-1 表示最后一个元素
lrange key start stop 

取键值为a1的列表所有元素

lrange a1 0 -1

# 设置制定索引位置的元素的值

lset key index value

修改建wei  a1 列表中下标为1的与元素值为z


lset a1 1 z

#  ----------删除

删除指定元素

将列表中前count此书出现的值为value的元素移除
count > 0; 从头往尾移除
count < 0; 从尾往头移除
count = 0; 移除全部

lrem key count value

lrem a2 -2 b  # 从a2键值 列表后往前移除2个b

#-------------------set 集合类型

无序集合
元素weistring类型
元素具有唯一性，不重复
说明: 对于集合没有修改操作

增加

添加元素
sadd key member1 member2....


获取
返回所有元素
smembers key

删除

srem key 元素 元素2

#------------zst
有序集合
string类型
元素具有唯一性，不重复性
每个元素都会关联一个double类型的score 表示权值，通过权值将元素从小到大排序
没有修改操作

增加

zadd key score1 member score2 member2


#  向键a4 的集合中添加元素 list wangwu zhangsan 权值分别为4 5 6
zadd a4 4 list 5 wangwu 6 zhangsan


#------------获取

返回指定范围的元素
start stop为元素的下标索引
索引从左边开始，第一个元素为0

索引可以是负数表示从尾部开始计数，如-1表示最后一个元素

zrange key start stop


返回score 值在min和max之间的成员
zrangebyscore key min max

返回成员member的权值

zscore a4 zhangsan  #  获取a4 里面zhangsan的权值


#======删除

zrem key member1 member2.....

zrem a4 zhangsan 删除zhangsan
zrange a4 0 -1 查看


zremrangebyscore key min max  
删除指定范围
zrmreangebyscore a4 5 6  # 删除权值5--6之间的元素，删除5和6 


---# 

#====================================================
git branch 查看分支
git push origin smart 推送到远程


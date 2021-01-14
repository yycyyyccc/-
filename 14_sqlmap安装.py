ubuntu16.04安装sqlmap
以下操作步骤都是搜索出来的，组合起来，存档以备日后再次需要配置

----

1、首先登陆Ubuntu系统中，使用su然后切换到超级用户，输入root的密码

2、然后进入到/opt目录下

cd /opt

3、安装git

apt-get install git

4、然后使用git安装sqlmap

git clone git://github.com/sqlmapproject/sqlmap.git

5、等到看到有“done”字样的提示

6、修改一下环境变量

sudo vim /home/pw/.bashrc

在最后面加上

alias sqlmap=‘python /opt/sqlmap/sqlmap.py’

7、全局变量也要改

sudo vim /etc/profile

同样是在最后加上

alias sqlmap=‘python /opt/sqlmap/sqlmap.py’

8、打开一个新到终端，运行sqlmap验证是否正确安装

好文要顶 关注我 收藏该文  
扎古_白色食人魔
关注 - 0
粉丝 - 0
+加关注
00


=================================================

-h 显示基本帮助信息并且退出
-hh 显示高级帮助信息并退出


sqlmaqp 针对-URL 探测，参数使用-u  或 --url
例如 sqlmap

 python sqlmap.py -u '127.0.0.1:666/less-1/?id=1' --banner




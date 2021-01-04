
wget http://download.redis.io/releases/redis-4.0.9.tar.gz


sudo mkdir /usr/local/redis

sudo tar -zxvf redis-4.0.9.tar.gz -C /usr/local/redis


然后sudo make 编译


# 没用
#wget http://downloads.sourceforge.net/tcl/tcl8.6.1-src.tar.gz
#tar xzvf tcl8.6.1-src.tar.gz  -C /usr/local/
#cd  /usr/local/tcl8.6.1/unix/
#./configure
#make
#make install


# 成功
sudo apt install -y tcl

sudo make test

安装，将redis的命令安装到/usr/local/bin/目录
sudo make install


redis-server 是redis服务器
redis-cli redis命令行客户端
resid-benchmark  redis性能测试工具
redis-check-rdb  RDB文件检索工具
redis-check-aof  AOF文件修复工具

#  配置文件，移动到/etc/目录下
# 配置文件目录为/usr/local/redis/redis.conf

sudo cp redis.conf /etc/redis/redis.conf


绑定ip 如果需要远程访问，可以注释这行，或绑定真实ip

bind 127.0.0.1


端口 默认为6379


是否守护进程运行

    如果以守护进程运行，则不会在命令行堵塞，类是于服务
    如果以非守护进程运行，则当前爱终端堵塞
    设置为yes表示守护进程，设置为no表示非守护进程
    推荐设置为yes
    daemonize yes


数据文件
dbfilename dump.rdb   存数据的
数据文件存路径

dir /var/lib/redis  # 先创建redis

日志文件
logfile  /var/log/redis/redis-server.log

数据库,默认16个数据库

databases 16 


主从复制，类似于双机备份
slaveof

#---------------------------------

这个是默认的启动方式，我们使用制定配置文件
启动redis

推荐使用服务的方式管理redis服务
启动
sudo service redis start

停止
sudo service redis stop

重启 
sudo service redis restart

个人习惯
ps -ef|frep redis 查看服务器进程


#-------------------------------------------------

制定配置文件启动
sudo redis-server /etc/redis/redis.conf


查看进程
ps aux | grep redis


关闭
sudo kill -9 pid 杀死redis服务器

------------------------客户端

redis-cli --help

-h 连接ip
-p 指定端口

连接
redis-cli

ping 回复
PONG

默认链接是0号数据库

切换数据库  5号
select 5



#---------------redis 数据类型

redis是key-value的数据结构，每条数据都是一个键值对
键值的类型是字符串
注意:键不能重复


值   五总类型

字符串string

哈希 hash

列表list

集合set

有序集合zset

数据操作为
保存

修改

获取

删除


#---string类型

最基础的类型，特色redis中是二进制安全的，可以存图像和JPEG图像，任何格式
容纳最大长度的512M


设置键值
set key value 不存在创建，存在修改

设置键值过期时间，秒为单位

setex key aa 3 aa

setex key 键 秒 值

-----设置多个对个键值
mset key1 value1 key2 vakue2



追加值
append a1 haha
往key a1 添加haha


获取多个值
mget a1 a2 a3

删除

健命令
查找建，参数支持正则

keys pattern


查看所有
keys *

a开头的
keys 'a*'


判断
exists 

EXISTS a1


type key 查看key的类型


删除建和对应值

del a1

del a2 a3


ttl key
 看过期时间


 hash类型

 hash用于存对象，对象结果为 属性、值

值为 string

设置但个数学
hset key field name

hset user name ithemiam

hmset key field11 vlue1 field2 value2 
          属性一  建值1

hget  u2 'name'

hmget u2 name age

看key对应所有属性值

hvals u2

删除整个hash  使用del

删除
hdel u2 age
删除u2建的属性  age值




# redis 与python 交互

pip install redis


通过init 创建的对象,指定参数host、post 与指定的服务器和端口连接，host 默认为
localhost， post默认为6379， db 默认为0

sr = StrictRedis(host='localhost', post=6379, db=0)

简写
sr = StrictRedis()


django 存储session
之前django 的session默认是存在的数据库里面的，我们也可以把session存储在redis里面

准备工作
创建test5 项目和booktest应用

# session 的redis 存储配置

安装包
pip install django-redis-sessions==0.5.6

创建项目
创建应用

在setting 配置mysaql
还有


# 设置redis存储session信息
SESSION_ENGINE = 'redis_sessions.session'
# 服务器的ip地址
SESSION_ENGINE_HOST = 'localhost'
# 服务器端口
SESSION_REDIS_PORT = 6379
# 连接哪个数据库
SESSION_REDIS_DB = 2
SESSION_REDIS_PASSWORD = ''
# 唯一标识玛作为键
SESSION_REDIS_PREFIX = 'session'


搭配主从

查看主机ip
ifconfig

sudo vim /etc/redis/redis.conf

bind 127.0.0.1
改为
bind 查到的ip


启动redis服务

sudo redis-server /etc/redis/redis.conf

ps -axu |grep redis

配置从

cd /etc/redis/

sudo cp redis.conf slave.conf

vim slave.conf
编辑
bind ip
port改变下

# slaveof <masterip> <masterport>
slaveof 192.168.31.158 6379
配置主服务器
# 启动从服务器
sudo redis-server /etc/redis/salve.conf

redis-cli -h 192.168.31.158 -p 6379 info Replication


# Replication
role:master  # 主服务器
# 从服务器有一个
connected_slaves:1
# 从服务器ip             端口
slave0:ip=192.168.31.158,port=6378,state=online,offset=210,lag=0

master_replid:1664c6cb94350821d27ca78a34ef6e034c14b658
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:210
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:210

celery -A celery_tasks.tasks worker -l info
启动celery中间人

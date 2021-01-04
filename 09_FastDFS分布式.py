什么是FastDFS
c语言写的，开源的分布式文件系统,文件上传，下载的服务

通过Tracker server调度 和 Storage server 完成文件上传下载

django 默认的上传在 MEDA_ROOT = os.path,jion(BASE_DIR, 'static/media')

FastDFS安装
安装fastdds依赖包
解压   fastdfs-master.zip
为了解压 zip 归档文件，必须先在Linux系统上安装unzip 软件包。大多数Linux 发行版本提供了解压 zip 文件的支持，但是对这些 zip 文件进行校验以避免以后出现损坏总是没有坏处的。

在基于Unbutu和Debian的发行版上，可以使用下面的命令来安装 unzip：

sudo apt install unzip

解压两个文件 sudo ./make.sh 编译 然后

#--------------------------
配置跟踪服务器 tracker
在 etc/fdfs/
mkdir -p fastdfs/tracker 在家目录下
复制sudo cp tracker.conf.sample tracker.conf
# 修改tracker.conf
base_path=/home/yyc/fastdf/tracker
#----------------------------------

#--------------
配置存储服务器 storage
sudo cp storage.conf.sample storage.conf
mkdir -p fastdfs/storage
# 修改storage.conf
base_path=/home/yyc/fastdfs/storage

store_path0=/home/yyc/fastdfs/storage

tracker_server=192.168.31.158:22122

#-------------------------------------
启动
fdfs_trackerd /etc/fdfs/tracker.conf start

fdfs_storaged  /etc/fdfs/storage.conf start



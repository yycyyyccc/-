安装nginx 及 fatsdf_nginx-module   web服务器  epoll
1. 解压缩nginx-1.8.1.tar.gz
2. 解压缩fastdfs-nginx-module-master.zip    
3. 进入 nginx-1.8.1 目录中
4. 执行

sudo ./configure --prefix=/user/local/nginx/ --add-module=fastdfs-nginx-module-master 解压后的目录绝对路径/src
    
sudo ./configure --prefix=/user/local/nginx/ --add-module=/home/yyc/bj18/fastdfs-nginx-module-master/src

sudo apt-get install libpcre3 libpcre3-dev  解决缺失pcre包


此处说明运行make时 其编译的函数发生措错误，查阅了网上大量资料发现均是说把 objs/Makefile 文件中的-werror 删除，可是发现其实根本没用。最后在放弃前一刻 想了一下是不是源代码的问题。 果然 在源代码**/nginx-1.12.2/src/os/unix/
```/ngx_user.c** 文件中 修改
#ifdef_GIBC_
    /*......*/
    /*......*/

    #最后一步：
将对应的makefile文件夹中（如本文中在 /nginx-1.12.2/objs/Makefile） 找到 -Werrori 并去掉 在重新 回到nginx主目录 make即可


(bj18_py3) yyc@yyc-Lenovo-G50-45:~/bj18/fastdfs-nginx-module-master/src$ sudo cp mod_fastdfs.conf /etc/fdfs/mod_fastdfs.conf 
拷贝配置文件

connect_timeout=10  # 连接超时时间
tracker_server=192.168.31.158:22122
url_have_group_name = true  # 保存路径带组信息
store_path0=/home/yyc/fastdfs/storage


(bj18_py3) yyc@yyc-Lenovo-G50-45:~/bj18/fastdfs-master/fastdfs-master/conf$ sudo cp http.conf /etc/fdfs/http.conf
(bj18_py3) yyc@yyc-Lenovo-G50-45:~/bj18/fastdfs-master/fastdfs-master/conf$ sudo cp mime.types /etc/fdfs/mime.types


修改 /user/local/nginx/conf nginx.conf 

    server {
        listen       8888;
        server_name  localhost;
        location ~/group[0-9]/ {
                ngx_fastdfs_module;
        }
        error_page 500 502 503 504 /50x.html;
        location =  /50x.html {
            root   html;
        }
    }

=====================================================================
    yyc@yyc-Lenovo-G50-45:/user/local/nginx/sbin$ ps aux |grep nginx  # 查看

    yyc@yyc-Lenovo-G50-45:/user/local/nginx/sbin$ sudo ./nginx  # 启动
    ngx_http_fastdfs_set pid=50405  

    sudo ./nginx -s stop  # 停止

    启动完成在浏览器访问http://127.0.0.1:8888/group1/M00/00/00/wKgfnl_ytUKAKg8RADAJoP6zfUE272.png   # 可以获取之前存的图片



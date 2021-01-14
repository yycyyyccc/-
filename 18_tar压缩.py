
压缩
tar -zcf *

1 # tar -cvf test.tar test 仅打包，不压缩 
2 # tar -zcvf test.tar.gz test 打包后，以gzip压缩 在参数f后面的压缩文件名是自己取的，习惯上用tar来做，如果加z参数，
3 则以tar.gz 或tgz来代表gzip压缩过的tar file文件


解压：
tar -xvf test.tar.gz 


tar 解压缩命令详解

1 -c: 建立压缩档案
2 -x：解压
3 -t：查看内容
4 -r：向压缩归档文件末尾追加文件
5 -u：更新原压缩包中的文件

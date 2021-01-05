workon bj18_py3

安装一个包fdfs client-py-master
(bj18_py3) yyc@yyc-Lenovo-G50-45:~/bj18$ unzip fdfs_client-py-master.zip
解压
这里报错版本太低，直接下面命令

pip install py3Fdfs
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from fdfs_client.client import Fdfs_client, get_tracker_conf
>>> tracker_path = get_tracker_conf('/etc/fdfs/client.conf')
>>> client = Fdfs_client(tracker_path)
>>> ret = client.upload_by_filename('./test')
>>> print(ret)
{'Group name': b'group1', 'Remote file_id': b'group1/M00/00/00/wKgfnl_z4IuAO4FrAAAABr99wgM4277861', 'Status': 'Upload successed.', 'Local file name': './test', 'Uploaded size': '6B', 'Storage IP': b'192.168.31.158'}
>>> 


默认上传文件

通过一个自定义一个存储类必须是Storage的子类




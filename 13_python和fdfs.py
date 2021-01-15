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

@deconstructible
class FDFSStorage(Storage):
    """fast dfs 文件存储类"""

    def _open(self, name, mode='rb'):
        """打开文件时候使用"""
        pass

    def _save(self, name, content):

        # 选择上传文件名字，content是File的一对象 包含上传文件
        tracket_path = get_tracker_conf('./utils/fdfs/client.conf')  # 路径相对项目dailyfresh
        client = Fdfs_client(tracket_path)
        print(content)
        print(type(content))

        # 上传文件
        try:
            # input()
            print('检测是否出错')
            res = client.upload_appender_by_buffer(content.read())

        except Exception as result:

            print('异常%s' % result)




        """
        
        dict
        {
            'Group name': group_name,
            'Remote file_id': remote_file_id,
            'Status': 'Upload successed.',
            'Local file name': '',
            'Uploaded size': upload_size,
            'Storage IP': storage_ip
        }
        """
        if res.get('Status') != "Upload successed.":
            # 上传失败
            print(res.get('Status'))
            print(res)
            # filename = res.get('Remote file_id')

            raise Exception('上传文件到fast dfs 失败')
        else:
            # 获取返回的ID
            filename = res.get('Remote file_id')
            return filename.decode()

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 记得decode不然会报错__str__ returned non-string (type bytes)        
return filename.decode()


还有记得启动
fdfs_trackerd /etc/fdfs/tracker.conf start

fdfs_storaged  /etc/fdfs/storage.conf start

不然也报错

decode查至https://www.cnblogs.com/canghai1024/p/13069198.html
作者：沧海1024
本文链接：https://www.cnblogs.com/canghai1024/p/13069198.html
关于博主：评论和私信会在第一时间回复。或者直接私信我。
版权声明：本博客所有文章除特别声明外，均采用 BY-NC-SA 许可协议。转载请注明出处！




   def _save(self, name, content):
        # 选择上传文件名字，content是File的一对象 包含上传文件
        input('===========================')
        tracket_path = get_tracker_conf('./utils/fdfs/client.conf')  # 路径相对项目dailyfresh
        client = Fdfs_client(tracket_path)
        print(content)
        print(type(content))

        # 上传文件
        try:
            
            print('检测是否出错')
            res = client.upload_appender_by_buffer(content.read())

        except Exception as result:

            print('异常%s' % result)
        """
        
        dict
        {
            'Group name': group_name,
            'Remote file_id': remote_file_id,
            'Status': 'Upload successed.',
            'Local file name': '',
            'Uploaded size': upload_size,
            'Storage IP': storage_ip
        }
        """
        if res.get('Status') != "Upload successed.":
            # 上传失败
            print(res.get('Status'))
            print(res)
            # filename = res.get('Remote file_id')

            raise Exception('上传文件到fast dfs 失败')
        else:
            # 获取返回的ID
            filename = res.get('Remote file_id')
            return filename.decode()

这是上传成功的



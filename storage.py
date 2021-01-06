from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client, get_tracker_conf
from dailyfresh import settings
from django.utils.deconstruct import deconstructible


@deconstructible
class FDFSStorage(Storage):
    """fast dfs 文件存储类"""

    def _open(self, name, mode='rb'):
        """打开文件时候使用"""
        pass

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

    def exists(self, name):
        """Django判断文件名是否可用"""
        # 用nginx所以文件名不会重复所以让他一直False 如果 为True则文件名存在
        return False

    def url(self, name):
        """访问文件url的路径"""
        return name


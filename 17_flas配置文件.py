在项目文件创建settings.py
class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'sagagawg'

在要用的test.py文件
app.config.from_object("settings.类名")

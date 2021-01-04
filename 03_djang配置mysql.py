mkvirtualenv -p python3 虚拟环境名字

创建新项目


django-admin startproject test2

创建应用
python manage.py startapp booktest

注册应用
在test  booktest里
setting.py
在INST。。。__APP里面配置





在
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'bj18',  # 使用数据库名字，数据库必需手动创建
        'USER': 'root',     # 连接mysql数据库用户名
        'PASSWORD': 'toor',  # 用户对应密码
        'HOST': 'localhost',  # 制定mysql所在电脑ip
        'POST': 3306,  # 端口

    }
}

在项目同名的文件夹下 __init__.py 加入

先 pip install pymysql


import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()


在model里建

from django.db import models

# Create your models here.
"""
    1.定义模型类
    2.模型迁移
        2.1先生成迁移文件(不会在数据库中生成表，只会创建一个数据表和模型的对应关系)
            python manage.py makemigrations
        2.2再迁移(会在数据库中生成表)
            python manage.py migrate
    3.操作数据库

    在哪里定义模型
    模型继承自谁都可以
    orm对应的关系
        表-》类
        字段-》属性
    """


class BookInfo(models.Model):
    """
   1.主键 当前会自动生成
   2.属性复制过来就可以
    """

    name = models.CharField(max_length=10)

    def str(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo)


然后生成迁移文件，在项目文件中
python manage.py makemigrations

python manage.py migrate


配置url  在应用中创建url.py
在项目url.py 中
"""
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('booktest.urls'))  # 包含booktest里面的url，匹配先来这里，然后再去booktest里面urls找
]

然后在新创的url.py中
from django.conf.urls import url, include
from booktest import views



urlpatterns = [
    url(r'^index$', views.index),


]

在views.py中

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
"""
视图
1.就是python函数
2.函数的第一个参数就是 请求 和请求相关的 它是 HttpRequest的实例对象
3.我们必须要返回一个对应     相应是 HttpRequest的实例对象/子类实例对象
"""


def index(request):
    name = '如花'
    # request,template_name,context=None
    # 参数1，当前的请求
    # 参数2，模板文件
    return render(request, 'index.html')
    return HttpResponse('index')


设在模板目录在setting.py中

import os
from pathlib import path

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #  设在模板路经
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

# ---在项目test1 文件夹创建templates文件夹
# --templates 文件夹下创建应用同名文件夹
# 在booktest创建index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>主页</title>
</head>
<body>
<h1>hello word!<h1/>
</body>
</html>


在views.py中

from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from booktest.models import BookInfo

# Create your views here.
"""
视图
1.就是python函数
2.函数的第一个参数就是 请求 和请求相关的 它是 HttpRequest的实例对象
3.我们必须要返回一个对应     相应是 HttpRequest的实例对象/子类实例对象
"""


def index(request):
    book = BookInfo()
    book.name = '如花'
    book.save()
    # request,template_name,context=None
    # 参数1，当前的请求
    # 参数2，模板文件
    return render(request, 'booktest/index.html')


# 本地化，在setting.py

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'


# 创建管理员



python manage.py createsuperuser


登入后台


# 注册模型类
# 在admin.py 文件注册
from django.contrib import admin
from booktest.models import BookInfo
# Register your models here.
admin.site.register(BookInfo)



class BookInfo(models.Model):
    """
   1.主键 当前会自动生成
   2.属性复制过来就可以
    """

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name




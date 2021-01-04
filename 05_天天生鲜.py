新建项目 test1
app   booktest


注册app
创建模板目录templates
拼接路径
连接数据库

ifconfig

sudo vim /etc/mysql/mysql.conf.d/mysql.cnf

/bind-address = ip（远程ip）

sudo server mysql restart

--------------------
mysql -uroot -p

授权
grant all privileges on test2.* to 'root'@'192.168.31.15' identified by 'toor' with grant option;
# 给权限                 数据库test2  root在ip 远程连接  用的密码是toor

flush privileges;  # 授权生效

迁移



# -----------------------------------------------------

副文本
tinymce 编辑器

pip install django-tinymce==2.6.0

在项目文件中setting.py

INSTALLRD_APPS = {
    .....,
    'tinymce',  # 副文本编辑器


        }

# 副文本编辑器
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'dvanced',  # 主题，高级
    'widith': 600,
    'height': 400,

        }


在项目文文件urls.py
urlpatterns = {
    url(r'^tinymce/', include('tinymce.urls')),

        }


# -----------------------------------------
django-admin startproject dailyfresh

python manage.py startapp cart
----cart
----goods
---order
---user

在dailyfresh中建一个python 包apps  把应用都放进这个文件夹

注册app  在setting.py


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.cart', 
    'apps.goods',
    'apps.order',
    'apps.user',
]

或则
import os
import sys
               第0个位置，目录和apps拼接
               # BASR_DIR 是项目的绝对路径
sys.path.insert(0, os.path.jion(BASR_DIR, 'apps'))

# 这样注册app就可以 直接 'cart'


创建templates
配置
'DIRS': [os.path.join(BASE_DIR, 'templates')],
创建static
配置
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

#--------------------------------
{% load static %}
# static目录
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>天天生鲜-注册</title>                # static目录下的'css/下的...'
	<link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/main.css' %}">
	<script type="text/javascript" src="{% static 'js/jquery-1.12.4.min.js' %}"></script>


# celery 异步发送邮件
任务队列(中间人) broker

redis 可以作中间人
--1
安装包 pip install celery

项目文件下新建一个python的包 celert_tasks 在文件创建tasks.py文件

from celery import Celery
from dailyfresh import settings
from django.core.mail import send_mail
# 创建一个Celery实例对象
app = Celery('celery_tasks.task', broker='redis://192.168.31.158:6379/8')  # 指定redis地址端口。后面8号数据库


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    """发送邮件"""
    # 发邮件
    # 发邮件
    subject = '天天生鲜欢迎信息'
    message = ''
    html_message = '<h1>%s, 欢迎您成为天天生注册会员</h1> 请点击下面连接激活您的账号<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
    username, token, token)
    # 发件人1
    receviver = [to_email]
    sender = settings.EMAIL_FROM
    send_mail(subject, message, sender, receviver, html_message=html_message)


在view.py调用 send_register_active_email.delay(email, username, token)  # .delay传参数  发出人物


# 处理着也需要人物代码。复制项目

报错因为redis这没有使用django配置项，没有初始化
在tasks


import os
import django
# 创建一个Celery实例对象
app = Celery('celery_tasks.task', broker='redis://192.168.31.158:6379/8')  # 指定redis地址端口。后面8号数据库
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
django.setup()
添加到处理者
@app.task
def send_register_active_email(to_email, username, token):
    """发送邮件"""
    # 发邮件
    # 发邮件
    subject = '天天生鲜欢迎信息'
    message = ''

    # 发件人1
    sender = settings.EMAIL_FROM
    receiver = [to_email, sender]  # sender 添加不然会报错认为是垃圾邮件
    html_message = '<h1>%s, 欢迎您成为天天生注册会员</h1> 请点击下面连接激活您的账号<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
        username, token, token)
    send_mail(subject, message, sender, receiver, html_message=html_message)



# 用户登入

from django.contrib.auth import authenticate
# 这个有bug authenticate一直返回NOne

from django.contrib.auth.hashers import check_password

#--------------------------------------
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
import re
from user.models import User
from dailyfresh import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password


def register(request):  # /user/register
    """显示注册页面"""
    if request.method == 'GET':
        # 显示注册页面
        return render(request, 'register.html')
    else:
        # 进行注册
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据的校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 进行业务处理

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            User.objects.get(username=username)
            # 用户名存在
        except User.DoesNotExist:
            # 用户不存在
            user = None
        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名存在'})
        # 用户注册
        user = User.objects.create_user(username, email, password)
        # 返回应答,跳转首页
        user.is_active = 0
        user.save()
        #                反向解析
        return redirect(reverse('goods:index.html'))


class RegisterViews(View):
    """注册"""
    def get(self, request):
        """显示注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """进行注册处理"""
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据的校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 进行业务处理

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
            # 用户名存在
        except User.DoesNotExist:
            # 用户不存在
            user = None
        if user:
            # 用户名已存在
            return render(request, 'register.html', {'errmsg': '用户名存在'})
        # 用户注册
        user = User.objects.create_user(username, email, password)
        user.set_password(password)
        # 返回应答,跳转首页
        user.is_active = 0
        user.save()
        # 发送邮件激活，包含激活连接 http://127.0.0.1:8000/user/active/1
        # 把身份信息加密is'dangerous 加密身份信息，生成激活的token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        token = token.decode('utf8')
        # 发邮件
        send_register_active_email.delay(email, username, token)

        #                反向解析
        return redirect(reverse('goods:index'))


class ActiveView(View):
    """用户激活"""
    def get(self, request, token):
        # 进行用户激活
        # 进行解密，获取要激活的用户信息
        serializer = Serializer(settings.SECRET_KEY, 3600)
        # print(token)
        try:
            info = serializer.loads(token)  # 解密
            # 获取代激活用户id
            user_id = info['confirm']
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 激活返回应答,跳转登入 反向解析
            return redirect(reverse('user:login'))
            # return HttpResponse('123')
        except SignatureExpired as e:
            # 激活连接过期
            return HttpResponse('激活连接已经过期')

# user/login
class LoginView(View):
    """登入"""
    def get(self, request):
        # 显示登入页面
        return render(request, 'login.html')

    def post(self, request):
        """d登入校验"""
        # 接受和数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        # 校验数据
        print('%s,%s,%s' % (username, password, all([username, password])))
        if not all([username, password]):
            print('===============')
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理,内置校验函数，正确返回user对象
        # user = authenticate(username=username, password=password)  # 一直返回none
        try:  # 以下重点！！！！！！！！！！！！！
            user = User.objects.get(username=username)
            pwd =user.password
            if check_password(password, pwd):
                if user.is_active:
                    # 用户激活
                    # 记住登入状态
                    login(request, user)
                    # 跳转主页
                    return redirect(reverse('goods:index'))

                else:
                    return render(request, 'login.html', {'errmsg': "账户没激活"})
                    # print('The password is valid, but the account hans benn disabled ')
            else:
                # 密码用户名错误
                return render(request, 'login.html', {'errmsg': '用户名或则密码错误'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'errmsg': '没有用户'})

        # 返回应答
#======================================================================


# 配置redis作为Django的缓存和session存储后端

使用django_redis包
pip install django-redis

在setting.py 缓存设置


# django缓存配置
CACHES = {
    "default": {
        'BACKEND': "django_redis.cache.RedisCache",
        'LOCATION': "redis://192.168.31.158:6379/9",
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# 配置session存储
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

====================
记住用户名


class LoginView(View):
    """登入"""
    def get(self, request):
        # 显示登入页面
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        # 使用模板
        return render(request, 'login.html', {'username': username, 'checked': checked})

然后在login.html
username 表单加入value='{{ username }}'

<input type="checkbox" name="remember" {{ checked }}>

#================================================================

父模板

在templeats复制index.html（比较典型）改名为base.html


# login_required 装饰器
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^register$', views.register, name='register'),
    # url(r'^register_handle', views.register_handle, name='register_handle')
    url(r'^register$', RegisterViews.as_view(), name='register'),
    url(r'^active/(.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 登入页面
    url(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心-信息
    url(r'^order$', login_required(UserOrderView.as_view()), name='order'),  # 订单
    url(r'^address$', login_required(AddressView.as_view()), name='address'),  # 用户中心-地址

]

在setting.py中
LOGIN_URL = '/user/login'

新建一个utils的python包  # 工具
新建一个minxin.py文件
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initwargs):
        # 调用父类as_view
        view = super(LoginRequiredMixin, cls).as_view(**initwargs)
        return login_required(view)
# 返回login_required() 包装的view
相当于 # url(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心-信息
login_required() 用来验证登入，如果不是登入状态默认跳转，在setting.py设置
LOGIN_URL = '默认跳转地址'
#========================  这个类作用调用super().as_view(**initwargs)就是view.py中继承LoginRequiredMixin这个类的 子类，super().as_view(**initwargs)调用继承的View的as_view方法
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""
    def get(self, request):
        """显示"""
        # page='user'
        # request.user.is_authenticated() 如果登入返回True
        return render(request, 'user_center_info.html', {'page': 'user'})

-------------------------------------------------------------------
# request.user.is_authenticated() 如果登入返回True

django 本生会给request增加request.is_authenticated属性

from django.contrib.auth import authenticate, login, logout

class LoginOut(View):
    """退出登入"""
    def get(self, request):
        """退出登入"""
        # 清除用户的session
        logout(request)

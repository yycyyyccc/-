pip install django==版本号


创建新项目

django-admin startproject test2

# test2创建应用
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
        'USER': 'root',       # 连接mysql数据库用户名
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

# python manage.py runserver 跑下试试


在model里建
from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """书本信息"""
    btitle = models.CharField(max_length=20)
    bpudate = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)

    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄人物"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    # 关系。外建
    #hbook = models.Foreignkey('BookInfo')
    # djiang2.0后需要制定on_delete 参数！！！！！！！！！！！！！！！
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

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
    url(r'^', include('booktest.urls'))
]

然后在新创的url.py中
from django.conf.urls import url, include
from booktest import views



urlpatterns = [
    url(r'^index$', views.index),


]

在views.py中
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.


def index(request):

    return HttpResponse('ok')


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

# ---在项目文件夹创建templates文件夹
# --templates 文件夹下创建应用同名文件夹
# 在booktest创建index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>显示图书信息</title>
</head>
<body>
<a href="/create">新增</a>
<ur>
        {% for book in books%}
               <li>{{ book.btitle }} <a href="delete">删除</a></li>
        {% endfor %}
</ur>
</body>
</html>


在views.py中
定义一个def create(request):
def create(request):
    """新增图书"""
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpudate = date(1995, 12, 12)
    book.save()
    # 3返回应答
    return HttpResponse('ok')

导入
from django.http import HttpResponse, HttpResponseRedirect  # 这是一个类
创建一个对象 地址作为参数

def create(request):
    """新增图书"""
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpudate = date(1995, 12, 12)
    book.save()
    # 3返回应答 重定向，返回类的对象让浏览器访问/index.html
    return HttpResponseRedirect('index.html')


index.html
删除功能
<ur>
        {% for book in books%}
               <li>{{ book.btitle }} <a href="/delete{{ book.id}} ">删除</a></li>
        {% endfor %}
</ur>

在urls.py中添加delde配置

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index.html$', views.index),
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^delete(\+d)$', views.delete) # 分组作为参数传递给，delete


]



在views.py中

def delete(request, bid):
    """删除图书"""
    book = BookInfo.objects.get(id=bid)
    book.delete()

    # return HttpResponseRedirect('/index')

from django.shortcuts import redirect  # 重定向和上面HttpResponseRedirect作用一样
    return redirect('/index')

查询
修改mysql 的日至文件
让mysql.log，即mysql日至文件，里面记录对mysql 的操作记录
1) 使用命令打开mysql的配置文件，去除68,69行的注释，然后保存
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
 56  general_log_file        = /var/log/mysql/query.log
 57  general_log             = 1



2) 重启mysql服务， 就会产生mysql日志文件
suodo service mysql restart

3）打开mysal的日志文件
/var/log/mysql/mysql.log 是日志所在位置
使用下面命令可以查看mysql的日志文件：
sudo tail -f /var/log/mysql/mysql.log



get 只查一条，只能返回一条
all 查所有返回值三 QuerySet  是一个查询集，  列表可以遍历
filter 返回满足的条件
exclude 返回不满足的条件
order_by 对查询结果排序

------------------------
filter 
条件格式
模型类的属性名__条件名=值

a）判等 条件名:exact
BookInfo.objects.get(id=1)

BookInfo.objects.get(id_exact=1)
b）模糊查询  contains
查询书名包含‘传’的图书 contains
BookInfo.objects.filter(btitle__contains='传')

查询结尾__endwith     开头__startswith

c)查询书名不为空的图书 isnull
select * from booktest_bookinfo where btitle is not ull


BookInfo.objects.filter(btitle__isnull=False)

d) 查询范围 in
select * from booktest__bookinfo where id in (1, 3 ,5);
BookInfo.objects.filter(id__in =[1, 3,5])

e) 比较查询
gt (greate than)   大与
lt (less than)   小于
gte (equal) 大于等于
lte  小于等于


f) 日期查询                     __moth=5 月
BookInfo.objects.filter(bpudate__year=1980)
查询1980，1，1后发行的图书
BookInfo.objects.filter(bpudate__gt=(1980,1,1)

排序BookInfo.objects.all().order__by('id') 大到小
排序BookInfo.objects.all().order__by('-id') 小到大
把id大于三的排序,阅读量小到大排序
BookInfo.objects.filter(id__gt=3).order__by('-bread')


Q对象
查询id大于3 且阅读量大于30
Bookinfo.objects.filter(id__gt=3, bread__gt=30)

查询id大于三或者阅读量大于30
from django.db.models import Q
BookInfo.objects.filter(Q(id__gt=3)|Q(bread__gt=30))

查询id不等于3   ~非
BookInfo.objects.filter(~Q(id=3))


F对象  用于类属性之间的比较
from django.db.models import F
                        bread 大于 bcomment
BookInfo.objects.filter(bread_gt=F('bcomment')

查询大于两倍
`
BookInfo.objects.filter(bread_gt=F('bcomment')*2)



聚合函数
sum  count avg max min
aggregate:使用这个函数聚合，返回值是一个字典

查询书的数目
from django.db.models import Count
BookInfo.objects.all().aggregate(Count('id'))
BookInfo.objects.aggregate(Count('id'))
{ 'id__count': 5}

图书阅读量总和
from django.db.models import Sum

Bookinfo.objects.aggregate(Sum('bread'))

Count 返回的是数字
查询id大于三书的数量
BookInfo.objects.filter(id__gt=3).count()

----模型类关系
1）一对多
models.Foreignkey()  定义在多的类中

2） 多对多
models.ManyToManyFied('类的名字') 定义在哪个类中都可以



3） 一对一关系
models.OneToOneField  定义在那个类中都可以

# 关系属性
employee__basic = models.OneToOneField('对应类的名字')


--关联查询

查询图书信息，要求图书关联中英雄的描述包含‘八’
BookInfo.objects.filter(heroinfo__hcomment__contains='八')

查图书信息，要求图书关联的英雄的id大于三
BookInfo.objects.filter(heroinfo__id__gt=3)

查询书名 天龙八部  所有英雄
HeroInfo.objects.filter(hbook__btitle='天龙八部')


查询id为1 的图书关联的英雄信息
HeroInfo.objects.filter(hbook__id=1)


---通过模型类实现关联查询时，要查哪个表中的数据，就需要通过哪个类来查
写关联查询条件时候，如果类中没有关系属性，条件需要写对应类的名字，如果类中
有关系属性，就直接写关系属性。


#-----------插入、更新和删除
调用一个模型类对象的save方法时候实现对模型类对应表
delete方法


#  ---------自关联

# 自关联是特殊的一对多关系
省--市--县

class AreaInfo(models.Model):

    atitle = models.CharField(max_length=20)
    # 自关联
    aParent = modes.Foreignkey('slef', null=Ture, blank=Ture)


一类查多类   b.heroinfo_set.all()
  一类的对象.多类名小写_set.all()  # 查询说有数据
多类查一类   h.hbook  关系属性

ajax: 异步的javascript
在不重新加载页面的情况下，对页面局部的刷新

$.ajax({
    'url':请求地址
    'type':请求方式
    'dataType':与其返回的数据格式
    'data':传参数
    }).success(function(data))({
    //回调函数
                
        })

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
    <script src="/static/js/jquery-1.12.4.min.js"></script>
    <script>
        $(function(){
            //绑定btnAjax的clik事件
            $('#btnAjax').click(function() {
                $.ajax({
                    'url':'/ajax_handle',
                    'type':'get',
                    'dataType':'json',

                }).success(function(data){
                    //进行处理
                    alert(data.res)
                })

            })
        })

    </script>


</head>
<body>

<input type="button" id="btnAjax" value="ajax请求">

</body>
</html>


view.py中

def ajax_test(request):
    """显示ajax页面"""
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    """ajax处理"""
    # 返回json数据{ 'res': 1}
    return JsonResponse({'res': 1})






----静态文件创建，在项目文件夹下，创建static文件夹

在settings.py中
SRATICFILES_DIRS = [os.path.join(BASE_DIR), 'static']


Cookie

1) 以建指对方式存储
2） 访问网站是，存储网站相关的关系会发送给服务器
3）浏览器发给服务器的cookie 保存在request对象的COOKIES指

设置cookie 需要一个HttpResponse类的对象







---模板标签

{%  代码段  %}

for 循环

{% for x in 列表   %}
# 列表不为空时执行

{% empty   %}

# 列表为空执行的代码

{% endfor    %}

可以通过{{ forloop.counter  }}  得到for循环遍历的第几次。

{% if 条件  %}
{% elif 条件  %}
{% else  %}
{% endif  %}

关系比较操作符: > < >= <= = !=

注意！！！ 进行比较操作时，比较操作符两边必须有空格

逻辑运算:  not  and  or 



——--csfg 攻击



# coding:utf-8
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/login',methods=['GET', 'POST'])
def login():
    print('请求来了')
    if request.method == 'GET':

        return render_template('login.html')


if __name__ == "__main__":
    app.run()

========================================================
__name__  作为启动模块就是 __main__

作为包被导入__name__就是模块名

app = Flask(__nam__,
        static_url_path='/python')  # 访问静态资源url前缀，默认值是static.. 
# 127.0.0.1:4000/python/index.html
# 127.0.0.1:4000/static/index.html 默认是static

stati_folder="static"  # 静态文件目录默认是static,可以改绝对路径，和上面的static_url_path区别在，这个指是__name__ 这个项目下的static目录是静态文件目录，static_url_path是url中有这个就去static_folder这个目录找资源

template_folder="templates"  # 模板文件目录，默认tmplates

--------------------------------
from flask import session
# 设置session
app.secret_key = 'afwagwgawgw'  # 加盐，加密
session['user_info'] = user  

del session['user_info']  # 删除session



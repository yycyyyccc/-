sudo pip install virtualenv
sudo pip install virtualenvwrapper
# 1
创建目录春芳虚拟环境
mkdir $HOME/.virtualenvs
# 2打开～/.bashc 文件添加
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
=========================================


mkvirtualenv -p 版本号 虚拟名

mkvirtualenv -p python3 env_1


退出虚拟环境 deactivate

rmvirtualenv 虚拟环境名

-------------------------------------------------

# 1 创建虚拟环境
 mkvirtualenv flask_py2

 安装的虚拟环境在./virtualenv 文件夹下


加了sudo 安装的包就不在虚拟环境了

pip list
pip freze > requirements.txt  把包名导入txt文件
pip instll -r requirements.txt 从这个文件一行一行的安装

## Refer
[知识目录](https://www.cnblogs.com/wupeiqi/articles/5237672.html)

## django 
### install
+ `pip3 install django`
### 创建django工程
`django-admin startproject 【工程名称】`
```
cd day18_djingo
django-admin startproject mysite
```
+ 运行
```
cd mysite
python manage.py runserver
python manage.py runserver 127.0.0.1:8001
```
+ 配置django server
在pycharm的的edit configuration，添加django支持，就直接运行即可
+ 目录结构
```
mysite
			- mysite        # 对整个程序进行配置
				- init
				- settings  # 配置文件
				- url       # URL对应关系
				- wsgi      # 遵循WSIG规范，uwsgi + nginx
			- manage.py     # 管理Django程序：
								- python manage.py 
								- python manage.py startapp xx
								- python manage.py makemigrations
								- python manage.py migrate
```
	
 + 创建app
 ```
python manage.py startapp cmdb
python manage.py startapp openstack
python manage.py startapp xxoo....
 ```
	
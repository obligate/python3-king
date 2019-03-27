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
 + app目录结构
 ```
 	app：
		migrations     记录修改表结构的记录
		admin          Django为我们提供的后台管理
		apps           配置当前app
		models         ORM,写指定的类  通过命令可以创建数据库结构
		tests          单元测试
		views          业务代码
 ```
	
+ admin 后台管理
     + cmdb.models.py添加类
     + day18_django_duli的settings.py中的INSTALLED_APPS,添加cmdb
     + 执行命令
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
     + 在cmdb的admin添加一下代码
        ```
            from cmdb import models
            admin.site.register(models.UserInfo)
            admin.site.register(models.UserType)
        ```
     +  执行命令`python manage.py createsuperuser` peter peter123456
     + 浏览器访问`http://127.0.0.1:8000/admin/`

### settings
#### 配置模板的路径
```
TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
```
#### 配置静态目录
```
		STATICFILES_DIRS = (
			os.path.join(BASE_DIR, 'static'),
		)
```

 +  html引用`<link rel="stylesheet" href="/static/commons.css" />`
		
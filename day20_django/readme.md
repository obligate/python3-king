## 创建django项目
+ 1.`python manage.py startapp app01`
+ 2.创建static 和 templates 目录
+ 3.修改settings
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
+ 4.在app01中添加一个函数
+ 5.在url中配置路由
+ 6.启动测试
## 一、 路由 [参考](http://www.cnblogs.com/wupeiqi/articles/5237704.html)
+ 1、path('index/', views.index),      # 一一对应
     path('home/', views.Home.as_view()),
+ 2、re_path('^detail-(\d+).html', views.detail),   # 一对多，但是严格按照顺序来传递
+ 3、re_path('^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail) # 一对多，可以打乱顺序,建议使用
     re_path('detail-(?P<nid>\d+).html', views.detail)
> def detail(request, *args,**kwargs):pass
```
实战：
			a. 正则表达式可以接收的函数
				url(r'^detail-(\d+)-(\d+).html', views.detail),
				def func(request, nid, uid):
					pass
				def func(request, *args):
					args = (2,9)
				def func(request, *args, **kwargs):
					args = (2,9)
			b. 分组正则表达式可以接收的函数
				url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail)
				def func(request, nid, uid):
					pass
				def funct(request, **kwargs):
					kwargs = {'nid': 1, 'uid': 3}
				def func(request, *args, **kwargs):
					args = (2,9)
```
+ 4.name,了解即可
```
对URL路由关系进行命名， ***** 以后可以根据此名称生成自己想要的URL *****
		url(r'^asdfasdfasdf/', views.index, name='i1'),
		url(r'^yug/(\d+)/(\d+)/', views.index, name='i2'),
		url(r'^buy/(?P<pid>\d+)/(?P<nid>\d+)/', views.index, name='i3'),
xxx.html
			
			{% url "i1" %}               # asdfasdfasdf/
			{% url "i2" 1 2 %}           # yug/1/2/
			{% url "i3" pid=1 nid=9 %}   # buy/1/9/
注：
			# 当前的URL
			request.path_info 
# reverse
def func(request, *args, **kwargs):
			from django.urls import reverse
			url1 = reverse('i1')                              # asdfasdfasdf/
			url2 = reverse('i2', args=(1,2,))                 # yug/1/2/
			url3 = reverse('i3', kwargs={'pid': 1, "nid": 9}) # buy/1/9/
```
+ 5. 多级路由
```python
project/urls.py
    from django.conf.urls import url,include
    from django.contrib import admin

    urlpatterns = [
        path('^cmdb/', include("app01.urls")),
        path('^monitor/', include("app02.urls")),
    ]
    
app01/urls.py
    from django.conf.urls import url,include
    from django.contrib import admin
    from app01 import views

    urlpatterns = [
        path('^login/', views.login),
    ]
    
app02/urls.py
    from django.conf.urls import url,include
    from django.contrib import admin
    from app02 import views

    urlpatterns = [
        path('^login/', views.login),
    ]
```
+ 6、默认值（欠）
+ 7、命名空间（欠）
## 二、视图
### 1.获取用户请求数据
+ request.GET
+ request.POST
+ request.FILES
> GET:获取数据，POST:提交数据
### 2. checkbox等多选的内容
+ request.POST.getlist()
### 3. 上传文件
+ 页面需要添加 enctype="multipart/form-data"
+ 代码中实现
```python
obj = request.FILES.get('fafafa')
obj.name
import os
file_path = os.path.join('upload', obj.name)
f = open(obj.name, mode='wb')
for item in obj.chunks():
    f.write(item)
f.close()
```
### 4. FBV & CBV
+ FBV (function base view)  例如：   /index/ -> 函数名
```
view.py
    def 函数(request):
        ...
urls.py
path('home/', views.home),
```
+ CBV(class base view)  例如： /index/ -> 类
```
views.py
    from django.views import View
    class Home(View):
        def get(self, request):
            return render(request, 'home.html')
    
        def post(self, request):
            pass
urls.py
     path('home/', views.Home.as_view()),
```
### 5. 装饰器 欠
## 三、ORM操作
```
select * from tb where id > 1
# 对应关系
models.tb.objects.filter(id__gt=1)
models.tb.objects.filter(id=1)
models.tb.objects.filter(id__lt=1)
```
### 默认操作步骤
#### 1. 创建类
+ 位置： app下的models.py
#### 2. 注册APP,在settings中添加
```
INSTALLED_APPS = [
			'django.contrib.admin',
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.sessions',
			'django.contrib.messages',
			'django.contrib.staticfiles',
			'app01',
		]
```
#### 3. 执行命令
```
		python manage.py  makemigrations
		python manage.py  migrate
```
### 使用mysql的操作步骤
Django默认使用MySQLdb模块链接MySQL
主动修改为pymysql，在project同名文件夹下的__init__文件中添加如下代码即可：
    import pymysql
    pymysql.install_as_MySQLdb()
#### 1. 修改settings
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME':'django',
    'USER': 'root',
    'PASSWORD': 'root',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    }
}
```
#### 2. 添加pymysql支持
如下设置放置的与project同名的配置的 __init__.py文件中，例如当前项目目录为
day19_django/__init__.py中添加
需要先安装pymysql`pip install pymysql`
```
import pymysql
pymysql.install_as_MySQLdb()
```
#### 3. 注册APP,在settings中添加，同上
#### 4. 执行命令，同上
#### 创建 Django 用户：python manage.py createsuperuser
### 字段
+ 字符串类型
+ 数字
+ 时间
+ 二进制
+ 自增(primary_key=True)
### 字段的参数[参考](http://www.cnblogs.com/wupeiqi/articles/5246483.html)
+ null            # db是否可以为空
+ default         # 默认值
+ primary_key     # 主键
+ db_column       # 列名
+ db_index        # 索引
+ unique          # 唯一索引
+ unique_for_date
+ unique_for_month
+ unique_for_year
+ auto_now        # 创建时，自动生成时间
+ auto_now_add    # 更新时，自动更新为当前时间
```
# obj = UserGroup.objects.filter(id=1).update(caption='CEO')
# obj = UserGroup.objects.filter(id=1).first()
# obj.caption = "CEO"
# obj.save()
```
+ choices		  #  django admin中显示下拉框，避免连表查询
+ blank           #  django admin是否可以为空
+ verbose_name    #  django admin显示字段中文
+ editable        #  django admin是否可以被编辑
+ error_messages  #  错误信息欠
+ help_text       #  django admin提示
+ validators      #  django form ,自定义错误信息（欠）

### 查询
```
增
models.User.objects.create(name='qianxiaohu',age=18)
dic = {'name': 'xx', 'age': 19}
models.User.objects.create(**dic)

obj = models.User(name='qianxiaohu',age=18)
obj.save()
删
models.User.objects.filter(id=1).delete()
改
    models.User.objects.filter(id__gt=1).update(name='alex',age=84)
    dic = {'name': 'xx', 'age': 19}
models.User.objects.filter(id__gt=1).update(**dic)
查
    models.User.objects.filter(id=1,name='root')
    models.User.objects.filter(id__gt=1,name='root')
    models.User.objects.filter(id__lt=1)
    models.User.objects.filter(id__gte=1)
    models.User.objects.filter(id__lte=1)
    
    models.User.objects.filter(id=1,name='root')
    dic = {'name': 'xx', 'age__gt': 19}
    models.User.objects.filter(**dic)
    
    v1 = models.Business.objects.all()
    # QuerySet ,内部元素都是对象
    # QuerySet ,内部元素都是字典
    v2 = models.Business.objects.all().values('id','caption')
    # QuerySet ,内部元素都是元组
    v3 = models.Business.objects.all().values_list('id','caption')
    # 获取到的一个对象，如果不存在就报错
    models.Business.objects.get(id=1)
    对象或者None = models.Business.objects.filter(id=1).first()
```
### 多对多
+ 自定义关系表
```
多对多：
    创建多对多：
		方式一：自定义关系表
			class Host(models.Model):
				nid = models.AutoField(primary_key=True)
				hostname = models.CharField(max_length=32,db_index=True)
				ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
				port = models.IntegerField()
				b = models.ForeignKey(to="Business", to_field='id')
			# 10
			class Application(models.Model):
				name = models.CharField(max_length=32)
			# 2
			
			class HostToApp(models.Model):
				hobj = models.ForeignKey(to='Host',to_field='nid')
				aobj = models.ForeignKey(to='Application',to_field='id')
				
			# HostToApp.objects.create(hobj_id=1,aobj_id=2)
```
+ 自动创建关系表
```
方式二：自动创建关系表
			class Host(models.Model):
				nid = models.AutoField(primary_key=True)
				hostname = models.CharField(max_length=32,db_index=True)
				ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
				port = models.IntegerField()
				b = models.ForeignKey(to="Business", to_field='id')
			# 10
			class Application(models.Model):
				name = models.CharField(max_length=32)
				r = models.ManyToManyField("Host")
				
			无法直接对第三张表进行操作
			
			obj = Application.objects.get(id=1)
			obj.name
			
			# 第三张表操作
			obj.r.add(1)
			obj.r.add(2)
			obj.r.add(2,3,4)
			obj.r.add(*[1,2,3,4])
			
			obj.r.remove(1)
			obj.r.remove(2,4)
			obj.r.remove(*[1,2,3])
			
			obj.r.clear()   # 清空id=1的app相关的所有host
			
			obj.r.set([3,5,7]) # 删除id=1的app对应的host，并更新为3，5，7的对应关系
			
			# 所有相关的主机对象“列表” QuerySet
			obj.r.all()
```
## 模板语法
+ dict
```
{% for k,v in user_dict.items %}
{% for k in user_dict.keys %}
{% for v in user_dict.values %}
```
+ list
```
{% for item in user_list%}
```
+ 插值表达式`{{user_name}}`
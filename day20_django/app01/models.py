from django.db import models


# Create your models here.

# class Foo(models.Model):
#     name = models.CharField(max_length=1)

class Business(models.Model):
    # id
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, null=True, default="SA")
    # fk = models.ForeignKey('Foo')


# 当查询到host，通过b可以访问business，通过business的fk可以访问Foo
# 			外键：
# 				v = models.Host.objects.filter(nid__gt=0)
# 				v[0].b.caption  ---->  通过.进行跨表
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4", db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id', on_delete=models.CASCADE)


class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")  # 2.自动创建关系表,这个只能生成3列，如果需要添加自定义列，只能采用自定义方式创建


# 1. 自定义关系表
# class HostToApp(models.Model):
#     hobj = models.ForeignKey(to='Host', to_field='nid', on_delete=models.CASCADE)
#     aobj = models.ForeignKey(to='Application', to_field='id', on_delete=models.CASCADE)

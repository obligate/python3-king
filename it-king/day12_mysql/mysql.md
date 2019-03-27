## Refer
+ [知识体系](https://www.cnblogs.com/alex3714/articles/5885096.html)
+ [知识体系2](http://www.cnblogs.com/alex3714/articles/5978329.html )


## python 操作mysql
###  1.Python 操作 Mysql 模块的安装,了解就可以
```
linux：
    yum install MySQL-python
window：
    http://files.cnblogs.com/files/wupeiqi/py-mysql-win.zip
```
### 2.原生模块 pymsql
pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同
+ `pip3 install pymysql`

### ORM框架 [SQLAchemy](http://www.cnblogs.com/alex3714/articles/5978329.html )
SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果
+ `pip3 install pymysql `  #由于mysqldb依然不支持py3，所以这里我们用pymysql与sqlalchemy交互
+ `pip3 install SQLAlchemy`
![sqlachemy](img/SQLAlchemy.png)
SQLAlchemy本身无法操作数据库，其必须以来pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如
```
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]   
更多详见：http://docs.sqlalchemy.org/en/latest/dialects/index.html
```
# Author: Peter
# 1. 第一种方式创建表o2_orm_basic
# 2. 第二种方式创建02_2orm_create_metadata，虽不常用，但还是看看吧
# 我们用第一种方式o2_orm_basic创建的表就是基于第2种方式的再封装
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

# the table metadata is created separately with the Table construct, then associated with the User class via the mapper() function
mapper(User, user)

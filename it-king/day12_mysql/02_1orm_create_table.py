# Author: Peter
# 1. 第一种方式创建表o2_orm_basic
# 2. 第二种方式创建02_2orm_create_metadata，虽不常用，但还是看看吧
# 我们用第一种方式o2_orm_basic创建的表就是基于第2种方式的再封装
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:root@localhost/python", encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)  # 创建表结构

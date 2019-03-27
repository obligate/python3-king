# Author: Peter
# 一本书可以有多个作者，一个作者又可以出版多本书
from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id', Integer, ForeignKey('books.id')),
                        Column('author_id', Integer, ForeignKey('authors.id')),
                        )


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author', secondary=book_m2m_author, backref='books')

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


# 处理中文==>sqlalchemy设置编码字符集一定要在数据库访问的URL上增加charset=utf8，否则数据库的连接就不是utf8的编码格式
engine = create_engine("mysql+pymysql://root:root@localhost/python?charset=utf8", encoding='utf-8', echo=False)
Base.metadata.create_all(engine)  # 创建表结构

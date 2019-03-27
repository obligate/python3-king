# Author: Peter
# http://www.cnblogs.com/alex3714/articles/5978329.html
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost/python", encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)


Base.metadata.create_all(engine)  # 创建表结构,如果表不存在会创建，存在不会创建

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# 回滚
my_user = Session.query(User).filter_by(id=1).first()
my_user.name = "Jack"

fake_user = User(name='Rain', password='12345')
Session.add(fake_user)
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据

Session.rollback()  # 此时你rollback一下
print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

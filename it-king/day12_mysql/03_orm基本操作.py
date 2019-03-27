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

# insert data
# user_obj = User(name="peter", password="qwe123")  # 生成你要创建的数据对象
# user_obj2 = User(name="peter2", password="qwe123")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建

# query data
# 1. query data
my_user = Session.query(User).filter_by(name="peter").first()  # sqlalchemy帮你把返回的数据映射成一个对象啦，这样你调用每个字段就可以跟调用对象属性一样啦
# 不过刚才上面的显示的内存对象对址你是没办法分清返回的是什么数据的，除非打印具体字段看一下，如果想让它变的可读，只需在定义表的类下面加上这样的代码
# def __repr__(self):
#     return "<User(name='%s',  password='%s')>" % (
#         self.name, self.password)
print(my_user)  # 需要添加__repr__方法
print(my_user.id, my_user.name, my_user.password)

# 2. 查询所有
print("#" * 100)
print(Session.query(User.name, User.id).all())

# # 连表
# ret = session.query(Users, Favor).filter(Users.id == Favor.nid).all()
# ret = session.query(Person).join(Favor).all()
# ret = session.query(Person).join(Favor, isouter=True).all()

# 3. 多条件查询,下面2个filter的关系相当于 user.id >1 AND user.id <2 的效果
objs = Session.query(User).filter(User.id > 0).filter(User.id < 2).all()
print(objs)

# 4. 分组
print(Session.query(User).filter(User.name.like("pet%")).count())  # 统计
from sqlalchemy import func
print(Session.query(func.count(User.name), User.name).group_by(User.name).all())


# 修改数据
my_user = Session.query(User).filter_by(name="peter").first()
my_user.name = "Jack"


Session.commit()  # 现此才统一提交，创建数据

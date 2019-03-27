# Author: Peter
import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# b1 = orm_m2m.Book(name="Whisper learning Python")
# b2 = orm_m2m.Book(name="Whisper girl")
# b3 = orm_m2m.Book(name="Whisper sb")
# b4 = orm_m2m.Book(name="Whisper car")
#
# a1 = orm_m2m.Author(name="Whisper")
# a2 = orm_m2m.Author(name="Thunder")
# a3 = orm_m2m.Author(name="Flash")
#
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
#
# session.add_all([b1, b2, b3, b4, a1, a2, a3])


# 查询
print('--------通过作者表查关联的书---------')
author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == "Whisper").first()
print(author_obj.name, author_obj.books)
print('--------通过书表查关联的作者---------')
book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.name == "Whisper learning Python").first()
print(book_obj.name, book_obj.authors)

# 删除
# 删除数据时不用管boo_m2m_authors　， sqlalchemy会自动帮你把对应的数据删除
# 通过书删除作者
# author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == "Whisper").first()
# book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.name == "Whisper girl").first()
# book_obj.authors.remove(author_obj)  # 从一本书里删除一个作者

# 直接删除作者
# 删除作者时，会把这个作者跟所有书的关联关系数据也自动删除
# author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == "Whisper").first()
# session.delete(author_obj)

session.commit()

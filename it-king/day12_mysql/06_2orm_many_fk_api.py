# Author: Peter
import orm_many_fk_create

from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_many_fk_create.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# insert
# addr1 = orm_many_fk_create.Address(street="Tiantongyuan", city="Changping", state="BJ")
# addr2 = orm_many_fk_create.Address(street="Wudaokou", city="Haidian", state="BJ")
# addr3 = orm_many_fk_create.Address(street="Yanjiao", city="Langfang", state="HB")
#
# session.add_all([addr1, addr2, addr3])
# c1 = orm_many_fk_create.Customer(name="Whisper", billing_address=addr1, shipping_address=addr2)
# c2 = orm_many_fk_create.Customer(name="Thunder", billing_address=addr3, shipping_address=addr3)
# session.add_all([c1, c2])


# query
obj = session.query(orm_many_fk_create.Customer).filter(orm_many_fk_create.Customer.name == "Whisper").first()
print(obj.name, obj.billing_address, obj.shipping_address)

session.commit()

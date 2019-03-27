# Author: Peter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:root@localhost/python", encoding='utf-8', echo=False)
Base = declarative_base()  # 生成orm基类


class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name:%s)>" % (
            self.id, self.name)


class Study_Record(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))

    # 允许你在Student表里通过backref字段反向查出所有它在my_study_record表里的关联项
    # ORM在内存中将Study_Record和Student做了一个双向关联
    student = relationship("Student",  backref="my_study_record")

    def __repr__(self):
        return "<%s day:%s status:%s)>" % (
            self.student.name, self.day, self.status)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# insert data
# s1 = Student(name="Whisper", register_date="2013-09-01")
# s2 = Student(name="Thunder", register_date="2014-09-01")
# s3 = Student(name="Flash", register_date="2012-09-01")
# s4 = Student(name="Misty", register_date="2017-09-01")
#
# sr1 = Study_Record(day=1, status="YES", stu_id=1)
# sr2 = Study_Record(day=2, status="NO", stu_id=1)
# sr3 = Study_Record(day=3, status="YES", stu_id=1)
# sr4 = Study_Record(day=1, status="YES", stu_id=2)
#
# session.add_all([s1, s2, s3, s4, sr1, sr2, sr3, sr4])

stu_obj = session.query(Student).filter(Student.name == "Whisper").first()
print(stu_obj.my_study_record)
session.commit()  # 现此才统一提交，创建数据

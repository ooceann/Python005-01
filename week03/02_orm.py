# -*- coding: utf-8 -*-
# @FileName: 02_orm.py
# @Time    : 2020/12/13 4:35 下午
# @Author  : zhan

# 02-用orm的方式创建user表


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    uid = Column(Integer(), primary_key=True)
    name = Column(String(50))
    age = Column(Integer())
    birthday = Column(String(20))
    gender = Column(String(10))
    education = Column(String(50))
    create_time = Column(DateTime(), default=datetime.now())
    update_time = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())


db_url = "mysql+pymysql://root:bluer123@localhost:3306/testdb"
engine = create_engine(db_url, echo=True, encoding="utf-8")
# 创建user表
# Base.metadata.create_all(engine)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 插入数据
user1 = User(name='Jack', age=22, birthday='1996-10-10', gender='boy')
user2 = User(name='Rose', age=22, birthday='1998-10-10', gender='girl')

session.add(user1)
session.add(user2)

# 查询所有值
query1 = session.query(User).all()
print(query1)  # 列表

# 更新
query2 = session.query(User)
query2 = query2.filter(User.name == 'Jack')
query2.update({User.age: '25', User.gender: 'boy', User.birthday: '1995-10-01', User.education: 'Master'})

session.flush()
session.commit()

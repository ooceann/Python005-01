# -*- coding: utf-8 -*-
# @FileName: 06_transfer.py
# @Time    : 2020/12/13 5:42 下午
# @Author  : zhan

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    uid = Column(Integer(), primary_key=True)
    name = Column(String(50))


class Balance(Base):
    __tablename__ = 'balance'
    uid = Column(Integer(), primary_key=True)
    amount = Column(DECIMAL(10, 0))


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer(), primary_key=True)
    s_id = Column(Integer(), comment='转账用户id')
    r_id = Column(Integer(), comment='接受用户id')
    trans_amount = Column(DECIMAL(10, 0), comment='转账金额')
    create_time = Column(DateTime(), default=datetime.now(), comment='转账时间')


db_url = "mysql+pymysql://root:bluer123@localhost:3306/testdb"
engine = create_engine(db_url, echo=True, encoding="utf-8")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()


def balance_enough(uid, need):
    query = session.query(Balance.amount).filter(Balance.uid == uid)
    if not query[0][0] > need:
        print(f'用户{uid}余额不足')
    else:
        return True


def exist_user(uid):
    user = session.query(Users).filter(Users.uid == uid)
    if not user.first():
        print(f'用户{uid}不存在')
    else:
        return True


def transfer(s_id, r_id, trans_amount):
    if exist_user(s_id) and exist_user(r_id) and balance_enough(s_id, trans_amount):
        try:
            s_balance = session.query(Balance).filter(Balance.uid == s_id)
            s_balance.update({Balance.amount: Balance.amount - trans_amount})

            r_balance = session.query(Balance).filter(Balance.uid == r_id)
            r_balance.update({Balance.amount: Balance.amount + trans_amount})

            order = Order(s_id=s_id, r_id=r_id, trans_amount=trans_amount)
            session.add(order)

            session.flush()
            session.commit()
            print('转账成功')
        except Exception as e:
            raise e


# 1号用户给3号用户转账200
transfer(1, 3, 1000)

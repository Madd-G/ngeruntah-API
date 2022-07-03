from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Table, Column
from config.db import meta, engine

orders = Table('order', meta,
              Column('id', Integer, primary_key=True),
              Column('weight', Integer),
              Column('date', String(255)),
              Column('address', String(255)),
              Column('note', String(255)),
              )

users = Table('user_ngeruntah', meta,
              Column('id', Integer, primary_key=True),
              Column('username', String(255)),
              Column('email', String(255)),
              Column('password', String(255)),
              Column('phone_number', String(255)),
              Column('gender', String(255)),
              )

meta.create_all(engine)

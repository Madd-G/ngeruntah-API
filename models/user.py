from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Table, Column
from config.db import meta, engine

users = Table('ngeruntah_user', meta,
              Column('id', Integer, primary_key=True),
              Column('username', String(255)),
              Column('email', String(255)),
              Column('password', String(255)),
              Column('phone_number', String(255)),
              Column('gender', String(255)),
              )

meta.create_all(engine)

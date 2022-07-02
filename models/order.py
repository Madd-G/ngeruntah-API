from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Table, Column
from config.db import meta, engine

orders = Table('ngeruntah', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String(255)),
              Column('weight', Integer),
              Column('date', String(255)),
              Column('address', String(255)),
              Column('note', String(255)),
              )



meta.create_all(engine)

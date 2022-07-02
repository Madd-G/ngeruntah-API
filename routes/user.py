from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()


@user.get('/')
def fetch_users():
    return conn.execute(users.select()).fetchall()


@user.post('/create/')
def post_user(user: User):
    return conn.execute(users.insert().values(name=user.name, weight=user.weight, date=user.date, address=user.address, note=user.note))


@user.put('/update/{id}')
def update_user(id: int, user: User):
    return conn.execute(users.update().values(name=user.name, weight=user.weight, date=user.date, address=user.address, note=user.note).where(users.c.id == id))


@user.delete('/delete/{id}')
def delete_user(id: int):
    # c = column
    return conn.execute(users.delete().where(users.c.id == id))

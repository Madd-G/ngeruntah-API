from fastapi import APIRouter
from config.db import conn
from models.model import orders, users
from schemas.order import Order
from schemas.user import User

user = APIRouter()


@user.get('/')
def fetch_orders():
    return conn.execute(orders.select()).fetchall()


@user.get('/profile')
def fetch_users():
    return conn.execute(users.select()).fetchall()


@user.post('/create_order/')
def post_order(order: Order):
    return conn.execute(
        orders.insert().values(weight=order.weight, date=order.date, address=order.address,
                               note=order.note))


@user.post('/create_user/')
def post_user(user: User):
    return conn.execute(
        users.insert().values(username=user.username, email=user.email, password=user.password,
                              phone_number=user.phone_number,
                              gender=user.gender))


@user.put('/update_order/{id}')
def update_order(id: int, order: Order):
    return conn.execute(
        orders.update().values(weight=order.weight, date=order.date, address=order.address,
                               note=order.note).where(orders.c.id == id))


@user.put('/update_user/{id}')
def update_user(id: int, user: User):
    return conn.execute(
        users.update().values(username=user.username, email=user.email, password=user.password,
                              phone_number=user.phone_number,
                              gender=user.gender).where(users.c.id == id))


@user.delete('/delete_order/{id}')
def delete_order(id: int):
    # c = column
    return conn.execute(orders.delete().where(orders.c.id == id))


@user.delete('/delete_user/{id}')
def delete_user(id: int):
    # c = column
    return conn.execute(users.delete().where(users.c.id == id))

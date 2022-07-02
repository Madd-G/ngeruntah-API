from fastapi import APIRouter
from config.db import conn
from models.order import orders
from schemas.order import Order

user = APIRouter()


@user.get('/')
def fetch_users():
    return conn.execute(orders.select()).fetchall()


@user.post('/create_order/')
def post_user(order: Order):
    return conn.execute(
        orders.insert().values(name=order.name, weight=order.weight, date=order.date, address=order.address,
                               note=order.note))


@user.put('/update_order/{id}')
def update_user(id: int, order: Order):
    return conn.execute(
        orders.update().values(name=order.name, weight=order.weight, date=order.date, address=order.address,
                               note=order.note).where(orders.c.id == id))


@user.delete('/delete_order/{id}')
def delete_user(id: int):
    # c = column
    return conn.execute(orders.delete().where(orders.c.id == id))

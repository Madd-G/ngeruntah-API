from pydantic import BaseModel


class Order(BaseModel):
    name: str
    weight: int
    date: str
    address: str
    note: str

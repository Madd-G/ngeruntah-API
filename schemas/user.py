from pydantic import BaseModel


class User(BaseModel):
    name: str
    weight: int
    date: str
    address: str
    note: str

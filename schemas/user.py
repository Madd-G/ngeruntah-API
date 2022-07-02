from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    phone_number: str
    gender: str

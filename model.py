from pydantic import BaseModel

class Price(BaseModel):
    gold: float


class Product(BaseModel):
    price: Price
    title: str
    code: str

class Items(BaseModel):
    products: list[Product]

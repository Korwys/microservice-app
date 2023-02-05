from pydantic import BaseModel

from products.schemas import ProductBase


class CartBase(BaseModel):
    ...


class CartDelete(CartBase):
    product: int


class CartUpdate(CartBase):
    product: int
    quantity: int


class CartAdd(CartUpdate):
    ...


class CartItem(CartUpdate):
    product: int
    quantity: int


class CartInDB(CartBase):
    id: int
    product: int
    quantity: int

    class Config:
        orm_mode = True

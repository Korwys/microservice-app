from pydantic import BaseModel


class CartBase(BaseModel):
    ...


class CartUpdate(CartBase):
    product: int
    quantity: int


class CartAdd(CartUpdate):
    quantity: int = 1


class CartItem(CartUpdate):
    product: int
    quantity: int


class CartInDB(CartBase):
    id: int
    product: int
    quantity: int

    class Config:
        orm_mode = True

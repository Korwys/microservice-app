from pydantic import BaseModel, validator


class CartBase(BaseModel):
    ...


class CartUpdate(CartBase):
    product: int
    quantity: int

    @validator('quantity')
    def quantity_validator(cls, value: int):
        if value > 999999999 or value <= 0:
            raise ValueError('Product quantity must lte 999999999 and gt 0')
        else:
            return value


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

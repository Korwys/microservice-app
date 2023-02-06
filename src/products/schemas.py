from pydantic import BaseModel, validator


class ProductBase(BaseModel):
    name: str
    price: float

    @validator('name')
    def name_validation(cls, value: str) -> str:
        if len(value) == 0 or len(value) > 150:
            raise ValueError('Product name must be less than 150  but more than 0 characters')
        else:
            return value

    @validator('price')
    def price_validator(cls, value: float) -> float:
        if value > 99999999999.9:
            raise ValueError('Product price must be less 99999999999.9')
        else:
            return value


class ProductQuery(BaseModel):
    keyword: str | None = None
    price_sorted: str | None = 'default'
    name_sorted: str | None = 'default'

    @validator('keyword')
    def keyword_validator(cls, value) -> str:
        if len(value) > 150:
            raise ValueError('Search query length must be less than 150 characters')
        else:
            return value

    @validator('price_sorted')
    def price_validator(cls, value) -> str:
        if value not in ('default', 'asc', 'desc'):
            raise ValueError('The sorting type should only be: default - if no sort, or asc or desc')
        else:
            return value

    @validator('name_sorted')
    def name_validator(cls, value) -> str:
        if value not in ('default', 'asc', 'desc'):
            raise ValueError('The sorting type should only be: default - if no sort, or asc or desc')
        else:
            return value


class ProductQueryList(ProductBase):
    ...

    class Config:
        orm_mode = True

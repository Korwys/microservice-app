from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config.db import get_db
from products.schemas import ProductBase, ProductQuery, ProductQueryList
from products.services import add_product_in_db, fetch_request_products

product_router = APIRouter()


@product_router.post('/', response_model=ProductBase, status_code=status.HTTP_201_CREATED)
async def create_new_product(product: ProductBase, db: AsyncSession = Depends(get_db)) -> ProductBase:
    return await add_product_in_db(db=db, obj_in=product)


@product_router.post('/search', response_model=list[ProductQueryList], status_code=status.HTTP_200_OK)
async def search_products(query: ProductQuery, db: AsyncSession = Depends(get_db)):
    return await fetch_request_products(db=db, query=query)


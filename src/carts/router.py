from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from carts.schemas import CartDelete, CartAdd, CartInDB, CartUpdate
from carts.services import add_new_product_in_cart, update_product_quantity, fetch_all_products_from_cart, \
    delete_product_from_cart
from config.db import get_db

cart_router = APIRouter()


@cart_router.post('/add', response_model=CartInDB, status_code=status.HTTP_201_CREATED)
async def add_product_in_cart(new_product_in_cart: CartAdd, db: AsyncSession = Depends(get_db)):
    return await add_new_product_in_cart(new_product_in_cart, db)


@cart_router.patch('/update_quantity', response_model=CartUpdate, status_code=status.HTTP_200_OK)
async def edit_product_quantity(new_product_quantity: CartUpdate, db: AsyncSession = Depends(get_db)):
    return await update_product_quantity(db, new_product_quantity)


@cart_router.get('/', response_model=list[CartInDB], status_code=status.HTTP_200_OK)
async def get_all_products(db: AsyncSession = Depends(get_db)):
    return await fetch_all_products_from_cart(db=db)


@cart_router.delete("/delete/}", status_code=status.HTTP_200_OK)
async def delete_product(product_to_delete: CartDelete, db: AsyncSession = Depends(get_db)):
    return await delete_product_from_cart(db, product_to_delete)

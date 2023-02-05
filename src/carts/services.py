import logging

from sqlalchemy import update, select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from carts.models import Cart
from carts.schemas import CartBase, CartDelete, CartAdd
from products.models import Product

logger = logging.getLogger('app.carts.router')


async def add_new_product_in_cart(new_product: CartAdd, db: AsyncSession):
    check_db_obj = await db.execute(select(Product).where(Product.id == new_product.product))
    result = check_db_obj.scalars().first()
    if result is not None:
        obj_in = new_product.dict()
        updated_db_obj = Cart(**obj_in)
        try:
            db.add(updated_db_obj)
            await db.commit()
            return updated_db_obj
        except SQLAlchemyError as err:
            logger.exception(err)
    else:
        return JSONResponse(status_code=404, content={"Message": "Product with this ID not found. Can't add to cart."})


async def update_product_quantity(db: AsyncSession, obj_in: CartBase):
    check_db_obj = await db.execute(select(Cart).where(Cart.product == obj_in.product))
    result = check_db_obj.scalars().first()
    if result is not None and obj_in.quantity > 0:
        stmt = update(Cart).where(Cart.product == obj_in.product).values(quantity=obj_in.quantity)
        try:
            await db.execute(stmt)
            await db.commit()
            return {"product": obj_in.product, "quantity": obj_in.quantity}
        except SQLAlchemyError as err:
            logger.exception(err)
    elif result is None:
        return JSONResponse(status_code=404,
                            content={"Message": "No product with same ID in the cart. Check product ID"})
    else:
        return JSONResponse(status_code=404, content={"Message": "Product quantity must be greater than 0"})


async def fetch_all_products_from_cart(db: AsyncSession):
    stmt = select(Cart)
    try:
        result = await db.execute(stmt)
        values = result.scalars().all()
        return values
    except SQLAlchemyError as err:
        logger.exception(err)

async def delete_product_from_cart(db: AsyncSession, obj_in: CartDelete):
    stmt = delete(Cart).where(Cart.product == obj_in.product)
    try:
        await db.execute(stmt)
        await db.commit()
        return JSONResponse(status_code=200, content={"Message": "Product was deleted"})
    except SQLAlchemyError as err:
        logger.exception(err)

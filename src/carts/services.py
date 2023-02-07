import logging

from sqlalchemy import update, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from carts.models import Cart
from carts.schemas import CartAdd, CartUpdate, CartInDB
from products.models import Product
from products.utils import error_notification

logger = logging.getLogger('app.carts.services')


async def add_new_product_in_cart(new_product: CartAdd, db: AsyncSession) -> CartInDB | JSONResponse:
    check_product_db_obj = await db.execute(select(Product).where(Product.id == new_product.product))
    product_result_response = check_product_db_obj.scalars().first()

    check_cart_db_obj = await db.execute(select(Cart).where(Cart.product == new_product.product))
    cart_result_response = check_cart_db_obj.scalars().first()
    if product_result_response is not None and cart_result_response is None:
        obj_in = new_product.dict()
        db_obj = Cart(**obj_in)
        try:
            db.add(db_obj)
            await db.commit()
            return db_obj
        except SQLAlchemyError as err:
            logger.exception(err)
            return error_notification()
    elif cart_result_response is not None:
        return JSONResponse(status_code=400, content={"Message": "This product is already in the cart."})
    else:
        return JSONResponse(status_code=404, content={"Message": "Product with this ID not found. Can't add to cart."})


async def update_product_quantity(db: AsyncSession, obj_in: CartUpdate) -> CartUpdate | JSONResponse:
    check_db_obj = await db.execute(select(Cart).where(Cart.product == obj_in.product))
    result = check_db_obj.scalars().first()
    if result is not None and obj_in.quantity > 0:
        stmt = update(Cart).where(Cart.product == obj_in.product).values(quantity=obj_in.quantity)
        try:
            await db.execute(stmt)
            await db.commit()
            return obj_in
        except SQLAlchemyError as err:
            logger.exception(err)
            return error_notification()
    elif result is None:
        return JSONResponse(status_code=404,
                            content={"Message": "No product with same ID in the cart. Check product ID"})
    else:
        return JSONResponse(status_code=404, content={"Message": "Product quantity must be greater than 0"})


async def fetch_all_products_from_cart(db: AsyncSession) -> list[Cart]:
    stmt = select(Cart)
    try:
        result = await db.execute(stmt)
        values = result.scalars().all()
        return values
    except SQLAlchemyError as err:
        logger.exception(err)
        return error_notification()

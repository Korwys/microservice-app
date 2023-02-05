import logging

from sqlalchemy import UnaryExpression
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from products.models import Product
from products.schemas import ProductBase, ProductQuery

logger = logging.getLogger('app.products.services')


async def add_product_in_db(db: AsyncSession, obj_in: ProductBase) -> Product:
    obj_in = obj_in.dict()
    db_obj = Product(**obj_in)
    try:
        db.add(db_obj)
        await db.commit()
        return db_obj
    except SQLAlchemyError as err:
        logger.exception(err)


async def sorted_keyword_data(db: AsyncSession, keyword: str, name: UnaryExpression,
                              price: UnaryExpression) -> JSONResponse:
    stmt = select(Product.name).where(Product.name.like(f"%{keyword}%"))
    if name is not None:
        stmt = stmt.order_by(name)
    if price is not None:
        stmt = stmt.order_by(price)
    try:
        result = await db.execute(stmt)
        values = [product.name for product in result]
        return JSONResponse(status_code=200, content={'products': values})
    except SQLAlchemyError as err:
        logger.exception(err)


async def sorted_data(db: AsyncSession, name: UnaryExpression, price: UnaryExpression) -> JSONResponse:
    stmt = select(Product.name)
    if name is not None:
        stmt = stmt.order_by(name)
    if price is not None:
        stmt = stmt.order_by(price)
    try:
        result = await db.execute(stmt)
        values = [product.name for product in result]
        return JSONResponse(status_code=200, content={'products': values})
    except SQLAlchemyError as err:
        logger.exception(err)


async def fetch_request_products(db: AsyncSession, query: ProductQuery) -> JSONResponse:
    column_price_sorted = getattr(Product.price, query.price_sorted)() if query.price_sorted != 'default' else None
    column_name_sorted = getattr(Product.name, query.name_sorted)() if query.name_sorted != 'default' else None
    if query.keyword:
        return await sorted_keyword_data(db, query.keyword, column_name_sorted, column_price_sorted)
    else:
        return await sorted_data(db, column_name_sorted, column_price_sorted)

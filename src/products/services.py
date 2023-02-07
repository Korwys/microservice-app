import logging

from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import UnaryExpression
from starlette.responses import JSONResponse

from products.models import Product
from products.schemas import ProductCreate, ProductQuery, ProductInDB
from products.utils import error_notification

logger = logging.getLogger('app.products.services')


async def add_product_in_db(db: AsyncSession, obj_in: ProductCreate) -> ProductInDB | JSONResponse:
    obj_in = obj_in.dict()
    db_obj = Product(**obj_in)
    try:
        db.add(db_obj)
        await db.commit()
        return db_obj
    except SQLAlchemyError as err:
        logger.exception(err)
        return error_notification()


async def sorted_data_with_keyword(db: AsyncSession, keyword: str, name: UnaryExpression,
                                   price: UnaryExpression) -> list[ProductInDB] | JSONResponse:
    stmt = select(Product).where(Product.name.ilike(f"%{keyword}%"))
    if name is not None:
        stmt = stmt.order_by(name)
    if price is not None:
        stmt = stmt.order_by(price)
    try:
        result = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        logger.exception(err)
        return error_notification()


async def sorted_data_without_keyword(db: AsyncSession, name: UnaryExpression,
                                      price: UnaryExpression) -> list[ProductInDB] | JSONResponse:
    stmt = select(Product)
    if name is not None:
        stmt = stmt.order_by(name)
    if price is not None:
        stmt = stmt.order_by(price)
    try:
        result = await db.execute(stmt)
        return result.scalars().all()
    except SQLAlchemyError as err:
        logger.exception(err)
        return error_notification()


async def fetch_request_products(db: AsyncSession, query: ProductQuery) -> list[ProductInDB] | JSONResponse:
    column_price_sorted = getattr(Product.price, query.price_sorted)() if query.price_sorted != 'default' else None
    column_name_sorted = getattr(Product.name, query.name_sorted)() if query.name_sorted != 'default' else None
    if query.keyword:
        return await sorted_data_with_keyword(db, query.keyword, column_name_sorted, column_price_sorted)
    else:
        return await sorted_data_without_keyword(db, column_name_sorted, column_price_sorted)

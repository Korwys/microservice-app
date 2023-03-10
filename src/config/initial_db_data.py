import logging

from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from config.db import engine, Base
from products.models import Product

logger = logging.getLogger('app.config.initial_db_data')


async def init_tables_and_data() -> None:
    """Тестовое наполнение БД."""
    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            await conn.execute(insert(Product),
                               [
                                   {"name": "Nokia 3310", "price": 1000},
                                   {"name": "Motorola V3", "price": 3000},
                                   {"name": "Samsung G1000", "price": 52200},
                                   {"name": "Xiaomi Note10 Pro", "price": 13000},
                                   {"name": "Iphone 14", "price": 20000},
                                   {"name": "Nokia XS", "price": 12000},
                                   {"name": "Iphone 15", "price": 22000},
                                   {"name": "Nokia A", "price": 26000},
                               ],
                               )
        except SQLAlchemyError as err:
            logger.exception(err)
        else:
            logger.info('DB IS READY ^_^')

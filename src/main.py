import json
import logging.config

import uvicorn
from fastapi import FastAPI

from carts.router import cart_router
from config.initial_db_data import init_tables_and_data
from products.router import product_router

app = FastAPI()

config_file = open('./config/logger.json')
logging.config.dictConfig(json.load(config_file))


@app.on_event("startup")
async def db_init() -> None:
    try:
        await init_tables_and_data()
    except ConnectionRefusedError as err:
        raise Exception('Please check your docker container') from err


app.include_router(product_router, tags=['product'], prefix='/api/product')
app.include_router(cart_router, tags=['cart'], prefix='/api/cart')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

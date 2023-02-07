from sqlalchemy import Column, Integer, String, DECIMAL

from config.db import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    price = Column(DECIMAL(11, 2), nullable=False)

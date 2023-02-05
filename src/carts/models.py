from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True, index=True)
    product = Column(Integer, ForeignKey('products.id'), nullable=False)
    price = Column(Integer, ForeignKey('products.price'), nullable=False)
    quantity = Column(Integer, nullable=False)
from sqlalchemy import Column, Integer, String, MetaData, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Products(Base):
    __tablename__ = 'tb_products'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(50), nullable=False)
    description   = Column(String(100), nullable=False)
    price         = Column(Float, nullable=False)


    def __init__(self, name=name, description=description, price=price):
        self.name = name
        self.description = description
        self.price = price


    def __repr__(self):
        return '<Product %r>' % (self.name)
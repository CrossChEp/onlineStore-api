from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    products = relationship('Product', backref='user')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('users.id'))
    sex = Column(String)
    type = Column(String)
    name = Column(String)
    description = Column(String)
    sizes = Column(JSON)
    price = Column(Float)


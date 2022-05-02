from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Float, Table, DATE
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


UserAndProductRelation = Table(
    'user_and_product_relation',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    products = relationship('Product', backref='user', cascade="all, delete")
    bag = relationship('Product', secondary=UserAndProductRelation,
                       backref='user_bag', cascade="all, delete")
    orders = relationship('Order', backref='user_orders', cascade="all, delete")


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
    people_bag = relationship('User', secondary=UserAndProductRelation,
                              backref='product', cascade="all, delete")


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey('users.id'))
    content = Column(JSON)
    date = Column(DATE)
    status = Column(String)
    address = Column(String)
    index = Column(Integer)
    price_sum = Column(Float)



from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Float,
    Boolean,
    Date,
    ForeignKey,
    Index,
    )

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as python_datetime
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types import TSVectorType



DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
#make_searchable()

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    owner = Column(Integer, ForeignKey('user.id'))
    name = Column(Text,nullable=False)
    picture = Column(Text,nullable=False)
    description = Column(Text,nullable=False) 
    category = Column(Text,nullable=False)
    condition = Column(Text,nullable=False)
    phone = Column(Text,nullable=False)
    email = Column(Text,nullable=False)
    oncampus = Column(Text,nullable=False)
    price = Column(Text,nullable=False)
    time = Column(DateTime,nullable=False)
    #search_vector = Column(TSVectorType('name'))

    def __init__(self,name = "",picture = "",description = "",category = "",\
                 condition = "",phone = "",email = "",oncampus = "",price = ""):
        self.name = name
        self.picture = picture
        self.description = description
        self.category = category
        self.condition = condition
        self.phone = phone
        self.email = email
        self.oncampus = oncampus
        self.price = price
        self.time = python_datetime.now()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    email = Column(Text,nullable=True)
    password = Column(Text,nullable=True)
    fname = Column(Text,nullable=True)
    lname = Column(Text,nullable=True)
    phone = Column(Text,nullable=True)
    address = Column(Text,nullable=True)
    oncampus = Column(Text,nullable=True)
    time = Column(DateTime,nullable=False)
    products = relationship(Product)

    def __init__(self,email = "",password = "",fname = "",lname = "",phone = "",address = "",oncampus = ""):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.oncampus = oncampus
        self.address = address
        self.time = python_datetime.now()

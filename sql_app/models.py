from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from .database import Base


class Product(Base):
    __tablename__ = "products"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
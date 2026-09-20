from sqlalchemy import Column, String, Integer, Float

from src.database.database import Base

class ProductsTable(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)


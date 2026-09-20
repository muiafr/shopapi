from sqlalchemy import Column, String, Integer, Numeric

from src.database.database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String)


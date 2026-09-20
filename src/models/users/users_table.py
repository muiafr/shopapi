

from sqlalchemy import Column, Integer, String, Numeric

from src.database.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    balance = Column(Numeric(10,2), nullable=False, default=0)
    password = Column(String, nullable=False)

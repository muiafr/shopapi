

from sqlalchemy import Column, Integer, String, Float, Numeric

from src.database.database import Base


class UsersTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    telephone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    balance = Column(Numeric(10,2), default=0 )
    password = Column(String, nullable=False)

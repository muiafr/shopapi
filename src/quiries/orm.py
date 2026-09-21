from sqlalchemy.orm import Session

from src.database.database import SessionLocal
from src.models.users.users_table import Users
from src.schemas.users.user import UserRead


class Orm:

    @staticmethod
    def insert_user():
        with SessionLocal() as session:
            dima = Users(nickname = "dima123",firstname= "dima", lastname = "yud" ,email = "dia@a.pu", password = "Doomch1k134567", balance = 1000, phone = "12333123" )
            session.add(dima)


            session.add_all([dima])
            session.commit()

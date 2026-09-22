

from src.database.database import SessionLocal
from src.models.users.users_table import Users
from src.schemas.users.user import UserRead


class Orm:

    @staticmethod
    def insert_user():
        with SessionLocal() as session:
            dima = Users(nickname = "dima123",
                         firstname= "dima",
                         lastname = "yud",
                         email = "dia@a.pu",
                         password = "Doomch1k134567",
                         balance = 1000,
                         phone = "12333123")
            artem = Users(nickname="artem123",
                         firstname="artem",
                         lastname="yud",
                         email="art@a.pu",
                         password="Artem123@@",
                         balance=1000,
                         phone="13333123")
            session.add_all([dima, artem])
            session.commit()

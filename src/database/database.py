from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import get_config

engine = create_engine(get_config(),  pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    with SessionLocal() as db:
        try:
            yield db
        except Exception:
            db.rollback()
            raise


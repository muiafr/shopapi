from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session


from src.database.database import get_db
from src.models.users.users_table import Users
from src.schemas.users.user import UserCreate, UserUpdate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead])
async def get_users(db: Session = Depends(get_db) ):
    users = db.scalars(select(Users)).all()
    return users




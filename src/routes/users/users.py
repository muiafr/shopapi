from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session


from src.database.database import get_db
from src.models.users.users_table import Users
from src.schemas.users.user import UserCreate, UserUpdate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead], status_code=200)
async def get_users(db: Session = Depends(get_db) ):
    users = db.scalars(select(Users)).all()
    return users



@router.get('/{id}', response_model=UserRead, status_code=200)
async def get_user(id: int, db: Session = Depends(get_db)):
        user = db.query(Users).filter(Users.id == id).first()
        return user


@router.post("/create_user", response_model=UserRead, status_code=200)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = Users(
        nickname = user.nickname,
        firstname = user.firstname,
        lastname = user.lastname,
        phone = user.phone,
        email = user.email,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete("/{id}", response_model=UserRead, status_code=200)
async def delete_user(id: int, db: Session = Depends(get_db)):
    user=db.get(Users,id)

    if user is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(user)
    db.commit()

    return Response(status_code=204)
from pydantic import EmailStr, Field, field_validator, model_validator
from typing import Annotated
from src.schemas.common import Response, Request, Money

Name = Annotated[str,Field(min_length=3, max_length=50)]
Email = Annotated[EmailStr, Field(max_length=50)]
Password = Annotated[str,Field(min_length=8, max_length=50)]
Phone = Annotated[str, Field(min_length=6, max_length=15)]

class UserCreate(Request):
    firstname:Name
    lastname:Name
    nickname:Name
    email:Email
    password:Password
    phone:Phone

    @field_validator('password')
    @classmethod
    def strong_password(cls, value):
        if not any(c in '!@#$%^&*' for c in value):
            raise ValueError('Password must include a symbol (!@#$%^&*)')
        return value


class UserUpdate(Request):
    nickname: Name | None = None
    email: Email | None = None
    phone: Phone | None = None
    password: Password | None = None

    @model_validator(mode='after')
    def validate_changes(self):
        if not self.model_fields_set or any(getattr(self, k) is None for k in self.model_fields_set):
            raise ValueError('Provide at least one non-null field')
        if self.password is not None:
            UserCreate.strong_password(self.password)
        return self


class UserRead(Response):
    id: int
    nickname: str
    firstname: str
    lastname: str
    email: str
    phone: str
    balance: Money
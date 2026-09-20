from typing import Annotated

from pydantic import Field, model_validator

from src.schemas.common import Request, Response, PositiveMoney

Name = Annotated[str, Field(min_length=1, max_length=20)]
Description = Annotated[str, Field(max_length=500)]
Category = Annotated[str, Field(min_length=1, max_length=20)]


class CreateProduct(Request):
    name: Name
    description: Description | None = None
    price: PositiveMoney
    category: Category | None = None


class UpdateProduct(Request):
    name: Name | None = None
    description: Description | None = None
    price: PositiveMoney | None = None
    category: Category | None = None

    @model_validator(mode="after")
    def validate_changes(self):
        if not self.model_fields_set:
            raise ValueError("Укажи хотя бы одно поле")

        for field in ("name", "price"):
            if field in self.model_fields_set and getattr(self, field) is None:
                raise ValueError(f"Поле {field} не может быть null")

        return self


class ReadProduct(Response):
    id: int
    name: str
    description: str | None
    price: PositiveMoney
    category: str | None
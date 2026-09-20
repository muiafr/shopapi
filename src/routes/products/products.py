from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.products.products_table import Products
from src.schemas.products.product import ReadProduct, UpdateProduct, CreateProduct

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/", response_model=list[ReadProduct])
def get_products(db: Session = Depends(get_db)):
    products = db.scalars(select(Products)).all()
    return products


@router.get("/{id}", response_model=ReadProduct)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.get(Products, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/create", response_model=ReadProduct)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    new_product = Products(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.patch("/{id}", response_model=ReadProduct)
def update_product(id: int, product: UpdateProduct, db: Session = Depends(get_db),
):
    db_product = db.get(Products, id)

    if db_product is None:
        raise HTTPException(status_code=404,detail="Product not found")

    changes = product.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)

    return db_product

@router.delete("/{id}", status_code=204)
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.get(Products, id)

    if product is None:
        raise HTTPException(status_code=404,detail="Product not found")

    db.delete(product)
    db.commit()

    return Response(status_code=204)
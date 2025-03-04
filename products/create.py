from fastapi import APIRouter, Depends, HTTPException

from db_connect import conn
from products.models import Product
from utils import admin_required

router = APIRouter()


@router.post("/create")
async def create(product: Product, _: dict = Depends(admin_required)):
    with conn.cursor() as cur:
        cur.execute(
            f"INSERT INTO products (name, description, price) VALUES ('{product.name}', '{product.description}', {product.price}) RETURNING id")
        created_product = cur.fetchone()
        conn.commit()
        if not created_product:
            raise HTTPException(400)
        return {'id': created_product['id']}

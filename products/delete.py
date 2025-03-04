from fastapi import APIRouter, Depends

from db_connect import conn
from products.models import Product
from utils import admin_required

router = APIRouter()


@router.delete("/delete/{product_id}")
async def create(product_id: int, _: dict = Depends(admin_required)):
    with conn.cursor() as cur:
        cur.execute(
            f"DELETE FROM products WHERE id={product_id}")
        conn.commit()
        return {'success': True}

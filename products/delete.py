from fastapi import APIRouter

from db_connect import conn

router = APIRouter()


@router.delete("/delete/{product_id}")
async def create(product_id: int):
    with conn.cursor() as cur:
        cur.execute(
            f"DELETE FROM products WHERE id={product_id}")
        conn.commit()
        return {'success': True}

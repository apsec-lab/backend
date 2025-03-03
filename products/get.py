from fastapi import APIRouter, Depends

from utils import auth_required
from db_connect import conn

router = APIRouter()


@router.get('/get')
async def get(_: dict = Depends(auth_required)):
    with conn.cursor() as cur:
        products = cur.execute('SELECT * FROM products').fetchall()
        print(products)
        return products

from fastapi import APIRouter, Depends

from utils import auth_required
from db_connect import conn

router = APIRouter()


@router.get('/get')
async def get(_: dict = Depends(auth_required), search: str | None = None):
    with conn.cursor() as cur:
        query = 'SELECT * FROM products' if not search else f"SELECT * FROM products WHERE LOWER(name) LIKE '%{str(search).lower()}%'"
        products = cur.execute(query).fetchall()
        return products

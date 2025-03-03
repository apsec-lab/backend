from fastapi import APIRouter
from products.get import router as get_router

router = APIRouter(prefix='/products', tags=['products'])

router.include_router(get_router)

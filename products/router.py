from fastapi import APIRouter
from products.get import router as get_router
from products.create import router as create_router
from products.delete import  router as delete_router

router = APIRouter(prefix='/products', tags=['products'])

router.include_router(get_router)
router.include_router(create_router)
router.include_router(delete_router)
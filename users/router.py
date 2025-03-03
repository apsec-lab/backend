from fastapi import APIRouter

from users.create import router as create_router
from users.auth import router as auth_router
from users.me import router as me_router

router = APIRouter(prefix='/users', tags=['users'])

router.include_router(create_router)
router.include_router(auth_router)
router.include_router(me_router)

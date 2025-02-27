from fastapi import APIRouter, Depends

from utils import auth_required

router = APIRouter()


@router.get('/me')
async def me(user: dict = Depends(auth_required)):
    return {'user': {'username': user['username'], 'isAdmin': user['isAdmin']}}

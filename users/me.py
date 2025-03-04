from fastapi import APIRouter, Depends, HTTPException

from db_connect import conn
from utils import auth_required

router = APIRouter()


@router.get('/me')
async def me(user: dict = Depends(auth_required)):
    with conn.cursor() as cur:
        userDb = cur.execute(f"SELECT id from users where username='{user['username']}';").fetchone()
        if userDb:
            return {'username': user['username'], 'isAdmin': user['isAdmin'], 'id': userDb['id']}
    raise HTTPException(403)
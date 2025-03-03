from datetime import timedelta

from db_connect import conn
from users.models import CreateUserPayload

from fastapi import HTTPException, Response, APIRouter

from users.utils import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post('/auth')
async def auth(response: Response, auth_user: CreateUserPayload):
    with conn.cursor() as cur:
        user = cur.execute(f"SELECT * from users where username='{auth_user.username}';").fetchone()
        if not user:
            raise HTTPException(status_code=400, detail='invalid data')
        verify_status = verify_password(auth_user.password, user['password'])
        if not verify_status:
            raise HTTPException(status_code=400, detail='invalid data')

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"username": auth_user.username, "isAdmin": user['isAdmin']}, expires_delta=access_token_expires
        )
        response.set_cookie(
            key='access',
            value=access_token,
            httponly=True,
            samesite='lax',
        )
    return {'username': auth_user.username}

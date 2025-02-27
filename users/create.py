from datetime import timedelta

from fastapi import HTTPException, Response, APIRouter

from db_connect import conn
from users.models import CreateUserPayload
from users.utils import create_access_token, get_password_hash, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/create")
async def create(response: Response, create_user: CreateUserPayload):
    with conn.cursor() as cur:
        user = cur.execute(f"SELECT username from users where username='{create_user.username}';").fetchone()
        if user:
            raise HTTPException(status_code=400, detail='user with this username exists')
        hashed_password = get_password_hash(create_user.password)
        cur.execute(
            f"INSERT INTO users (username, password) VALUES ('{create_user.username}', '{hashed_password}')")
        conn.commit()
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"username": create_user.username}, expires_delta=access_token_expires
        )
        response.set_cookie(key='access', value=access_token, httponly=True)

    return {'username': create_user.username}

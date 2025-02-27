from fastapi import Cookie, HTTPException
from users.utils import SECRET_KEY, ALGORITHM
import jwt


async def auth_required(access: str = Cookie(None)):
    if not access:
        raise HTTPException(403)
    data = jwt.decode(
        access,
        SECRET_KEY,
        algorithms=[ALGORITHM],
        verify=False,
        options={'verify_signature': False})
    if 'username' in data and data['username'] and 'isAdmin' in data:
        return {
            'username': data['username'],
            'isAdmin': data['isAdmin'] or False
        }
    raise HTTPException(403)

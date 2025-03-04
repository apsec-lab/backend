from fastapi import Response, APIRouter

router = APIRouter()


@router.post('/logout')
async def auth(response: Response):
    response.set_cookie(
        key='access',
        value='',
        httponly=True,
        samesite='lax',
    )

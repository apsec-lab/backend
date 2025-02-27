from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

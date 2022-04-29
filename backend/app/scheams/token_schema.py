from pydantic import BaseModel
from typing import Optional


class BaseToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    is_user: Optional[bool] = False
    is_doctor: Optional[bool] = False

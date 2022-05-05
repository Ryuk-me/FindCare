from pydantic import BaseModel
from typing import Optional, Literal


class BaseToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    status: Optional[Literal['admin', 'user', 'doctor']]
    email: Optional[str] = None

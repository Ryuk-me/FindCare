from pydantic import BaseModel


class ChangePassword(BaseModel):
    password: str
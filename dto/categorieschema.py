from pydantic import BaseModel
from typing import Optional



class CategorieSchema(BaseModel):
    name: str
    image: str
    description: str



class TokenSchema(BaseModel):
    id: str
    email: str


class CurrentUserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

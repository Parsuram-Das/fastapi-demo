from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
    id: int
    email: str
    name: str
    age :Optional[int] = None
        
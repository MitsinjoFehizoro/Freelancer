from pydantic import BaseModel, Field, EmailStr, computed_field
from uuid import UUID
from typing import Annotated, Literal
from datetime import datetime


class User(BaseModel):
    id: Annotated[UUID, Field(strict=True)]
    username: Annotated[str, Field(pattern=r"^\w{3,20}$")]
    email: EmailStr
    role: Literal["client", "freelancer"]

    @computed_field
    def created_at(self) -> datetime:
        return datetime.now()

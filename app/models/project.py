from pydantic import Field, BaseModel, PositiveFloat, field_validator
from typing import Annotated
from datetime import date
from .profile import Profile


class Project(BaseModel):
    title: Annotated[str, Field(min_length=3, max_length=100)]
    description: Annotated[str, Field(min_length=20)]
    budget: PositiveFloat
    deadline: date
    client: Profile
    freelancer: Profile

    @field_validator("deadline", mode="after")
    @classmethod
    def validate_deadline(cls, value: date) -> date:
        if (value - date.today()).days < 3:
            raise ValueError("deadline must be at least 3 days in the future.")
        return date

    @field_validator("client", mode="after")
    @classmethod
    def validate_client(cls, value: Profile) -> Profile:
        if value.role != "client":
            raise ValueError("The client must be a user with role 'client'.")
        return value

    @field_validator("freelancer", mode="after")
    @classmethod
    def validate_freelancer(cls, value: Profile) -> Profile:
        if value.role != "freelancer":
            raise ValueError("The freelancer must be a user with role 'freelancer'.")
        return value

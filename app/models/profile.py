from pydantic import (
    Field,
    PositiveFloat,
    model_validator,
)
from .user import User
from typing import Annotated
from typing_extensions import Self

SkillsItemType = Annotated[str, Field(pattern=r"^\w{2,30}$")]


class Profile(User):
    bio: Annotated[str | None, Field(max_length=200)]
    skills: list[SkillsItemType]
    hourly_rate: PositiveFloat | None = None

    @model_validator(mode="after")
    def validate_hourly_rate(self) -> Self:
        if self.role == "freelancer":
            if (
                self.hourly_rate == None
                or self.hourly_rate < 5
                or self.hourly_rate > 200
            ):
                raise ValueError("hourly_rate must be in 5 - 200$.")
        else:
            self.hourly_rate = None
        return self

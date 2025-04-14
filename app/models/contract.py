from pydantic import (
    BaseModel,
    NonNegativeFloat,
    field_validator,
    ValidationInfo,
    model_validator,
)
from typing import Annotated, Literal, Self
from uuid import UUID
from .project import Project
from datetime import date


class Contract(BaseModel):
    id: UUID
    project: Project
    start_date: date
    end_date: date
    status: Literal["pending", "active", "completed", "cancelled"]
    paiement_advance: NonNegativeFloat = 0.0

    @field_validator("end_date", mode="after")
    @classmethod
    def validate_end_date(cls, value: date, info: ValidationInfo) -> date:
        if (value - info.data["start_date"]).days < 0:
            raise ValueError("end_date of contract must be after start_date")
        if (value - info.data["start_date"]).days > 90:
            raise ValueError("The constract's duration must be less than 90 days.")
        return value

    @model_validator(mode="after")
    def validate_paiement_advance(self) -> Self:
        if self.paiement_advance > self.project.budget:
            raise ValueError(
                "paiement_advance must be less than or equal the project's budget"
            )
        return self

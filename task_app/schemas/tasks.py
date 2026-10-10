from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = None
    # было default=10 при ge=1, le=5 - значение по умолчанию выходило за границы
    priority: int = Field(default=3, ge=1, le=5)
    is_done: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = None
    priority: Optional[int] = Field(default=None, ge=1, le=5)
    is_done: Optional[bool] = None

    @field_validator("title", "priority", "is_done")
    @classmethod
    def not_null(cls, value):
        # description можно обнулить, остальные поля в БД NOT NULL
        if value is None:
            raise ValueError("This field cannot be null")
        return value


class TaskOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str]
    priority: int
    is_done: bool
    created_at: datetime
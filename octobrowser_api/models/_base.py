from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar('T')


class OctoModel(BaseModel):
    model_config = ConfigDict(
        extra='ignore',
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
    )


class Response(OctoModel, Generic[T]):
    success: bool = True
    msg: str | None = ''
    code: str | None = None
    data: T | None = None


class ListResponse(OctoModel, Generic[T]):
    success: bool = True
    msg: str | None = ''
    code: str | None = None
    data: list[T] = Field(default_factory=list)
    total_count: int = 0
    page: int = 0

from __future__ import annotations

from typing import Any

from pydantic import Field

from ..enums import ErrorCode
from ._base import OctoModel

__all__ = [
    'ErrorResponse',
    'ValidationError',
    'HTTPValidationError',
    'ValidationErrorItem',
    'CloudValidationError',
]


class ErrorResponse(OctoModel):
    success: bool = False
    msg: str = 'Error detail'
    code: ErrorCode | str = Field(union_mode='left_to_right')
    data: str | list[Any] | dict[str, Any] | None = None


class ValidationError(OctoModel):
    loc: list[str | int]
    msg: str
    type: str


class HTTPValidationError(OctoModel):
    detail: list[ValidationError] = Field(default_factory=list)


class ValidationErrorItem(OctoModel):
    type: str | None = None
    loc: list[str | int] = Field(default_factory=list)
    msg: str | None = None
    input: Any = None


class CloudValidationError(OctoModel):
    validation_error: dict[str, list[ValidationErrorItem]] = Field(default_factory=dict)

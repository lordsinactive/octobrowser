from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

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
    code: Union[ErrorCode, str] = Field(union_mode='left_to_right')
    data: Optional[Union[str, List[Any], Dict[str, Any]]] = None


class ValidationError(OctoModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class HTTPValidationError(OctoModel):
    detail: List[ValidationError] = Field(default_factory=list)


class ValidationErrorItem(OctoModel):
    type: Optional[str] = None
    loc: List[Union[str, int]] = Field(default_factory=list)
    msg: Optional[str] = None
    input: Any = None


class CloudValidationError(OctoModel):
    validation_error: Dict[str, List[ValidationErrorItem]] = Field(default_factory=dict)

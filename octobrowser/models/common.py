from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ..enums import ErrorCode
from ._base import OctoModel

__all__ = [
    "DefaultResp",
    "BaseErrorResponse",
    "ValidationError",
    "HTTPValidationError",
]


class DefaultResp(OctoModel):
    success: bool = True
    msg: str = ""
    code: str = ""
    data: Optional[Union[str, List[Any], Dict[str, Any]]] = None


class BaseErrorResponse(OctoModel):
    success: bool = False
    msg: str = "Error detail"
    code: ErrorCode
    data: Optional[Union[str, List[Any], Dict[str, Any]]] = None


class ValidationError(OctoModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class HTTPValidationError(OctoModel):
    detail: List[ValidationError] = Field(default_factory=list)

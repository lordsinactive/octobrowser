from __future__ import annotations
from typing import List, Optional

from pydantic import Field
from ._base import OctoModel

__all__ = [
    "TagCreate",
    "TagUpdate",
    "TagOut",
    "TagResponse",
    "TagsResponse",
]


class TagCreate(OctoModel):
    name: str
    color: str = "grey"


class TagUpdate(OctoModel):
    name: str
    color: Optional[str] = None


class TagOut(OctoModel):
    uuid: str
    name: str
    color: Optional[str] = None


class TagResponse(OctoModel):
    success: bool = True
    msg: str = ""
    code: Optional[str] = None
    data: Optional[TagOut] = None


class TagsResponse(OctoModel):
    success: bool = True
    msg: str = ""
    code: Optional[str] = None
    data: List[TagOut] = Field(default_factory=list)

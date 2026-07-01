from __future__ import annotations
from typing import Optional

from ._base import OctoModel

__all__ = [
    'TagCreate',
    'TagUpdate',
    'Tag',
]


class TagCreate(OctoModel):
    name: str
    color: str = 'grey'


class TagUpdate(OctoModel):
    name: str
    color: Optional[str] = None


class Tag(OctoModel):
    uuid: str
    name: str
    color: Optional[str] = None

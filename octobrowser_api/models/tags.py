from __future__ import annotations

from ..enums import TagColor
from ._base import OctoModel

__all__ = [
    'TagCreate',
    'TagUpdate',
    'Tag',
]


class TagCreate(OctoModel):
    name: str
    color: TagColor = TagColor.GREY


class TagUpdate(OctoModel):
    name: str
    color: TagColor | None = None


class Tag(OctoModel):
    uuid: str
    name: str
    color: TagColor | None = None

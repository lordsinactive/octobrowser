from __future__ import annotations

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
    color: str | None = None


class Tag(OctoModel):
    uuid: str
    name: str
    color: str | None = None

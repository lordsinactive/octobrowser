from __future__ import annotations

from typing import Any

from ._base import OctoModel

__all__ = [
    'FolderCreate',
    'FoldersCreate',
    'FolderUpdate',
    'Folder',
]


class FolderCreate(OctoModel):
    name: str
    assignable_wo_permission: bool | None = None


class FoldersCreate(OctoModel):
    folders: list[FolderCreate | dict[str, Any]]


class FolderUpdate(OctoModel):
    name: str | None = None
    assignable_wo_permission: bool | None = None


class Folder(OctoModel):
    uuid: str
    name: str
    assignable_wo_permission: bool = False

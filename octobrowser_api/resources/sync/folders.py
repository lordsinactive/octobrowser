from __future__ import annotations

import builtins
from typing import Any, overload

from ...models import (
    Folder,
    FolderCreate,
    FoldersCreate,
    FolderUpdate,
    ListResponse,
    Response,
)
from .._base import Resource, unwrap


class Folders(Resource):
    def list(self) -> builtins.list[Folder]:
        return self._transport.request('GET', '/folders', out=ListResponse[Folder]).data

    @overload
    def create(self, data: FolderCreate, /) -> Folder: ...
    @overload
    def create(
        self, *, name: str, assignable_wo_permission: bool | None = None
    ) -> Folder: ...
    def create(self, data: FolderCreate | None = None, **fields: Any) -> Folder:
        item = data if data is not None else FolderCreate(**fields)
        created = self.create_many([item])
        return unwrap(created[0] if created else None)

    @overload
    def create_many(self, data: FoldersCreate, /) -> builtins.list[Folder]: ...
    @overload
    def create_many(
        self, folders: builtins.list[FolderCreate | dict[str, Any]], /
    ) -> builtins.list[Folder]: ...
    def create_many(
        self, data: FoldersCreate | builtins.list[FolderCreate | dict[str, Any]], /
    ) -> builtins.list[Folder]:
        body = data if isinstance(data, FoldersCreate) else FoldersCreate(folders=data)
        resp = self._transport.request(
            'POST', '/folders', body=body, out=Response[builtins.list[Folder]]
        )
        return unwrap(resp.data)

    @overload
    def update(self, folder: str, data: FolderUpdate, /) -> Folder: ...
    @overload
    def update(
        self,
        folder: str,
        /,
        *,
        name: str | None = None,
        assignable_wo_permission: bool | None = None,
    ) -> Folder: ...
    def update(
        self, folder: str, data: FolderUpdate | None = None, **fields: Any
    ) -> Folder:
        body = data if data is not None else FolderUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/folders/{folder}', body=body, out=Response[Folder]
        )
        return unwrap(resp.data)

    def delete(self, folder: str) -> None:
        self._transport.request('DELETE', f'/folders/{folder}')

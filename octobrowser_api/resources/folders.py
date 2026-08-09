from __future__ import annotations

import builtins
from typing import Any, overload

from ..models import (
    Folder,
    FolderCreate,
    FoldersCreate,
    FolderUpdate,
    ListResponse,
    Response,
)
from ._base import AsyncResource, unwrap


class AsyncFolders(AsyncResource):
    async def list(self) -> builtins.list[Folder]:
        resp = await self._transport.request(
            'GET', '/folders', out=ListResponse[Folder]
        )
        return resp.data

    @overload
    async def create(self, data: FolderCreate, /) -> Folder: ...
    @overload
    async def create(
        self, *, name: str, assignable_wo_permission: bool | None = None
    ) -> Folder: ...
    async def create(self, data: FolderCreate | None = None, **fields: Any) -> Folder:
        item = data if data is not None else FolderCreate(**fields)
        created = await self.create_many([item])
        return unwrap(created[0] if created else None)

    @overload
    async def create_many(self, data: FoldersCreate, /) -> builtins.list[Folder]: ...
    @overload
    async def create_many(
        self, folders: builtins.list[FolderCreate | dict[str, Any]], /
    ) -> builtins.list[Folder]: ...
    async def create_many(
        self, data: FoldersCreate | builtins.list[FolderCreate | dict[str, Any]], /
    ) -> builtins.list[Folder]:
        body = data if isinstance(data, FoldersCreate) else FoldersCreate(folders=data)
        resp = await self._transport.request(
            'POST', '/folders', body=body, out=Response[builtins.list[Folder]]
        )
        return unwrap(resp.data)

    @overload
    async def update(self, folder: str, data: FolderUpdate, /) -> Folder: ...
    @overload
    async def update(
        self,
        folder: str,
        /,
        *,
        name: str | None = None,
        assignable_wo_permission: bool | None = None,
    ) -> Folder: ...
    async def update(
        self, folder: str, data: FolderUpdate | None = None, **fields: Any
    ) -> Folder:
        body = data if data is not None else FolderUpdate(**fields)
        resp = await self._transport.request(
            'PATCH', f'/folders/{folder}', body=body, out=Response[Folder]
        )
        return unwrap(resp.data)

    async def delete(self, folder: str) -> None:
        await self._transport.request('DELETE', f'/folders/{folder}')

from __future__ import annotations
from typing import Any, List, Optional, overload

from ._base import AsyncResource, unwrap
from ..models import ListResponse, Response, Tag, TagCreate, TagUpdate


class AsyncTags(AsyncResource):
    async def list(self) -> List[Tag]:
        resp = await self._transport.request('GET', '/tags', out=ListResponse[Tag])
        return resp.data

    @overload
    async def create(self, data: TagCreate, /) -> Tag: ...
    @overload
    async def create(self, *, name: str, color: str = 'grey') -> Tag: ...
    async def create(self, data: Optional[TagCreate] = None, **fields: Any) -> Tag:
        body = data if data is not None else TagCreate(**fields)
        resp = await self._transport.request(
            'POST', '/tags', body=body, out=Response[Tag]
        )
        return unwrap(resp.data)

    @overload
    async def update(self, uuid: str, data: TagUpdate, /) -> Tag: ...
    @overload
    async def update(
        self, uuid: str, /, *, name: str, color: Optional[str] = None
    ) -> Tag: ...
    async def update(
        self, uuid: str, data: Optional[TagUpdate] = None, **fields: Any
    ) -> Tag:
        body = data if data is not None else TagUpdate(**fields)
        resp = await self._transport.request(
            'PATCH', f'/tags/{uuid}', body=body, out=Response[Tag]
        )
        return unwrap(resp.data)

    async def delete(self, uuid: str) -> None:
        await self._transport.request('DELETE', f'/tags/{uuid}')

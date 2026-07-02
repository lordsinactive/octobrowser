from __future__ import annotations
from typing import List

from ._base import AsyncResource, query
from ..models import Extension, ExtensionsDelete, ListResponse


class AsyncExtensions(AsyncResource):
    async def list(self, *, start: int = 0, limit: int = 25) -> List[Extension]:
        params = query(start=start, limit=limit)
        resp = await self._transport.request(
            'GET', '/teams/extensions', params=params, out=ListResponse[Extension]
        )
        return resp.data

    async def delete(self, uuids: List[str]) -> None:
        await self._transport.request(
            'DELETE', '/teams/extensions', body=ExtensionsDelete(uuids=uuids)
        )

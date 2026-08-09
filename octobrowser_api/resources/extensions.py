from __future__ import annotations

import builtins

from ..models import Extension, ExtensionsDelete, ListResponse
from ._base import AsyncResource, query


class AsyncExtensions(AsyncResource):
    async def list(self, *, start: int = 0, limit: int = 25) -> builtins.list[Extension]:
        params = query(start=start, limit=limit)
        resp = await self._transport.request(
            'GET', '/teams/extensions', params=params, out=ListResponse[Extension]
        )
        return resp.data

    async def delete(self, uuids: builtins.list[str]) -> None:
        await self._transport.request(
            'DELETE', '/teams/extensions', body=ExtensionsDelete(uuids=uuids)
        )

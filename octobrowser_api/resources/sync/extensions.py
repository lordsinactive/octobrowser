from __future__ import annotations

import builtins

from ...models import Extension, ExtensionsDelete, ListResponse
from .._base import Resource, query


class Extensions(Resource):
    def list(self, *, start: int = 0, limit: int = 25) -> builtins.list[Extension]:
        params = query(start=start, limit=limit)
        return self._transport.request(
            'GET', '/teams/extensions', params=params, out=ListResponse[Extension]
        ).data

    def delete(self, uuids: builtins.list[str]) -> None:
        self._transport.request(
            'DELETE', '/teams/extensions', body=ExtensionsDelete(uuids=uuids)
        )

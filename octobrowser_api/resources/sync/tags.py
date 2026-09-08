from __future__ import annotations

import builtins
from typing import Any, overload

from ...enums import TagColor
from ...models import ListResponse, Response, Tag, TagCreate, TagUpdate
from .._base import Resource, unwrap


class Tags(Resource):
    def list(self) -> builtins.list[Tag]:
        return self._transport.request('GET', '/tags', out=ListResponse[Tag]).data

    @overload
    def create(self, data: TagCreate, /) -> Tag: ...
    @overload
    def create(self, *, name: str, color: TagColor = TagColor.GREY) -> Tag: ...
    def create(self, data: TagCreate | None = None, **fields: Any) -> Tag:
        body = data if data is not None else TagCreate(**fields)
        resp = self._transport.request('POST', '/tags', body=body, out=Response[Tag])
        return unwrap(resp.data)

    @overload
    def update(self, uuid: str, data: TagUpdate, /) -> Tag: ...
    @overload
    def update(
        self, uuid: str, /, *, name: str, color: TagColor | None = None
    ) -> Tag: ...
    def update(self, uuid: str, data: TagUpdate | None = None, **fields: Any) -> Tag:
        body = data if data is not None else TagUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/tags/{uuid}', body=body, out=Response[Tag]
        )
        return unwrap(resp.data)

    def delete(self, uuid: str) -> None:
        self._transport.request('DELETE', f'/tags/{uuid}')

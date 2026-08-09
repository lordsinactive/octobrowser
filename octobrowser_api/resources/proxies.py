from __future__ import annotations

import builtins
from typing import Any, overload

from ..enums import ProxyType
from ..models import ListResponse, Proxy, ProxyCreate, ProxyUpdate, Response
from ._base import AsyncResource, unwrap


class AsyncProxies(AsyncResource):
    async def list(self) -> builtins.list[Proxy]:
        resp = await self._transport.request('GET', '/proxies', out=ListResponse[Proxy])
        return resp.data

    @overload
    async def create(self, data: ProxyCreate, /) -> Proxy: ...
    @overload
    async def create(
        self,
        *,
        type: ProxyType,
        host: str,
        port: int,
        title: str,
        login: str | None = None,
        password: str | None = None,
        change_ip_url: str | None = None,
        external_id: str | None = None,
    ) -> Proxy: ...
    async def create(self, data: ProxyCreate | None = None, **fields: Any) -> Proxy:
        body = data if data is not None else ProxyCreate(**fields)
        resp = await self._transport.request(
            'POST', '/proxies', body=body, out=Response[Proxy]
        )
        return unwrap(resp.data)

    @overload
    async def update(self, uuid: str, data: ProxyUpdate, /) -> Proxy: ...
    @overload
    async def update(
        self,
        uuid: str,
        /,
        *,
        type: ProxyType | None = None,
        host: str | None = None,
        port: int | None = None,
        login: str | None = None,
        password: str | None = None,
        change_ip_url: str | None = None,
        title: str | None = None,
        external_id: str | None = None,
    ) -> Proxy: ...
    async def update(
        self, uuid: str, data: ProxyUpdate | None = None, **fields: Any
    ) -> Proxy:
        body = data if data is not None else ProxyUpdate(**fields)
        resp = await self._transport.request(
            'PATCH', f'/proxies/{uuid}', body=body, out=Response[Proxy]
        )
        return unwrap(resp.data)

    async def delete(self, uuid: str) -> None:
        await self._transport.request('DELETE', f'/proxies/{uuid}')

from __future__ import annotations
from typing import Any, List, Optional, overload

from ._base import AsyncResource, Resource, unwrap
from ..enums import ProxyType
from ..models import ListResponse, Proxy, ProxyCreate, ProxyUpdate, Response


class Proxies(Resource):
    def list(self) -> List[Proxy]:
        return self._transport.request('GET', '/proxies', out=ListResponse[Proxy]).data

    @overload
    def create(self, data: ProxyCreate, /) -> Proxy: ...
    @overload
    def create(
        self,
        *,
        type: ProxyType,
        host: str,
        port: int,
        title: str,
        login: Optional[str] = None,
        password: Optional[str] = None,
        change_ip_url: Optional[str] = None,
        external_id: Optional[str] = None,
    ) -> Proxy: ...
    def create(self, data: Optional[ProxyCreate] = None, **fields: Any) -> Proxy:
        body = data if data is not None else ProxyCreate(**fields)
        resp = self._transport.request(
            'POST', '/proxies', body=body, out=Response[Proxy]
        )
        return unwrap(resp.data)

    @overload
    def update(self, uuid: str, data: ProxyUpdate, /) -> Proxy: ...
    @overload
    def update(
        self,
        uuid: str,
        /,
        *,
        type: Optional[ProxyType] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        login: Optional[str] = None,
        password: Optional[str] = None,
        change_ip_url: Optional[str] = None,
        title: Optional[str] = None,
        external_id: Optional[str] = None,
    ) -> Proxy: ...
    def update(
        self, uuid: str, data: Optional[ProxyUpdate] = None, **fields: Any
    ) -> Proxy:
        body = data if data is not None else ProxyUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/proxies/{uuid}', body=body, out=Response[Proxy]
        )
        return unwrap(resp.data)

    def delete(self, uuid: str) -> None:
        self._transport.request('DELETE', f'/proxies/{uuid}')


class AsyncProxies(AsyncResource):
    async def list(self) -> List[Proxy]:
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
        login: Optional[str] = None,
        password: Optional[str] = None,
        change_ip_url: Optional[str] = None,
        external_id: Optional[str] = None,
    ) -> Proxy: ...
    async def create(self, data: Optional[ProxyCreate] = None, **fields: Any) -> Proxy:
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
        type: Optional[ProxyType] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
        login: Optional[str] = None,
        password: Optional[str] = None,
        change_ip_url: Optional[str] = None,
        title: Optional[str] = None,
        external_id: Optional[str] = None,
    ) -> Proxy: ...
    async def update(
        self, uuid: str, data: Optional[ProxyUpdate] = None, **fields: Any
    ) -> Proxy:
        body = data if data is not None else ProxyUpdate(**fields)
        resp = await self._transport.request(
            'PATCH', f'/proxies/{uuid}', body=body, out=Response[Proxy]
        )
        return unwrap(resp.data)

    async def delete(self, uuid: str) -> None:
        await self._transport.request('DELETE', f'/proxies/{uuid}')

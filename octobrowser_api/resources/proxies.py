from __future__ import annotations

import builtins
from typing import Any, Literal, overload

from ..enums import ProxyType, SynMode, VPNProtocol
from ..models import (
    ListResponse,
    Proxy,
    ProxyCreate,
    ProxyUpdate,
    Response,
    VPNProxyCreate,
    VPNProxyUpdate,
)
from ._base import AsyncResource, unwrap

VPN_FIELDS = frozenset({'conf', 'syn_mode', 'vpn_protocol'})


def is_vpn(fields: dict[str, Any]) -> bool:
    return fields.get('type') == ProxyType.VPN or not VPN_FIELDS.isdisjoint(fields)


class AsyncProxies(AsyncResource):
    async def list(self) -> builtins.list[Proxy]:
        resp = await self._transport.request('GET', '/proxies', out=ListResponse[Proxy])
        return resp.data

    @overload
    async def create(self, data: ProxyCreate | VPNProxyCreate, /) -> Proxy: ...
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
    @overload
    async def create(
        self,
        *,
        type: Literal[ProxyType.VPN],
        title: str,
        conf: str,
        syn_mode: SynMode | None = None,
        vpn_protocol: VPNProtocol | None = None,
        external_id: str | None = None,
    ) -> Proxy: ...
    async def create(
        self, data: ProxyCreate | VPNProxyCreate | None = None, **fields: Any
    ) -> Proxy:
        if data is None:
            data = VPNProxyCreate(**fields) if is_vpn(fields) else ProxyCreate(**fields)
        resp = await self._transport.request(
            'POST', '/proxies', body=data, out=Response[Proxy]
        )
        return unwrap(resp.data)

    @overload
    async def update(
        self, uuid: str, data: ProxyUpdate | VPNProxyUpdate, /
    ) -> Proxy: ...
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
    @overload
    async def update(
        self,
        uuid: str,
        /,
        *,
        type: Literal[ProxyType.VPN] | None = None,
        title: str | None = None,
        conf: str | None = None,
        syn_mode: SynMode | None = None,
        vpn_protocol: VPNProtocol | None = None,
        external_id: str | None = None,
    ) -> Proxy: ...
    async def update(
        self,
        uuid: str,
        data: ProxyUpdate | VPNProxyUpdate | None = None,
        **fields: Any,
    ) -> Proxy:
        if data is None:
            data = VPNProxyUpdate(**fields) if is_vpn(fields) else ProxyUpdate(**fields)
        resp = await self._transport.request(
            'PATCH', f'/proxies/{uuid}', body=data, out=Response[Proxy]
        )
        return unwrap(resp.data)

    async def delete(self, uuid: str) -> None:
        await self._transport.request('DELETE', f'/proxies/{uuid}')

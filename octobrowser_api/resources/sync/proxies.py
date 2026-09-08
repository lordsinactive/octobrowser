from __future__ import annotations

import builtins
from typing import Any, Literal, overload

from ...enums import ProxyType, SynMode, VPNProtocol
from ...models import (
    ListResponse,
    Proxy,
    ProxyCreate,
    ProxyUpdate,
    Response,
    VPNProxyCreate,
    VPNProxyUpdate,
)
from .._base import Resource, unwrap
from ..proxies import is_vpn


class Proxies(Resource):
    def list(self) -> builtins.list[Proxy]:
        return self._transport.request('GET', '/proxies', out=ListResponse[Proxy]).data

    @overload
    def create(self, data: ProxyCreate | VPNProxyCreate, /) -> Proxy: ...
    @overload
    def create(
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
    def create(
        self,
        *,
        type: Literal[ProxyType.VPN],
        title: str,
        conf: str,
        syn_mode: SynMode | None = None,
        vpn_protocol: VPNProtocol | None = None,
        external_id: str | None = None,
    ) -> Proxy: ...
    def create(
        self, data: ProxyCreate | VPNProxyCreate | None = None, **fields: Any
    ) -> Proxy:
        if data is None:
            data = VPNProxyCreate(**fields) if is_vpn(fields) else ProxyCreate(**fields)
        resp = self._transport.request(
            'POST', '/proxies', body=data, out=Response[Proxy]
        )
        return unwrap(resp.data)

    @overload
    def update(self, uuid: str, data: ProxyUpdate | VPNProxyUpdate, /) -> Proxy: ...
    @overload
    def update(
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
    def update(
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
    def update(
        self,
        uuid: str,
        data: ProxyUpdate | VPNProxyUpdate | None = None,
        **fields: Any,
    ) -> Proxy:
        if data is None:
            data = VPNProxyUpdate(**fields) if is_vpn(fields) else ProxyUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/proxies/{uuid}', body=data, out=Response[Proxy]
        )
        return unwrap(resp.data)

    def delete(self, uuid: str) -> None:
        self._transport.request('DELETE', f'/proxies/{uuid}')

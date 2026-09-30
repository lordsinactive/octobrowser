from __future__ import annotations

import builtins
from typing import Any, overload

from ...enums import ProxyKind
from ...models import (
    Location,
    ProviderProxy,
    ProviderProxyList,
    ProxyProvider,
    ProxyPurchase,
    Response,
)
from .._base import Resource, query, unwrap
from ..providers import locations_path


class Providers(Resource):
    def list(
        self, kind: ProxyKind | str = ProxyKind.RESIDENTIAL
    ) -> builtins.list[ProxyProvider]:
        resp = self._transport.request(
            'GET',
            '/v2/proxy_providers',
            params=query(kind=kind),
            out=Response[builtins.list[ProxyProvider]],
        )
        return unwrap(resp.data)

    def countries(
        self, provider_uuid: str, kind: ProxyKind | str = ProxyKind.RESIDENTIAL
    ) -> builtins.list[Location]:
        resp = self._transport.request(
            'GET',
            f'/v2/proxy_providers/{provider_uuid}/countries/{kind}',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    def isps(
        self, provider_uuid: str, kind: ProxyKind | str, country: str
    ) -> builtins.list[Location]:
        resp = self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country)}/isps',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    def regions(
        self,
        provider_uuid: str,
        kind: ProxyKind | str,
        country: str,
        *,
        isp: str | None = None,
    ) -> builtins.list[Location]:
        resp = self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country, isp)}/regions',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    def cities(
        self,
        provider_uuid: str,
        kind: ProxyKind | str,
        country: str,
        region: str,
        *,
        isp: str | None = None,
    ) -> builtins.list[Location]:
        resp = self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country, isp)}'
            f'/regions/{region}/cities',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    @overload
    def purchase(self, data: ProxyPurchase, /) -> builtins.list[ProviderProxy]: ...
    @overload
    def purchase(
        self,
        *,
        provider_uuid: str,
        kind: ProxyKind | str,
        country: str,
        region: str | None = None,
        city: str | None = None,
        isp: str | None = None,
        quantity: int = 1,
    ) -> builtins.list[ProviderProxy]: ...
    def purchase(
        self, data: ProxyPurchase | None = None, **fields: Any
    ) -> builtins.list[ProviderProxy]:
        body = data if data is not None else ProxyPurchase(**fields)
        resp = self._transport.request(
            'POST',
            '/v2/proxies/purchase',
            body=body,
            out=Response[builtins.list[ProviderProxy]],
        )
        return unwrap(resp.data)

    def proxies(self) -> builtins.list[ProviderProxy]:
        resp = self._transport.request(
            'GET', '/v2/proxies', out=Response[ProviderProxyList]
        )
        return unwrap(resp.data).items

    def delete(self, uuids: builtins.list[str]) -> None:
        self._transport.request('DELETE', '/v2/proxies', json={'uuids': uuids})

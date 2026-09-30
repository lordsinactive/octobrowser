from __future__ import annotations

import builtins
from typing import Any, overload

from ..enums import ProxyKind
from ..models import (
    Location,
    ProviderProxy,
    ProviderProxyList,
    ProxyProvider,
    ProxyPurchase,
    Response,
)
from ._base import AsyncResource, query, unwrap


def locations_path(
    provider_uuid: str, kind: ProxyKind | str, country: str, isp: str | None = None
) -> str:
    path = f'/v2/proxy_providers/{provider_uuid}/countries/{country}/{kind}'
    return f'{path}/isps/{isp}' if isp else path


class AsyncProviders(AsyncResource):
    async def list(
        self, kind: ProxyKind | str = ProxyKind.RESIDENTIAL
    ) -> builtins.list[ProxyProvider]:
        resp = await self._transport.request(
            'GET',
            '/v2/proxy_providers',
            params=query(kind=kind),
            out=Response[builtins.list[ProxyProvider]],
        )
        return unwrap(resp.data)

    async def countries(
        self, provider_uuid: str, kind: ProxyKind | str = ProxyKind.RESIDENTIAL
    ) -> builtins.list[Location]:
        resp = await self._transport.request(
            'GET',
            f'/v2/proxy_providers/{provider_uuid}/countries/{kind}',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    async def isps(
        self, provider_uuid: str, kind: ProxyKind | str, country: str
    ) -> builtins.list[Location]:
        resp = await self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country)}/isps',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    async def regions(
        self,
        provider_uuid: str,
        kind: ProxyKind | str,
        country: str,
        *,
        isp: str | None = None,
    ) -> builtins.list[Location]:
        resp = await self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country, isp)}/regions',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    async def cities(
        self,
        provider_uuid: str,
        kind: ProxyKind | str,
        country: str,
        region: str,
        *,
        isp: str | None = None,
    ) -> builtins.list[Location]:
        resp = await self._transport.request(
            'GET',
            f'{locations_path(provider_uuid, kind, country, isp)}'
            f'/regions/{region}/cities',
            out=Response[builtins.list[Location]],
        )
        return unwrap(resp.data)

    @overload
    async def purchase(
        self, data: ProxyPurchase, /
    ) -> builtins.list[ProviderProxy]: ...
    @overload
    async def purchase(
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
    async def purchase(
        self, data: ProxyPurchase | None = None, **fields: Any
    ) -> builtins.list[ProviderProxy]:
        body = data if data is not None else ProxyPurchase(**fields)
        resp = await self._transport.request(
            'POST',
            '/v2/proxies/purchase',
            body=body,
            out=Response[builtins.list[ProviderProxy]],
        )
        return unwrap(resp.data)

    async def proxies(self) -> builtins.list[ProviderProxy]:
        resp = await self._transport.request(
            'GET', '/v2/proxies', out=Response[ProviderProxyList]
        )
        return unwrap(resp.data).items

    async def delete(self, uuids: builtins.list[str]) -> None:
        await self._transport.request('DELETE', '/v2/proxies', json={'uuids': uuids})

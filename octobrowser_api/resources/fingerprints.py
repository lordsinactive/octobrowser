from __future__ import annotations

from ..models import DeviceModel, FingerprintOption, ListResponse
from ._base import AsyncResource, query


class AsyncFingerprints(AsyncResource):
    async def renderers(
        self,
        *,
        os: str = 'win',
        os_arch: str = 'x86',
        page_len: int | None = None,
        page: int | None = None,
    ) -> list[FingerprintOption]:
        params = query(os=os, os_arch=os_arch, page_len=page_len, page=page)
        resp = await self._transport.request(
            'GET',
            '/fingerprint/renderers',
            params=params,
            out=ListResponse[FingerprintOption],
        )
        return resp.data

    async def screens(
        self, *, os: str = 'win', os_arch: str = 'x86'
    ) -> list[FingerprintOption]:
        params = query(os=os, os_arch=os_arch)
        resp = await self._transport.request(
            'GET',
            '/fingerprint/screens',
            params=params,
            out=ListResponse[FingerprintOption],
        )
        return resp.data

    async def device_models(
        self, *, device_type: str | None = None
    ) -> list[DeviceModel]:
        params = query(device_type=device_type)
        resp = await self._transport.request(
            'GET',
            '/fingerprint/device_models',
            params=params,
            out=ListResponse[DeviceModel],
        )
        return resp.data

from __future__ import annotations
from typing import List, Optional

from ._base import AsyncResource, Resource, query
from ..models import DeviceModel, FingerprintOption, ListResponse


class Fingerprints(Resource):
    def renderers(
        self,
        *,
        os: str = 'win',
        os_arch: str = 'x86',
        page_len: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[FingerprintOption]:
        params = query(os=os, os_arch=os_arch, page_len=page_len, page=page)
        return self._transport.request(
            'GET',
            '/fingerprint/renderers',
            params=params,
            out=ListResponse[FingerprintOption],
        ).data

    def screens(
        self, *, os: str = 'win', os_arch: str = 'x86'
    ) -> List[FingerprintOption]:
        params = query(os=os, os_arch=os_arch)
        return self._transport.request(
            'GET',
            '/fingerprint/screens',
            params=params,
            out=ListResponse[FingerprintOption],
        ).data

    def device_models(self, *, device_type: Optional[str] = None) -> List[DeviceModel]:
        params = query(device_type=device_type)
        return self._transport.request(
            'GET',
            '/fingerprint/device_models',
            params=params,
            out=ListResponse[DeviceModel],
        ).data


class AsyncFingerprints(AsyncResource):
    async def renderers(
        self,
        *,
        os: str = 'win',
        os_arch: str = 'x86',
        page_len: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[FingerprintOption]:
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
    ) -> List[FingerprintOption]:
        params = query(os=os, os_arch=os_arch)
        resp = await self._transport.request(
            'GET',
            '/fingerprint/screens',
            params=params,
            out=ListResponse[FingerprintOption],
        )
        return resp.data

    async def device_models(
        self, *, device_type: Optional[str] = None
    ) -> List[DeviceModel]:
        params = query(device_type=device_type)
        resp = await self._transport.request(
            'GET',
            '/fingerprint/device_models',
            params=params,
            out=ListResponse[DeviceModel],
        )
        return resp.data

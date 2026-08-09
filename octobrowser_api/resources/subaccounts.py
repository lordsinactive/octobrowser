from __future__ import annotations

import builtins
from typing import Any, overload

from ..models import (
    ListResponse,
    Subaccount,
    SubaccountCreate,
    SubaccountDelete,
    SubaccountPermissions,
    SubaccountUpdate,
)
from ._base import AsyncResource


class AsyncSubaccounts(AsyncResource):
    async def list(self) -> builtins.list[Subaccount]:
        resp = await self._transport.request(
            'GET', '/teams/subaccounts', out=ListResponse[Subaccount]
        )
        return resp.data

    @overload
    async def create(self, data: SubaccountCreate, /) -> None: ...
    @overload
    async def create(
        self,
        *,
        email: str,
        permissions: SubaccountPermissions | dict[str, Any] | None = None,
    ) -> None: ...
    async def create(
        self, data: SubaccountCreate | None = None, **fields: Any
    ) -> None:
        body = data if data is not None else SubaccountCreate(**fields)
        await self._transport.request('POST', '/teams/subaccounts', body=body)

    @overload
    async def update(self, data: SubaccountUpdate, /) -> None: ...
    @overload
    async def update(
        self,
        *,
        email: str,
        permissions: SubaccountPermissions | dict[str, Any] | None = None,
    ) -> None: ...
    async def update(
        self, data: SubaccountUpdate | None = None, **fields: Any
    ) -> None:
        body = data if data is not None else SubaccountUpdate(**fields)
        await self._transport.request('PATCH', '/teams/subaccounts', body=body)

    async def delete(self, email: str) -> None:
        await self._transport.request(
            'DELETE', '/teams/subaccounts', body=SubaccountDelete(email=email)
        )

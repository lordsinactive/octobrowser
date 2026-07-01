from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, overload

from ._base import AsyncResource, Resource
from ..models import (
    ListResponse,
    Subaccount,
    SubaccountCreate,
    SubaccountDelete,
    SubaccountPermissions,
    SubaccountUpdate,
)


class Subaccounts(Resource):
    def list(self) -> List[Subaccount]:
        return self._transport.request(
            'GET', '/teams/subaccounts', out=ListResponse[Subaccount]
        ).data

    @overload
    def create(self, data: SubaccountCreate, /) -> None: ...
    @overload
    def create(
        self,
        *,
        email: str,
        permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None,
    ) -> None: ...
    def create(self, data: Optional[SubaccountCreate] = None, **fields: Any) -> None:
        body = data if data is not None else SubaccountCreate(**fields)
        self._transport.request('POST', '/teams/subaccounts', body=body)

    @overload
    def update(self, data: SubaccountUpdate, /) -> None: ...
    @overload
    def update(
        self,
        *,
        email: str,
        permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None,
    ) -> None: ...
    def update(self, data: Optional[SubaccountUpdate] = None, **fields: Any) -> None:
        body = data if data is not None else SubaccountUpdate(**fields)
        self._transport.request('PATCH', '/teams/subaccounts', body=body)

    def delete(self, email: str) -> None:
        self._transport.request(
            'DELETE', '/teams/subaccounts', body=SubaccountDelete(email=email)
        )


class AsyncSubaccounts(AsyncResource):
    async def list(self) -> List[Subaccount]:
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
        permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None,
    ) -> None: ...
    async def create(
        self, data: Optional[SubaccountCreate] = None, **fields: Any
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
        permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None,
    ) -> None: ...
    async def update(
        self, data: Optional[SubaccountUpdate] = None, **fields: Any
    ) -> None:
        body = data if data is not None else SubaccountUpdate(**fields)
        await self._transport.request('PATCH', '/teams/subaccounts', body=body)

    async def delete(self, email: str) -> None:
        await self._transport.request(
            'DELETE', '/teams/subaccounts', body=SubaccountDelete(email=email)
        )

from __future__ import annotations

import builtins
from typing import Any, overload

from ...models import (
    ListResponse,
    Subaccount,
    SubaccountCreate,
    SubaccountDelete,
    SubaccountPermissions,
    SubaccountUpdate,
)
from .._base import Resource


class Subaccounts(Resource):
    def list(self) -> builtins.list[Subaccount]:
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
        permissions: SubaccountPermissions | dict[str, Any] | None = None,
    ) -> None: ...
    def create(self, data: SubaccountCreate | None = None, **fields: Any) -> None:
        body = data if data is not None else SubaccountCreate(**fields)
        self._transport.request('POST', '/teams/subaccounts', body=body)

    @overload
    def update(self, data: SubaccountUpdate, /) -> None: ...
    @overload
    def update(
        self,
        *,
        email: str,
        permissions: SubaccountPermissions | dict[str, Any] | None = None,
    ) -> None: ...
    def update(self, data: SubaccountUpdate | None = None, **fields: Any) -> None:
        body = data if data is not None else SubaccountUpdate(**fields)
        self._transport.request('PATCH', '/teams/subaccounts', body=body)

    def delete(self, email: str) -> None:
        self._transport.request(
            'DELETE', '/teams/subaccounts', body=SubaccountDelete(email=email)
        )

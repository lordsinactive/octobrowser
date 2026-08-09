from __future__ import annotations

import builtins

from ..models import Invite, InviteDelete, ListResponse
from ._base import AsyncResource


class AsyncInvites(AsyncResource):
    async def list(self) -> builtins.list[Invite]:
        resp = await self._transport.request(
            'GET', '/teams/invites', out=ListResponse[Invite]
        )
        return resp.data

    async def delete(self, receiver: str) -> None:
        await self._transport.request(
            'DELETE', '/teams/invites', body=InviteDelete(receiver=receiver)
        )

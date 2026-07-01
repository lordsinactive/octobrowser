from __future__ import annotations
from typing import List

from ._base import AsyncResource, Resource
from ..models import Invite, InviteDelete, ListResponse


class Invites(Resource):
    def list(self) -> List[Invite]:
        return self._transport.request(
            'GET', '/teams/invites', out=ListResponse[Invite]
        ).data

    def delete(self, receiver: str) -> None:
        self._transport.request(
            'DELETE', '/teams/invites', body=InviteDelete(receiver=receiver)
        )


class AsyncInvites(AsyncResource):
    async def list(self) -> List[Invite]:
        resp = await self._transport.request(
            'GET', '/teams/invites', out=ListResponse[Invite]
        )
        return resp.data

    async def delete(self, receiver: str) -> None:
        await self._transport.request(
            'DELETE', '/teams/invites', body=InviteDelete(receiver=receiver)
        )

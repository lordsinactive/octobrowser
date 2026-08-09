from __future__ import annotations

import builtins

from ...models import Invite, InviteDelete, ListResponse
from .._base import Resource


class Invites(Resource):
    def list(self) -> builtins.list[Invite]:
        return self._transport.request(
            'GET', '/teams/invites', out=ListResponse[Invite]
        ).data

    def delete(self, receiver: str) -> None:
        self._transport.request(
            'DELETE', '/teams/invites', body=InviteDelete(receiver=receiver)
        )

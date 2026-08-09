from __future__ import annotations

from typing import Any, overload

from ...models import (
    ActiveProfiles,
    Browser,
    ClearPassword,
    ForceStopProfile,
    Login,
    Ok,
    SetPassword,
    StartOneTimeProfile,
    StartProfile,
    StopProfile,
    UpdateInfo,
    Username,
)
from .._base import Resource


class Local(Resource):
    def active(self) -> list[Browser]:
        return self._transport.request(
            'GET', '/profiles/active', out=ActiveProfiles
        ).root

    def version(self) -> UpdateInfo:
        return self._transport.request('GET', '/update', out=UpdateInfo)

    def update(self) -> str:
        return self._transport.request('POST', '/update', out=Ok).msg

    def username(self) -> str:
        return self._transport.request('GET', '/username', out=Username).username

    @overload
    def start(self, data: StartProfile, /) -> Browser: ...
    @overload
    def start(
        self,
        uuid: str,
        /,
        *,
        headless: bool = False,
        debug_port: bool = False,
        flags: list[str] | None = None,
        only_local: bool = True,
        timeout: int = 60,
        password: str | None = None,
    ) -> Browser: ...
    def start(
        self, data: StartProfile | str | None = None, **fields: Any
    ) -> Browser:
        if isinstance(data, StartProfile):
            body = data
        elif data is not None:
            body = StartProfile(uuid=data, **fields)
        else:
            body = StartProfile(**fields)
        return self._transport.request(
            'POST', '/profiles/start', body=body, out=Browser
        )

    @overload
    def start_one_time(self, data: StartOneTimeProfile, /) -> Browser: ...
    @overload
    def start_one_time(
        self,
        profile_data: dict[str, Any],
        /,
        *,
        headless: bool = True,
        debug_port: bool = True,
        flags: list[str] | None = None,
        timeout: int = 60,
    ) -> Browser: ...
    def start_one_time(
        self,
        data: StartOneTimeProfile | dict[str, Any] | None = None,
        **fields: Any,
    ) -> Browser:
        if isinstance(data, StartOneTimeProfile):
            body = data
        elif data is not None:
            body = StartOneTimeProfile(profile_data=data, **fields)
        else:
            body = StartOneTimeProfile(**fields)
        return self._transport.request(
            'POST', '/profiles/one_time/start', body=body, out=Browser
        )

    def stop(self, uuid: str) -> None:
        self._transport.request('POST', '/profiles/stop', body=StopProfile(uuid=uuid))

    def force_stop(self, uuid: str) -> None:
        self._transport.request(
            'POST', '/profiles/force_stop', body=ForceStopProfile(uuid=uuid)
        )

    def set_password(self, uuid: str, password: str) -> None:
        self._transport.request(
            'POST', '/profiles/password', body=SetPassword(uuid=uuid, password=password)
        )

    def clear_password(self, uuid: str, password: str) -> None:
        self._transport.request(
            'DELETE',
            '/profiles/password',
            body=ClearPassword(uuid=uuid, password=password),
        )

    def login(
        self, email: str, password: str, *, api_token: str | None = None
    ) -> None:
        self._transport.request(
            'POST',
            '/auth/login',
            body=Login(email=email, password=password, api_token=api_token),
        )

    def logout(self) -> None:
        self._transport.request('POST', '/auth/logout')

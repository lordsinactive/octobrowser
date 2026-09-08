from __future__ import annotations

from typing import Any, overload

from ..models import (
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
from ._base import AsyncResource


class AsyncLocal(AsyncResource):
    async def active(self) -> list[Browser]:
        resp = await self._transport.request(
            'GET', '/profiles/active', out=ActiveProfiles
        )
        return resp.root

    async def version(self) -> UpdateInfo:
        return await self._transport.request('GET', '/update', out=UpdateInfo)

    async def update(self) -> str:
        resp = await self._transport.request('POST', '/update', out=Ok)
        return resp.msg

    async def username(self) -> str:
        resp = await self._transport.request('GET', '/username', out=Username)
        return resp.username

    @overload
    async def start(self, data: StartProfile, /) -> Browser: ...
    @overload
    async def start(
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
        profile_data: dict[str, Any] | None = None,
    ) -> Browser: ...
    async def start(
        self, data: StartProfile | str | None = None, **fields: Any
    ) -> Browser:
        if isinstance(data, StartProfile):
            body = data
        elif data is not None:
            body = StartProfile(uuid=data, **fields)
        else:
            body = StartProfile(**fields)
        return await self._transport.request(
            'POST', '/profiles/start', body=body, out=Browser
        )

    @overload
    async def start_one_time(self, data: StartOneTimeProfile, /) -> Browser: ...
    @overload
    async def start_one_time(
        self,
        profile_data: dict[str, Any],
        /,
        *,
        headless: bool = True,
        debug_port: bool = True,
        flags: list[str] | None = None,
        timeout: int = 60,
    ) -> Browser: ...
    async def start_one_time(
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
        return await self._transport.request(
            'POST', '/profiles/one_time/start', body=body, out=Browser
        )

    async def stop(self, uuid: str) -> None:
        await self._transport.request(
            'POST', '/profiles/stop', body=StopProfile(uuid=uuid)
        )

    async def force_stop(self, uuid: str) -> None:
        await self._transport.request(
            'POST', '/profiles/force_stop', body=ForceStopProfile(uuid=uuid)
        )

    async def set_password(self, uuid: str, password: str) -> None:
        await self._transport.request(
            'POST', '/profiles/password', body=SetPassword(uuid=uuid, password=password)
        )

    async def clear_password(self, uuid: str, password: str) -> None:
        await self._transport.request(
            'DELETE',
            '/profiles/password',
            body=ClearPassword(uuid=uuid, password=password),
        )

    async def login(
        self, email: str, password: str, *, api_token: str | None = None
    ) -> None:
        await self._transport.request(
            'POST',
            '/auth/login',
            body=Login(email=email, password=password, api_token=api_token),
        )

    async def logout(self) -> None:
        await self._transport.request('POST', '/auth/logout')

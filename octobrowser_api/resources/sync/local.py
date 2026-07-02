from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, overload

from .._base import Resource
from ...models import (
    ActiveProfiles,
    Browser,
    ClearPassword,
    ForceStopProfile,
    Login,
    SetPassword,
    StartOneTimeProfile,
    StartProfile,
    StopProfile,
    UpdateInfo,
    Username,
)


class Local(Resource):
    def active(self) -> List[Browser]:
        return self._transport.request(
            'GET', '/profiles/active', out=ActiveProfiles
        ).root

    def version(self) -> UpdateInfo:
        return self._transport.request('GET', '/update', out=UpdateInfo)

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
        flags: Optional[List[str]] = None,
        only_local: bool = True,
        timeout: int = 60,
        password: Optional[str] = None,
    ) -> Browser: ...
    def start(
        self, data: Union[StartProfile, str, None] = None, **fields: Any
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
        profile_data: Dict[str, Any],
        /,
        *,
        headless: bool = True,
        debug_port: bool = True,
        flags: Optional[List[str]] = None,
        timeout: int = 60,
    ) -> Browser: ...
    def start_one_time(
        self,
        data: Union[StartOneTimeProfile, Dict[str, Any], None] = None,
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

    def login(self, email: str, password: str) -> None:
        self._transport.request(
            'POST', '/auth/login', body=Login(email=email, password=password)
        )

    def logout(self) -> None:
        self._transport.request('POST', '/auth/logout')
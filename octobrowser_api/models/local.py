from __future__ import annotations

from typing import Any, Union

from pydantic import Field, RootModel

from ._base import OctoModel

__all__ = [
    'StartProfile',
    'StartOneTimeProfile',
    'StopProfile',
    'ForceStopProfile',
    'Login',
    'SetPassword',
    'ClearPassword',
    'BrowserConnectionData',
    'Browser',
    'Ok',
    'Error',
    'UpdateInfo',
    'Username',
    'StartProfileResult',
    'LocalResult',
    'ActiveProfiles',
]


class StartProfile(OctoModel):
    uuid: str
    headless: bool = False
    debug_port: int | bool = False
    flags: list[str] = Field(default_factory=list)
    only_local: bool = True
    timeout: int = Field(default=60, ge=0)
    password: str | None = None
    profile_data: dict[str, Any] | None = None


class StartOneTimeProfile(OctoModel):
    profile_data: dict[str, Any]
    headless: bool = True
    debug_port: bool = True
    flags: list[str] = Field(default_factory=list)
    timeout: int = Field(default=60, ge=0)


class StopProfile(OctoModel):
    uuid: str


class ForceStopProfile(OctoModel):
    uuid: str


class Login(OctoModel):
    email: str
    password: str
    api_token: str | None = None


class SetPassword(OctoModel):
    uuid: str
    password: str


class ClearPassword(OctoModel):
    uuid: str
    password: str


class BrowserConnectionData(OctoModel):
    ip: str | None = None
    country: str | None = None
    supports_udp: bool | None = None


class Browser(OctoModel):
    uuid: str
    state: str
    headless: bool | None = None
    start_time: int | None = None
    ws_endpoint: str | None = None
    debug_port: str | None = None
    one_time: bool = False
    browser_pid: int | None = None
    connection_data: BrowserConnectionData | None = None


class Ok(OctoModel):
    msg: str
    data: Any = None


class Error(OctoModel):
    code: str | None = None
    error: str
    error_code: int = -1


class UpdateInfo(OctoModel):
    current: str
    latest: str
    update_required: bool


class Username(OctoModel):
    username: str


class StartProfileResult(RootModel[Union[Browser, Error]]):
    pass


class LocalResult(RootModel[Union[Ok, Error]]):
    pass


class ActiveProfiles(RootModel[list[Browser]]):
    pass

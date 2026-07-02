from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

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
    debug_port: Union[int, bool] = False
    flags: List[str] = Field(default_factory=list)
    only_local: bool = True
    timeout: int = Field(default=60, ge=0)
    password: Optional[str] = None


class StartOneTimeProfile(OctoModel):
    profile_data: Dict[str, Any]
    headless: bool = True
    debug_port: bool = True
    flags: List[str] = Field(default_factory=list)
    timeout: int = Field(default=60, ge=0)


class StopProfile(OctoModel):
    uuid: str


class ForceStopProfile(OctoModel):
    uuid: str


class Login(OctoModel):
    email: str
    password: str


class SetPassword(OctoModel):
    uuid: str
    password: str


class ClearPassword(OctoModel):
    uuid: str
    password: str


class Browser(OctoModel):
    uuid: str
    state: str
    headless: Optional[bool] = None
    start_time: Optional[int] = None
    ws_endpoint: Optional[str] = None
    debug_port: Optional[str] = None
    one_time: bool = False
    browser_pid: Optional[int] = None
    connection_data: Optional[Dict[str, Any]] = None


class Ok(OctoModel):
    msg: str
    data: Any = None


class Error(OctoModel):
    code: Optional[str] = None
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


class ActiveProfiles(RootModel[List[Browser]]):
    pass

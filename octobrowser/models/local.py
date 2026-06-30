from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field, RootModel
from ._base import OctoModel

__all__ = [
    "StartRequest",
    "StartOneTimeProfileIn",
    "StopRequest",
    "ForceStopRequest",
    "LoginIn",
    "SetPasswordIn",
    "ClearPasswordIn",
    "BrowserJson",
    "OkOut",
    "ErrorOut",
    "UpdatesJson",
    "StartProfileOut",
    "ResponseOut",
    "ActiveProfilesOut",
    "GetUpdatesOut",
]


class StartRequest(OctoModel):
    uuid: str
    headless: bool = False
    debug_port: Union[int, bool] = False
    flags: List[str] = Field(default_factory=list)
    only_local: bool = True
    timeout: int = 60
    password: Optional[str] = None


class StartOneTimeProfileIn(OctoModel):
    profile_data: Dict[str, Any]
    headless: bool = True
    debug_port: bool = True
    flags: List[str] = Field(default_factory=list)
    timeout: int = 60


class StopRequest(OctoModel):
    uuid: str


class ForceStopRequest(OctoModel):
    uuid: str


class LoginIn(OctoModel):
    email: str
    password: str


class SetPasswordIn(OctoModel):
    uuid: str
    password: str


class ClearPasswordIn(OctoModel):
    uuid: str
    password: str


class BrowserJson(OctoModel):
    uuid: str
    state: str
    headless: Optional[bool] = None
    start_time: Optional[int] = None
    ws_endpoint: Optional[str] = None
    debug_port: Optional[str] = None
    one_time: bool = False
    browser_pid: Optional[int] = None
    connection_data: Optional[Dict[str, Any]] = None


class OkOut(OctoModel):
    msg: str
    data: Any = None


class ErrorOut(OctoModel):
    code: str
    error: str
    error_code: int = -1


class UpdatesJson(OctoModel):
    current: str
    latest: str
    update_required: bool


class StartProfileOut(RootModel[Union[BrowserJson, ErrorOut]]):
    pass


class ResponseOut(RootModel[Union[OkOut, ErrorOut]]):
    pass


class ActiveProfilesOut(RootModel[List[BrowserJson]]):
    pass


GetUpdatesOut = UpdatesJson

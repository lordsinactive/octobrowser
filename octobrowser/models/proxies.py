from __future__ import annotations
from typing import List, Optional

from pydantic import Field
from ..enums import ProxyType
from ._base import OctoModel

__all__ = [
    "ProxyUUID",
    "ProxyDataInExtraIgnore",
    "ProxyCreateRequest",
    "ProxyUpdate",
    "PermanentProxyOut",
    "ProxyResponse",
    "ProxiesResponse",
]


class ProxyUUID(OctoModel):
    uuid: str


class ProxyDataInExtraIgnore(OctoModel):
    type: ProxyType
    host: str
    port: int
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None


class ProxyCreateRequest(OctoModel):
    type: ProxyType
    host: str
    port: int
    title: str
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    external_id: Optional[str] = None


class ProxyUpdate(OctoModel):
    type: Optional[ProxyType] = None
    host: Optional[str] = None
    port: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    title: Optional[str] = None
    external_id: Optional[str] = None


class PermanentProxyOut(OctoModel):
    uuid: str
    type: ProxyType
    host: str
    port: int
    profiles_count: int
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    external_id: Optional[str] = None
    title: Optional[str] = None


class ProxyResponse(OctoModel):
    success: bool = True
    msg: str = ""
    code: str = ""
    data: Optional[PermanentProxyOut] = None


class ProxiesResponse(OctoModel):
    success: bool = True
    msg: str = ""
    code: str = ""
    data: List[PermanentProxyOut] = Field(default_factory=list)

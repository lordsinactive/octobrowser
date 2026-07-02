from __future__ import annotations
from typing import Optional

from pydantic import Field
from ..enums import ProxyType
from ._base import OctoModel

__all__ = [
    'ProxyRef',
    'ProxyData',
    'ProxyCreate',
    'ProxyUpdate',
    'Proxy',
]


class ProxyRef(OctoModel):
    uuid: str


class ProxyData(OctoModel):
    type: ProxyType
    host: str
    port: int = Field(ge=1, le=65535)
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None


class ProxyCreate(OctoModel):
    type: ProxyType
    host: str
    port: int = Field(ge=1, le=65535)
    title: str
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    external_id: Optional[str] = None


class ProxyUpdate(OctoModel):
    type: Optional[ProxyType] = None
    host: Optional[str] = None
    port: Optional[int] = Field(default=None, ge=1, le=65535)
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    title: Optional[str] = None
    external_id: Optional[str] = None


class Proxy(OctoModel):
    uuid: str
    type: ProxyType
    host: str
    port: int
    profiles_count: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    external_id: Optional[str] = None
    title: Optional[str] = None

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ..enums import ProxyType, SynMode, VPNProtocol
from ._base import OctoModel

__all__ = [
    'ProxyRef',
    'ProxyData',
    'ProxyCreate',
    'ProxyUpdate',
    'VPNProxyCreate',
    'VPNProxyUpdate',
    'Proxy',
]


class ProxyRef(OctoModel):
    uuid: str


class ProxyData(OctoModel):
    type: ProxyType
    host: str
    port: int = Field(ge=0, le=65535)
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None


class ProxyCreate(OctoModel):
    type: ProxyType
    host: str
    port: int = Field(ge=0, le=65535)
    title: str
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None
    external_id: str | None = None


class ProxyUpdate(OctoModel):
    type: ProxyType | None = None
    host: str | None = None
    port: int | None = Field(default=None, ge=0, le=65535)
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None
    title: str | None = None
    external_id: str | None = None


class VPNProxyCreate(OctoModel):
    title: str
    conf: str
    type: Literal[ProxyType.VPN] = ProxyType.VPN
    syn_mode: SynMode | None = None
    vpn_protocol: VPNProtocol | None = None
    external_id: str | None = None


class VPNProxyUpdate(OctoModel):
    type: Literal[ProxyType.VPN] | None = None
    title: str | None = None
    conf: str | None = None
    syn_mode: SynMode | None = None
    vpn_protocol: VPNProtocol | None = None
    external_id: str | None = None


class Proxy(OctoModel):
    uuid: str
    type: ProxyType
    host: str
    port: int
    profiles_count: int | None = None
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None
    external_id: str | None = None
    title: str | None = None
    syn_mode: SynMode | None = None
    vpn_protocol: VPNProtocol | None = None

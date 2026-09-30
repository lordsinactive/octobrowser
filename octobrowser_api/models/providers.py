from __future__ import annotations

from typing import Annotated

from pydantic import Field

from ..enums import ProviderFeature, ProxyKind, ProxyType
from ._base import OctoModel

__all__ = [
    'ProxyProvider',
    'Location',
    'ProxyPurchase',
    'ProviderProxyMeta',
    'ProviderProxy',
    'ProviderProxyList',
]

Feature = Annotated[ProviderFeature | str, Field(union_mode='left_to_right')]


class ProxyProvider(OctoModel):
    uuid: str
    name: str
    vendor: str
    subaccount_id: str | None = None
    is_disabled: bool = False
    create_proxy: bool = False
    buy_traffic: bool = False
    team_traffic: int | None = None
    proxy_count: int = 0
    features_by_kind: dict[ProxyKind, list[Feature]] = Field(default_factory=dict)
    banner_text: dict[str, str] = Field(default_factory=dict)


class Location(OctoModel):
    code: str
    name: str


class ProxyPurchase(OctoModel):
    provider_uuid: str
    kind: ProxyKind
    country: str
    region: str | None = None
    city: str | None = None
    isp: str | None = None
    quantity: int = Field(default=1, ge=1)


class ProviderProxyMeta(OctoModel):
    country_code: str | None = None
    region_code: str | None = None
    city_code: str | None = None
    isp: str | None = None
    os: str | None = None
    sid: str | None = None
    username: str | None = None


class ProviderProxy(OctoModel):
    uuid: str
    title: str | None = None
    type: ProxyType
    kind: ProxyKind | None = None
    ip: str
    port: int
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None
    provider_uuid: str | None = None
    profiles_count: int = 0
    country: str | None = None
    external_ip: str | None = None
    meta: ProviderProxyMeta | None = None


class ProviderProxyList(OctoModel):
    total: int = 0
    items: list[ProviderProxy] = Field(default_factory=list)

from __future__ import annotations

from enum import StrEnum

__all__ = ['ProxyType', 'SynMode', 'VPNProtocol', 'ProxyKind', 'ProviderFeature']


class ProxyType(StrEnum):
    SSH = 'ssh'
    HTTP = 'http'
    HTTPS = 'https'
    SOCKS = 'socks'
    SOCKS5 = 'socks5'
    VPN = 'vpn'


class SynMode(StrEnum):
    PROFILE_BASED = 'profile_based'
    WIN = 'win'
    MAC = 'mac'
    ANDROID = 'android'
    REAL = 'real'


class VPNProtocol(StrEnum):
    WIREGUARD = 'wireguard'


class ProxyKind(StrEnum):
    RESIDENTIAL = 'residential'
    MOBILE = 'mobile'
    DATA_CENTER = 'data_center'


class ProviderFeature(StrEnum):
    HAS_REGIONS = 'has_regions'
    HAS_CITIES = 'has_cities'
    HAS_ISP = 'has_isp'
    HAS_OS = 'has_os'
    IP_CHANGING = 'ip_changing'
    SUPPORTS_UDP = 'supports_udp'

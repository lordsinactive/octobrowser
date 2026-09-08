from __future__ import annotations

from enum import StrEnum

__all__ = ['ProxyType', 'SynMode', 'VPNProtocol']


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

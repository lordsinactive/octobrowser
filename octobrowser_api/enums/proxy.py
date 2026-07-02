from __future__ import annotations
from enum import StrEnum

__all__ = ['ProxyType']


class ProxyType(StrEnum):
    SSH = 'ssh'
    HTTP = 'http'
    HTTPS = 'https'
    SOCKS = 'socks'
    SOCKS5 = 'socks5'

from __future__ import annotations
from enum import IntEnum, StrEnum

__all__ = [
    "OSTypeIn",
    "PlatformsBaseSpec",
    "DeviceType",
    "MacOSArchType",
    "IPBasedType",
    "IPBasedNoManualType",
    "CPUVariant",
    "RAMVariant",
    "WindowsVersion",
    "MacOSVersion",
    "AndroidVersion",
]


class OSTypeIn(StrEnum):
    WIN = "win"
    MAC = "mac"
    ANDROID = "android"


class PlatformsBaseSpec(StrEnum):
    WIN = "win"
    MAC = "mac"
    LIN = "lin"


class DeviceType(StrEnum):
    PHONE = "phone"
    TABLET = "tablet"


class MacOSArchType(StrEnum):
    X86 = "x86"
    ARM = "arm"


class IPBasedType(StrEnum):
    IP = "ip"
    REAL = "real"
    MANUAL = "manual"


class IPBasedNoManualType(StrEnum):
    IP = "ip"
    REAL = "real"
    DISABLE_NON_PROXIED_UDP = "disable_non_proxied_udp"


class CPUVariant(IntEnum):
    CORES_2 = 2
    CORES_4 = 4
    CORES_6 = 6
    CORES_8 = 8
    CORES_10 = 10
    CORES_11 = 11
    CORES_12 = 12
    CORES_14 = 14
    CORES_16 = 16
    CORES_20 = 20
    CORES_24 = 24


class RAMVariant(IntEnum):
    GB_2 = 2
    GB_4 = 4
    GB_8 = 8
    GB_12 = 12
    GB_16 = 16
    GB_24 = 24
    GB_32 = 32
    GB_64 = 64


class WindowsVersion(StrEnum):
    V10 = "10"
    V11 = "11"


class MacOSVersion(StrEnum):
    V12 = "12"
    V13 = "13"
    V14 = "14"
    V15 = "15"
    V26 = "26"


class AndroidVersion(StrEnum):
    V12 = "12"
    V13 = "13"
    V14 = "14"
    V15 = "15"

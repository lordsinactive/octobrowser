from __future__ import annotations

from typing import Any

from pydantic import Field

from ..enums import (
    OS,
    AndroidVersion,
    Arch,
    CPUCores,
    DeviceType,
    IPMode,
    MacOSVersion,
    Platform,
    RAMSize,
    WebRTCMode,
    WindowsVersion,
)
from ._base import OctoModel

__all__ = [
    'GeoCoordinates',
    'Geolocation',
    'Languages',
    'Timezone',
    'WebRTC',
    'Noise',
    'MediaDevices',
    'Fingerprint',
    'FingerprintUpdate',
    'FingerprintOption',
    'DeviceModel',
]


class GeoCoordinates(OctoModel):
    latitude: float
    longitude: float
    accuracy: int = Field(ge=0)


class Geolocation(OctoModel):
    type: IPMode
    data: GeoCoordinates | dict[str, Any] | None = None


class Languages(OctoModel):
    type: IPMode
    data: list[str] | None = None


class Timezone(OctoModel):
    type: IPMode
    data: str | None = None


class WebRTC(OctoModel):
    type: WebRTCMode
    data: str | None = None


class Noise(OctoModel):
    webgl: bool = False
    canvas: bool = False
    audio: bool = False
    client_rects: bool = False


class MediaDevices(OctoModel):
    video_in: int
    audio_in: int
    audio_out: int


class Fingerprint(OctoModel):
    os: OS
    os_version: WindowsVersion | MacOSVersion | AndroidVersion | str | None = (
        None
    )
    os_arch: Arch | str | None = None
    user_agent: str | None = None
    screen: str | None = None
    renderer: str | None = None
    languages: Languages | dict[str, Any] | None = None
    timezone: Timezone | dict[str, Any] | None = None
    geolocation: Geolocation | dict[str, Any] | None = None
    cpu: CPUCores | None = None
    ram: RAMSize | None = None
    noise: Noise | dict[str, Any] | None = None
    webrtc: WebRTC | dict[str, Any] | None = None
    dns: str | None = None
    fonts: list[str] | None = None
    media_devices: MediaDevices | dict[str, Any] | None = None
    device_model: str | None = None
    device_type: DeviceType | None = None


class FingerprintUpdate(OctoModel):
    os: OS | None = None
    os_version: WindowsVersion | MacOSVersion | AndroidVersion | str | None = (
        None
    )
    os_arch: Arch | str | None = None
    user_agent: str | None = None
    screen: str | None = None
    renderer: str | None = None
    languages: Languages | dict[str, Any] | None = None
    timezone: Timezone | dict[str, Any] | None = None
    geolocation: Geolocation | dict[str, Any] | None = None
    cpu: CPUCores | None = None
    ram: RAMSize | None = None
    noise: Noise | dict[str, Any] | None = None
    webrtc: WebRTC | dict[str, Any] | None = None
    dns: str | None = None
    fonts: list[str] | None = None
    media_devices: MediaDevices | dict[str, Any] | None = None
    device_model: str | None = None
    device_type: DeviceType | None = None


class FingerprintOption(OctoModel):
    value: str
    platform: Platform
    archs: list[Arch]


class DeviceModel(OctoModel):
    value: str
    os: OS
    os_versions: list[str] = Field(default_factory=list)
    archs: list[Arch] = Field(default_factory=list)
    device_type: DeviceType | None = None

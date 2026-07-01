from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ..enums import (
    OS,
    Arch,
    CPUCores,
    DeviceType,
    IPMode,
    Platform,
    RAMSize,
    WebRTCMode,
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
    data: Optional[Union[GeoCoordinates, Dict[str, Any]]] = None


class Languages(OctoModel):
    type: IPMode
    data: Optional[List[str]] = None


class Timezone(OctoModel):
    type: IPMode
    data: Optional[str] = None


class WebRTC(OctoModel):
    type: WebRTCMode
    data: Optional[str] = None


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
    os_version: Optional[str] = None
    os_arch: Optional[str] = None
    user_agent: Optional[str] = None
    screen: Optional[str] = None
    renderer: Optional[str] = None
    languages: Optional[Union[Languages, Dict[str, Any]]] = None
    timezone: Optional[Union[Timezone, Dict[str, Any]]] = None
    geolocation: Optional[Union[Geolocation, Dict[str, Any]]] = None
    cpu: Optional[CPUCores] = None
    ram: Optional[RAMSize] = None
    noise: Optional[Union[Noise, Dict[str, Any]]] = None
    webrtc: Optional[Union[WebRTC, Dict[str, Any]]] = None
    dns: Optional[str] = None
    fonts: Optional[List[str]] = None
    media_devices: Optional[Union[MediaDevices, Dict[str, Any]]] = None
    device_model: Optional[str] = None
    device_type: Optional[DeviceType] = None


class FingerprintUpdate(OctoModel):
    os: Optional[OS] = None
    os_version: Optional[str] = None
    os_arch: Optional[str] = None
    user_agent: Optional[str] = None
    screen: Optional[str] = None
    renderer: Optional[str] = None
    languages: Optional[Union[Languages, Dict[str, Any]]] = None
    timezone: Optional[Union[Timezone, Dict[str, Any]]] = None
    geolocation: Optional[Union[Geolocation, Dict[str, Any]]] = None
    cpu: Optional[CPUCores] = None
    ram: Optional[RAMSize] = None
    noise: Optional[Union[Noise, Dict[str, Any]]] = None
    webrtc: Optional[Union[WebRTC, Dict[str, Any]]] = None
    dns: Optional[str] = None
    fonts: Optional[List[str]] = None
    media_devices: Optional[Union[MediaDevices, Dict[str, Any]]] = None
    device_model: Optional[str] = None
    device_type: Optional[DeviceType] = None


class FingerprintOption(OctoModel):
    value: str
    platform: Platform
    archs: List[Arch]


class DeviceModel(OctoModel):
    value: str
    os: OS
    os_versions: List[str] = Field(default_factory=list)
    archs: List[Arch] = Field(default_factory=list)
    device_type: Optional[DeviceType] = None

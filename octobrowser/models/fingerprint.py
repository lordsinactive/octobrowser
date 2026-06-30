from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ..enums import (
    CPUVariant,
    DeviceType,
    IPBasedNoManualType,
    IPBasedType,
    MacOSArchType,
    OSTypeIn,
    PlatformsBaseSpec,
    RAMVariant,
)
from ._base import OctoModel

__all__ = [
    "GeoData",
    "GeolocationIn",
    "LanguagesIn",
    "TimezoneIn",
    "WebRTCIn",
    "NoiseType",
    "MediaDevicesType",
    "FingerprintDataInBaseSpec",
    "FingerprintUpdateIn",
    "FingerprintDataOutBaseSpec",
    "DeviceModelOut",
    "RenderersRespBaseSpec",
    "ScreensRespBaseSpec",
    "DeviceModelsResponse",
]


class GeoData(OctoModel):
    latitude: float
    longitude: float
    accuracy: int


class GeolocationIn(OctoModel):
    type: IPBasedType
    data: Optional[Union[GeoData, Dict[str, Any]]] = None


class LanguagesIn(OctoModel):
    type: IPBasedType
    data: Optional[List[str]] = None


class TimezoneIn(OctoModel):
    type: IPBasedType
    data: Optional[str] = None


class WebRTCIn(OctoModel):
    type: IPBasedNoManualType
    data: Optional[str] = None


class NoiseType(OctoModel):
    webgl: bool = False
    canvas: bool = False
    audio: bool = False
    client_rects: bool = False


class MediaDevicesType(OctoModel):
    video_in: int
    audio_in: int
    audio_out: int


class FingerprintDataInBaseSpec(OctoModel):
    os: OSTypeIn
    os_version: Optional[str] = None
    os_arch: Optional[str] = None
    user_agent: Optional[str] = None
    screen: Optional[str] = None
    renderer: Optional[str] = None
    languages: Optional[Union[LanguagesIn, Dict[str, Any]]] = None
    timezone: Optional[Union[TimezoneIn, Dict[str, Any]]] = None
    geolocation: Optional[Union[GeolocationIn, Dict[str, Any]]] = None
    cpu: Optional[CPUVariant] = None
    ram: Optional[RAMVariant] = None
    noise: Optional[Union[NoiseType, Dict[str, Any]]] = None
    webrtc: Optional[Union[WebRTCIn, Dict[str, Any]]] = None
    dns: Optional[str] = None
    fonts: Optional[List[str]] = None
    media_devices: Optional[Union[MediaDevicesType, Dict[str, Any]]] = None
    device_model: Optional[str] = None
    device_type: Optional[DeviceType] = None


class FingerprintUpdateIn(OctoModel):
    os: Optional[OSTypeIn] = None
    os_version: Optional[str] = None
    os_arch: Optional[str] = None
    user_agent: Optional[str] = None
    screen: Optional[str] = None
    renderer: Optional[str] = None
    languages: Optional[Union[LanguagesIn, Dict[str, Any]]] = None
    timezone: Optional[Union[TimezoneIn, Dict[str, Any]]] = None
    geolocation: Optional[Union[GeolocationIn, Dict[str, Any]]] = None
    cpu: Optional[CPUVariant] = None
    ram: Optional[RAMVariant] = None
    noise: Optional[Union[NoiseType, Dict[str, Any]]] = None
    webrtc: Optional[Union[WebRTCIn, Dict[str, Any]]] = None
    dns: Optional[str] = None
    fonts: Optional[List[str]] = None
    media_devices: Optional[Union[MediaDevicesType, Dict[str, Any]]] = None
    device_model: Optional[str] = None
    device_type: Optional[DeviceType] = None


class FingerprintDataOutBaseSpec(OctoModel):
    value: str
    platform: PlatformsBaseSpec
    archs: List[MacOSArchType]


class DeviceModelOut(OctoModel):
    value: str
    os: OSTypeIn
    os_versions: List[str] = Field(default_factory=list)
    archs: List[MacOSArchType] = Field(default_factory=list)
    device_type: Optional[DeviceType] = None


class RenderersRespBaseSpec(OctoModel):
    success: bool = True
    msg: str = ""
    data: List[FingerprintDataOutBaseSpec] = Field(default_factory=list)
    total_count: int = 0
    page: int = 0


class ScreensRespBaseSpec(OctoModel):
    success: bool = True
    msg: str = ""
    data: List[FingerprintDataOutBaseSpec] = Field(default_factory=list)


class DeviceModelsResponse(OctoModel):
    success: bool = True
    msg: str = ""
    data: List[DeviceModelOut] = Field(default_factory=list)

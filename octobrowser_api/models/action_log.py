from __future__ import annotations

from pydantic import Field

from ..enums import ActionType
from ._base import OctoModel

__all__ = [
    'ConnectionData',
    'ActionLogData',
    'ActionLogEntry',
    'ActionLogWatermark',
    'ActionLogPage',
]


class ConnectionData(OctoModel):
    ip: str | None = None
    country_code: str | None = Field(default=None, alias='countryCode')
    country_name: str | None = Field(default=None, alias='countryName')
    subdivisions: list[str] | None = None
    postal_code: str | None = Field(default=None, alias='postalCode')
    city_name: str | None = Field(default=None, alias='cityName')
    timezone: str | None = None
    lat: float | None = None
    lon: float | None = None
    languages: list[str] | None = None
    isp: str | None = None
    connection_type: str | None = Field(default=None, alias='connectionType')


class ActionLogData(OctoModel):
    connection_data: ConnectionData | None = None


class ActionLogEntry(OctoModel):
    uuid: str
    action: ActionType | str = Field(union_mode='left_to_right')
    time: int
    user_email: str | None = None
    object_type: str | None = None
    object_id: str | None = None
    object_title: str | None = None
    data: ActionLogData | None = None


class ActionLogWatermark(OctoModel):
    uuid: str
    time: int


class ActionLogPage(OctoModel):
    items: list[ActionLogEntry] = Field(default_factory=list)
    watermark: ActionLogWatermark | None = None

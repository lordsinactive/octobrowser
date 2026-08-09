from __future__ import annotations

from pydantic import Field

from ._base import OctoModel

__all__ = [
    'ActionLogEntry',
    'ActionLogWatermark',
    'ActionLogPage',
]


class ActionLogEntry(OctoModel):
    uuid: str
    action: str
    time: int
    user_email: str | None = None
    object_type: str | None = None
    object_id: str | None = None
    object_title: str | None = None


class ActionLogWatermark(OctoModel):
    uuid: str
    time: int


class ActionLogPage(OctoModel):
    items: list[ActionLogEntry] = Field(default_factory=list)
    watermark: ActionLogWatermark | None = None

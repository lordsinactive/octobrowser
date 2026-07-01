from __future__ import annotations
from typing import List, Optional

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
    user_email: Optional[str] = None
    object_type: Optional[str] = None
    object_id: Optional[str] = None
    object_title: Optional[str] = None


class ActionLogWatermark(OctoModel):
    uuid: str
    time: int


class ActionLogPage(OctoModel):
    items: List[ActionLogEntry] = Field(default_factory=list)
    watermark: Optional[ActionLogWatermark] = None

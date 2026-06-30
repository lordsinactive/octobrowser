from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class OctoModel(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
    )

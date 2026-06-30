from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ._base import OctoModel
from .fingerprint import FingerprintDataInBaseSpec, FingerprintUpdateIn
from .proxies import ProxyDataInExtraIgnore, ProxyUUID

__all__ = [
    "Bookmark",
    "StorageOptions",
    "CookiesRequest",
    "ProfileCreateRequestAutomation",
    "ProfileUpdateRequest",
    "ProfilesResp",
    "ProfileCreatedResp",
    "DeleteProfileRequest",
    "ProfileForceStopRequest",
    "SetProfilePasswordRequestAutomation",
    "ClearProfilePasswordRequestAutomation",
    "TransferProfilesRequest",
    "ExportProfilesData",
    "ImportDataV1",
    "ImportDataV2",
    "ImportFileV1",
    "ImportFileV2",
    "ImportProfilesRequest",
]


class Bookmark(OctoModel):
    name: str
    url: str


class StorageOptions(OctoModel):
    cookies: bool = True
    passwords: bool = True
    extensions: bool = False
    localstorage: bool = False
    history: bool = False
    bookmarks: bool = True
    serviceworkers: bool = False


class CookiesRequest(OctoModel):
    cookies: List[Dict[str, Any]]


class ProfileCreateRequestAutomation(OctoModel):
    title: str
    fingerprint: Union[FingerprintDataInBaseSpec, Dict[str, Any]]
    description: Optional[str] = None
    start_pages: Optional[List[str]] = None
    bookmarks: Optional[List[Union[Bookmark, Dict[str, Any]]]] = None
    tags: Optional[List[str]] = None
    pinned_tag: Optional[str] = None
    password: Optional[str] = None
    proxy: Optional[Union[ProxyDataInExtraIgnore, ProxyUUID, Dict[str, Any]]] = None
    storage_options: Optional[Union[StorageOptions, Dict[str, Any]]] = None
    cookies: Optional[List[Dict[str, Any]]] = None
    image: Optional[str] = None
    extensions: Optional[List[str]] = None
    launch_args: Optional[List[str]] = None
    images_load_limit: Optional[int] = None
    local_cache: Optional[bool] = None


class ProfileUpdateRequest(OctoModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_pages: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    pinned_tag: Optional[str] = None
    bookmarks: Optional[List[Union[Bookmark, Dict[str, Any]]]] = None
    proxy: Optional[Union[ProxyDataInExtraIgnore, ProxyUUID, Dict[str, Any]]] = None
    storage_options: Optional[Union[StorageOptions, Dict[str, Any]]] = None
    cookies: Optional[List[Dict[str, Any]]] = None
    image: Optional[str] = None
    fingerprint: Optional[Union[FingerprintUpdateIn, Dict[str, Any]]] = None
    extensions: Optional[List[str]] = None
    launch_args: Optional[List[str]] = None
    images_load_limit: Optional[int] = None
    local_cache: Optional[bool] = None


class ProfilesResp(OctoModel):
    success: bool = True
    msg: str = ""
    data: List[Dict[str, Any]] = Field(default_factory=list)
    total_count: int = 0
    page: int = 0
    code: str = ""


class ProfileCreatedResp(OctoModel):
    success: bool = True
    msg: str = ""
    data: Dict[str, Any] = Field(default_factory=dict)
    code: str = ""


class DeleteProfileRequest(OctoModel):
    uuids: List[str]
    skip_trash_bin: bool = True


class ProfileForceStopRequest(OctoModel):
    version: int


class SetProfilePasswordRequestAutomation(OctoModel):
    profiles: List[str]
    password: str
    old_password: Optional[str] = None


class ClearProfilePasswordRequestAutomation(OctoModel):
    password: str


class TransferProfilesRequest(OctoModel):
    uuids: List[str]
    receiver_email: str
    transfer_proxy: bool


class ExportProfilesData(OctoModel):
    uuids: List[str]
    export_proxy: bool
    app_version: Optional[str] = None


class ImportDataV1(OctoModel):
    title: str
    exported_at: str
    profile: str


class ImportDataV2(OctoModel):
    data: str


class ImportFileV1(OctoModel):
    data: Union[ImportDataV1, Dict[str, Any]]
    signature: str


class ImportFileV2(OctoModel):
    data: Union[ImportDataV2, Dict[str, Any]]
    uuid: Optional[str] = None
    title: Optional[str] = None


class ImportProfilesRequest(OctoModel):
    data: List[Union[str, ImportFileV2, ImportFileV1, Dict[str, Any]]]

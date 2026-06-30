from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ..enums import ProxyType
from ._base import OctoModel
from .fingerprint import FingerprintDataInBaseSpec, FingerprintUpdateIn
from .proxies import ProxyDataInExtraIgnore, ProxyUUID

__all__ = [
    "Bookmark",
    "StorageOptions",
    "CookiesRequest",
    "ProfileProxyOut",
    "ProfileOut",
    "ProfileCreateRequestAutomation",
    "ProfileUpdateRequest",
    "ProfilesResp",
    "ProfileResp",
    "ProfileCreatedResp",
    "DeleteProfileRequest",
    "ProfileForceStopRequest",
    "MassForceStopRequest",
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
    cookies: List[Union[Dict[str, Any], str]]


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
    cookies: Optional[List[Union[Dict[str, Any], str]]] = None
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
    cookies: Optional[List[Union[Dict[str, Any], str]]] = None
    image: Optional[str] = None
    fingerprint: Optional[Union[FingerprintUpdateIn, Dict[str, Any]]] = None
    extensions: Optional[List[str]] = None
    launch_args: Optional[List[str]] = None
    images_load_limit: Optional[int] = None
    local_cache: Optional[bool] = None


class ProfileProxyOut(OctoModel):
    uuid: Optional[str] = None
    type: Optional[ProxyType] = None
    host: Optional[str] = None
    port: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None
    change_ip_url: Optional[str] = None
    external_id: Optional[str] = None


class ProfileOut(OctoModel):
    uuid: str
    title: Optional[str] = None
    description: Optional[str] = None
    start_pages: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    folder: Optional[str] = None
    pinned_tag: Optional[str] = None
    has_user_password: Optional[bool] = None
    password_set_at: Optional[str] = None
    proxy: Optional[ProfileProxyOut] = None
    status: Optional[int] = None
    version: Optional[str] = None
    storage_options: Optional[StorageOptions] = None
    fingerprint: Optional[Dict[str, Any]] = None
    bookmarks: Optional[List[Dict[str, Any]]] = None
    extensions: Optional[List[Any]] = None
    image: Optional[str] = None
    launch_args: Optional[List[str]] = None
    images_load_limit: Optional[int] = None
    local_cache: Optional[bool] = None
    last_active: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    extra_info: Any = None


class ProfilesResp(OctoModel):
    success: bool = True
    msg: str = ""
    data: List[ProfileOut] = Field(default_factory=list)
    total_count: int = 0
    page: int = 0
    code: Optional[str] = None


class ProfileResp(OctoModel):
    success: bool = True
    msg: str = ""
    data: Optional[ProfileOut] = None
    code: Optional[str] = None


class ProfileCreatedResp(OctoModel):
    success: bool = True
    msg: str = ""
    data: Optional[ProfileOut] = None
    code: Optional[str] = None


class DeleteProfileRequest(OctoModel):
    uuids: List[str]
    skip_trash_bin: bool = True


class ProfileForceStopRequest(OctoModel):
    version: int = Field(gt=0)


class MassForceStopRequest(OctoModel):
    uuids: List[str]


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

from __future__ import annotations

from typing import Any

from pydantic import Field, HttpUrl

from ..enums import ProxyType
from ._base import OctoModel
from .fingerprint import Fingerprint, FingerprintUpdate
from .proxies import ProxyData, ProxyRef

__all__ = [
    'Bookmark',
    'StorageOptions',
    'Cookies',
    'ProfileProxy',
    'Profile',
    'ProfileCreate',
    'ProfileUpdate',
    'ProfileDelete',
    'ProfileForceStop',
    'ProfilesForceStop',
    'SetProfilePassword',
    'ClearProfilePassword',
    'TransferProfiles',
    'ExportProfiles',
    'ImportDataV1',
    'ImportDataV2',
    'ImportFileV1',
    'ImportFileV2',
    'ImportProfiles',
    'ExportedProfile',
    'ExportResult',
    'ExportList',
    'ImportResult',
]


class Bookmark(OctoModel):
    name: str
    url: HttpUrl


class StorageOptions(OctoModel):
    cookies: bool = True
    passwords: bool = True
    extensions: bool = False
    localstorage: bool = False
    history: bool = False
    bookmarks: bool = True
    serviceworkers: bool = False


class Cookies(OctoModel):
    cookies: list[dict[str, Any] | str]


class ProfileCreate(OctoModel):
    title: str
    fingerprint: Fingerprint | dict[str, Any]
    description: str | None = None
    start_pages: list[str] | None = None
    bookmarks: list[Bookmark | dict[str, Any]] | None = None
    tags: list[str] | None = None
    folder: str | None = None
    pinned_tag: str | None = None
    password: str | None = None
    proxy: ProxyData | ProxyRef | dict[str, Any] | None = None
    storage_options: StorageOptions | dict[str, Any] | None = None
    cookies: list[dict[str, Any] | str] | None = None
    image: str | None = None
    extensions: list[str] | None = None
    launch_args: list[str] | None = None
    images_load_limit: int | None = Field(default=None, ge=0)
    local_cache: bool | None = None
    extra_info: dict[str, Any] | None = None


class ProfileUpdate(OctoModel):
    title: str | None = None
    description: str | None = None
    start_pages: list[str] | None = None
    tags: list[str] | None = None
    folder: str | None = None
    pinned_tag: str | None = None
    bookmarks: list[Bookmark | dict[str, Any]] | None = None
    proxy: ProxyData | ProxyRef | dict[str, Any] | None = None
    storage_options: StorageOptions | dict[str, Any] | None = None
    cookies: list[dict[str, Any] | str] | None = None
    image: str | None = None
    fingerprint: FingerprintUpdate | dict[str, Any] | None = None
    extensions: list[str] | None = None
    launch_args: list[str] | None = None
    images_load_limit: int | None = Field(default=None, ge=0)
    local_cache: bool | None = None
    extra_info: dict[str, Any] | None = None


class ProfileProxy(OctoModel):
    uuid: str | None = None
    type: ProxyType | None = None
    host: str | None = None
    port: int | None = None
    login: str | None = None
    password: str | None = None
    change_ip_url: str | None = None
    external_id: str | None = None


class Profile(OctoModel):
    uuid: str
    title: str | None = None
    description: str | None = None
    start_pages: list[str] | None = None
    tags: list[str] | None = None
    folder: str | None = None
    pinned_tag: str | None = None
    has_user_password: bool | None = None
    password_set_at: str | None = None
    proxy: ProfileProxy | None = None
    status: int | None = None
    version: str | None = None
    storage_options: StorageOptions | None = None
    fingerprint: dict[str, Any] | None = None
    bookmarks: list[dict[str, Any]] | None = None
    extensions: list[Any] | None = None
    image: str | None = None
    launch_args: list[str] | None = None
    images_load_limit: int | None = None
    local_cache: bool | None = None
    last_active: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    extra_info: Any = None


class ProfileDelete(OctoModel):
    uuids: list[str]
    skip_trash_bin: bool = True


class ProfileForceStop(OctoModel):
    version: int | None = Field(default=None, gt=0)


class ProfilesForceStop(OctoModel):
    uuids: list[str]


class SetProfilePassword(OctoModel):
    profiles: list[str]
    password: str
    old_password: str | None = None


class ClearProfilePassword(OctoModel):
    password: str


class TransferProfiles(OctoModel):
    uuids: list[str]
    receiver_email: str
    transfer_proxy: bool


class ExportProfiles(OctoModel):
    uuids: list[str]
    export_proxy: bool
    app_version: str | None = None


class ImportDataV1(OctoModel):
    title: str
    exported_at: str
    profile: str


class ImportDataV2(OctoModel):
    data: str


class ImportFileV1(OctoModel):
    data: ImportDataV1 | dict[str, Any]
    signature: str


class ImportFileV2(OctoModel):
    data: ImportDataV2 | dict[str, Any]
    uuid: str | None = None
    title: str | None = None


class ImportProfiles(OctoModel):
    data: list[str | ImportFileV2 | ImportFileV1 | dict[str, Any]]
    folder: str | None = None


class ExportedProfile(OctoModel):
    uuid: str
    title: str | None = None
    data: str


class ExportResult(OctoModel):
    exported: list[ExportedProfile] = Field(default_factory=list)
    failed: list[str] = Field(default_factory=list)


class ExportList(OctoModel):
    data: list[ExportedProfile] = Field(default_factory=list)
    total: int = 0
    page: int = 0


class ImportResult(OctoModel):
    failed: list[str] = Field(default_factory=list)
    imported: list[str] | None = None

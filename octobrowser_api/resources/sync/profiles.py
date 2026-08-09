from __future__ import annotations

import builtins
from typing import Any, overload

from ...enums import ProfileOrdering
from ...models import (
    Bookmark,
    ClearProfilePassword,
    Cookies,
    ExportedProfile,
    ExportList,
    ExportProfiles,
    ExportResult,
    Fingerprint,
    FingerprintUpdate,
    ImportFileV1,
    ImportFileV2,
    ImportProfiles,
    ImportResult,
    ListResponse,
    Profile,
    ProfileCreate,
    ProfileDelete,
    ProfileForceStop,
    ProfilesForceStop,
    ProfileUpdate,
    ProxyData,
    ProxyRef,
    Response,
    SetProfilePassword,
    StorageOptions,
    TransferProfiles,
)
from .._base import Resource, query, unwrap


class Profiles(Resource):
    def list(
        self,
        *,
        fields: str | None = None,
        search: str | None = None,
        search_tags: str | None = None,
        ordering: ProfileOrdering | str | None = None,
        page_len: int | None = None,
        page: int | None = None,
    ) -> builtins.list[Profile]:
        params = query(
            fields=fields,
            search=search,
            search_tags=search_tags,
            ordering=ordering,
            page_len=page_len,
            page=page,
        )
        return self._transport.request(
            'GET', '/profiles', params=params, out=ListResponse[Profile]
        ).data

    def get(self, uuid: str) -> Profile:
        resp = self._transport.request(
            'GET', f'/profiles/{uuid}', out=Response[Profile]
        )
        return unwrap(resp.data)

    @overload
    def create(self, data: ProfileCreate, /) -> Profile: ...
    @overload
    def create(
        self,
        *,
        title: str,
        fingerprint: Fingerprint | dict[str, Any],
        description: str | None = None,
        start_pages: builtins.list[str] | None = None,
        bookmarks: builtins.list[Bookmark | dict[str, Any]] | None = None,
        tags: builtins.list[str] | None = None,
        folder: str | None = None,
        pinned_tag: str | None = None,
        password: str | None = None,
        proxy: ProxyData | ProxyRef | dict[str, Any] | None = None,
        storage_options: StorageOptions | dict[str, Any] | None = None,
        cookies: builtins.list[dict[str, Any] | str] | None = None,
        image: str | None = None,
        extensions: builtins.list[str] | None = None,
        launch_args: builtins.list[str] | None = None,
        images_load_limit: int | None = None,
        local_cache: bool | None = None,
        extra_info: dict[str, Any] | None = None,
    ) -> Profile: ...
    def create(self, data: ProfileCreate | None = None, **fields: Any) -> Profile:
        body = data if data is not None else ProfileCreate(**fields)
        resp = self._transport.request(
            'POST', '/profiles', body=body, out=Response[Profile]
        )
        return unwrap(resp.data)

    @overload
    def update(self, uuid: str, data: ProfileUpdate, /) -> Profile: ...
    @overload
    def update(
        self,
        uuid: str,
        /,
        *,
        title: str | None = None,
        description: str | None = None,
        start_pages: builtins.list[str] | None = None,
        tags: builtins.list[str] | None = None,
        folder: str | None = None,
        pinned_tag: str | None = None,
        bookmarks: builtins.list[Bookmark | dict[str, Any]] | None = None,
        proxy: ProxyData | ProxyRef | dict[str, Any] | None = None,
        storage_options: StorageOptions | dict[str, Any] | None = None,
        cookies: builtins.list[dict[str, Any] | str] | None = None,
        image: str | None = None,
        fingerprint: FingerprintUpdate | dict[str, Any] | None = None,
        extensions: builtins.list[str] | None = None,
        launch_args: builtins.list[str] | None = None,
        images_load_limit: int | None = None,
        local_cache: bool | None = None,
        extra_info: dict[str, Any] | None = None,
    ) -> Profile: ...
    def update(
        self, uuid: str, data: ProfileUpdate | None = None, **fields: Any
    ) -> Profile:
        body = data if data is not None else ProfileUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/profiles/{uuid}', body=body, out=Response[Profile]
        )
        return unwrap(resp.data)

    def delete(self, uuids: builtins.list[str], *, skip_trash_bin: bool = True) -> None:
        self._transport.request(
            'DELETE',
            '/profiles',
            body=ProfileDelete(uuids=uuids, skip_trash_bin=skip_trash_bin),
        )

    def import_cookies(
        self, uuid: str, cookies: builtins.list[dict[str, Any] | str]
    ) -> None:
        self._transport.request(
            'POST', f'/profiles/{uuid}/import_cookies', body=Cookies(cookies=cookies)
        )

    def force_stop(self, uuid: str, version: int) -> None:
        self._transport.request(
            'POST',
            f'/profiles/{uuid}/force_stop',
            body=ProfileForceStop(version=version),
        )

    def force_stop_many(self, uuids: builtins.list[str]) -> None:
        self._transport.request(
            'POST', '/profiles/force_stop', body=ProfilesForceStop(uuids=uuids)
        )

    def set_password(
        self, uuids: builtins.list[str], password: str, *, old_password: str | None = None
    ) -> None:
        self._transport.request(
            'POST',
            '/profiles/set_password',
            body=SetProfilePassword(
                profiles=uuids, password=password, old_password=old_password
            ),
        )

    def clear_password(self, uuid: str, password: str) -> None:
        self._transport.request(
            'POST',
            f'/profiles/{uuid}/clear_password',
            body=ClearProfilePassword(password=password),
        )

    def transfer(
        self, uuids: builtins.list[str], receiver_email: str, *, transfer_proxy: bool = False
    ) -> None:
        self._transport.request(
            'POST',
            '/profiles/transfer',
            body=TransferProfiles(
                uuids=uuids,
                receiver_email=receiver_email,
                transfer_proxy=transfer_proxy,
            ),
        )

    def export(
        self,
        uuids: builtins.list[str],
        *,
        export_proxy: bool = False,
        app_version: str | None = None,
    ) -> ExportResult:
        body = ExportProfiles(
            uuids=uuids, export_proxy=export_proxy, app_version=app_version
        )
        resp = self._transport.request(
            'POST', '/profiles/export', body=body, out=Response[ExportResult]
        )
        return unwrap(resp.data)

    def exports(
        self, *, page: int | None = None, page_len: int | None = None
    ) -> ExportList:
        params = query(page=page, page_len=page_len)
        resp = self._transport.request(
            'GET', '/profiles/export', params=params, out=Response[ExportList]
        )
        return unwrap(resp.data)

    def get_export(self, uuid: str) -> ExportedProfile:
        resp = self._transport.request(
            'GET', f'/profiles/export/{uuid}', out=Response[ExportedProfile]
        )
        return unwrap(resp.data)

    def import_(
        self,
        data: builtins.list[str | ImportFileV2 | ImportFileV1 | dict[str, Any]],
        *,
        folder: str | None = None,
    ) -> ImportResult:
        resp = self._transport.request(
            'POST',
            '/profiles/import',
            body=ImportProfiles(data=data, folder=folder),
            out=Response[ImportResult],
        )
        return unwrap(resp.data)

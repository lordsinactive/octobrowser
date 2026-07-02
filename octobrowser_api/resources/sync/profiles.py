from __future__ import annotations
from typing import Any, Dict, List, Optional, Union, overload

from .._base import Resource, query, unwrap
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


class Profiles(Resource):
    def list(
        self,
        *,
        fields: Optional[str] = None,
        search: Optional[str] = None,
        search_tags: Optional[str] = None,
        page_len: Optional[int] = None,
        page: Optional[int] = None,
    ) -> List[Profile]:
        params = query(
            fields=fields,
            search=search,
            search_tags=search_tags,
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
        fingerprint: Union[Fingerprint, Dict[str, Any]],
        description: Optional[str] = None,
        start_pages: Optional[List[str]] = None,
        bookmarks: Optional[List[Union[Bookmark, Dict[str, Any]]]] = None,
        tags: Optional[List[str]] = None,
        pinned_tag: Optional[str] = None,
        password: Optional[str] = None,
        proxy: Optional[Union[ProxyData, ProxyRef, Dict[str, Any]]] = None,
        storage_options: Optional[Union[StorageOptions, Dict[str, Any]]] = None,
        cookies: Optional[List[Union[Dict[str, Any], str]]] = None,
        image: Optional[str] = None,
        extensions: Optional[List[str]] = None,
        launch_args: Optional[List[str]] = None,
        images_load_limit: Optional[int] = None,
        local_cache: Optional[bool] = None,
    ) -> Profile: ...
    def create(self, data: Optional[ProfileCreate] = None, **fields: Any) -> Profile:
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
        title: Optional[str] = None,
        description: Optional[str] = None,
        start_pages: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        pinned_tag: Optional[str] = None,
        bookmarks: Optional[List[Union[Bookmark, Dict[str, Any]]]] = None,
        proxy: Optional[Union[ProxyData, ProxyRef, Dict[str, Any]]] = None,
        storage_options: Optional[Union[StorageOptions, Dict[str, Any]]] = None,
        cookies: Optional[List[Union[Dict[str, Any], str]]] = None,
        image: Optional[str] = None,
        fingerprint: Optional[Union[FingerprintUpdate, Dict[str, Any]]] = None,
        extensions: Optional[List[str]] = None,
        launch_args: Optional[List[str]] = None,
        images_load_limit: Optional[int] = None,
        local_cache: Optional[bool] = None,
    ) -> Profile: ...
    def update(
        self, uuid: str, data: Optional[ProfileUpdate] = None, **fields: Any
    ) -> Profile:
        body = data if data is not None else ProfileUpdate(**fields)
        resp = self._transport.request(
            'PATCH', f'/profiles/{uuid}', body=body, out=Response[Profile]
        )
        return unwrap(resp.data)

    def delete(self, uuids: List[str], *, skip_trash_bin: bool = True) -> None:
        self._transport.request(
            'DELETE',
            '/profiles',
            body=ProfileDelete(uuids=uuids, skip_trash_bin=skip_trash_bin),
        )

    def import_cookies(
        self, uuid: str, cookies: List[Union[Dict[str, Any], str]]
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

    def force_stop_many(self, uuids: List[str]) -> None:
        self._transport.request(
            'POST', '/profiles/force_stop', body=ProfilesForceStop(uuids=uuids)
        )

    def set_password(
        self, uuids: List[str], password: str, *, old_password: Optional[str] = None
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
        self, uuids: List[str], receiver_email: str, *, transfer_proxy: bool = False
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
        uuids: List[str],
        *,
        export_proxy: bool = False,
        app_version: Optional[str] = None,
    ) -> ExportResult:
        body = ExportProfiles(
            uuids=uuids, export_proxy=export_proxy, app_version=app_version
        )
        resp = self._transport.request(
            'POST', '/profiles/export', body=body, out=Response[ExportResult]
        )
        return unwrap(resp.data)

    def exports(
        self, *, page: Optional[int] = None, page_len: Optional[int] = None
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
        self, data: List[Union[str, ImportFileV2, ImportFileV1, Dict[str, Any]]]
    ) -> ImportResult:
        resp = self._transport.request(
            'POST',
            '/profiles/import',
            body=ImportProfiles(data=data),
            out=Response[ImportResult],
        )
        return unwrap(resp.data)
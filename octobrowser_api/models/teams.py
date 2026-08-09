from __future__ import annotations

from typing import Any

from ._base import OctoModel

__all__ = [
    'Extension',
    'ExtensionsDelete',
    'ProxyPermissions',
    'PaidProxyPermissions',
    'ProfilePermissions',
    'TemplatePermissions',
    'ExtensionPermissions',
    'TaskPermissions',
    'SubaccountPermissions',
    'Subaccount',
    'SubaccountCreate',
    'SubaccountUpdate',
    'SubaccountDelete',
    'Invite',
    'InviteDelete',
]


class Extension(OctoModel):
    uuid: str
    name: str
    version: str


class ExtensionsDelete(OctoModel):
    uuids: list[str]


class ProxyPermissions(OctoModel):
    create: bool = False
    edit: bool = False
    delete: bool = False


class PaidProxyPermissions(OctoModel):
    create: bool = False


class ProfilePermissions(OctoModel):
    transfer: bool = False
    clone: bool = False
    create: bool = False
    edit: bool = False
    delete: bool = False
    passwords: bool = False


class TemplatePermissions(OctoModel):
    create: bool = False
    edit: bool = False
    delete: bool = False


class ExtensionPermissions(OctoModel):
    delete: bool = False


class TaskPermissions(OctoModel):
    view: bool = False
    manage: bool = False


class SubaccountPermissions(OctoModel):
    manage_team: bool = False
    edit_tags: bool = False
    view_all_tags: bool = False
    edit_folders: bool = False
    view_all_folders: bool = False
    manage_action_log: bool = False
    proxies: ProxyPermissions | None = None
    paid_proxies: PaidProxyPermissions | None = None
    profiles: ProfilePermissions | None = None
    templates: TemplatePermissions | None = None
    extensions: ExtensionPermissions | None = None
    tasks: TaskPermissions | None = None
    visible_tags: list[str] | None = None
    visible_folders: list[str] | None = None
    view_profiles_wo_folders: bool = False


class Subaccount(OctoModel):
    uuid: str
    email: str
    master: bool = False
    created_at: str | None = None
    permissions: SubaccountPermissions | None = None


class SubaccountCreate(OctoModel):
    email: str
    permissions: SubaccountPermissions | dict[str, Any] | None = None


class SubaccountUpdate(OctoModel):
    email: str
    permissions: SubaccountPermissions | dict[str, Any] | None = None


class SubaccountDelete(OctoModel):
    email: str


class Invite(OctoModel):
    receiver: str
    created_at: str | None = None


class InviteDelete(OctoModel):
    receiver: str

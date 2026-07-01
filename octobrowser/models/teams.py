from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

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
    uuids: List[str]


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
    manage_action_log: bool = False
    proxies: Optional[ProxyPermissions] = None
    paid_proxies: Optional[PaidProxyPermissions] = None
    profiles: Optional[ProfilePermissions] = None
    templates: Optional[TemplatePermissions] = None
    extensions: Optional[ExtensionPermissions] = None
    tasks: Optional[TaskPermissions] = None
    visible_tags: Optional[List[str]] = None


class Subaccount(OctoModel):
    uuid: str
    email: str
    master: bool = False
    created_at: Optional[str] = None
    permissions: Optional[SubaccountPermissions] = None


class SubaccountCreate(OctoModel):
    email: str
    permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None


class SubaccountUpdate(OctoModel):
    email: str
    permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None


class SubaccountDelete(OctoModel):
    email: str


class Invite(OctoModel):
    receiver: str
    created_at: Optional[str] = None


class InviteDelete(OctoModel):
    receiver: str

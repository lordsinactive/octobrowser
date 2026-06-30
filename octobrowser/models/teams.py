from __future__ import annotations
from typing import Any, Dict, List, Optional, Union

from pydantic import Field
from ._base import OctoModel

__all__ = [
    "ExtensionOut",
    "ExtensionsListResponse",
    "DeleteExtensionsRequest",
    "ProxyPermissions",
    "PaidProxyPermissions",
    "ProfilePermissions",
    "TemplatePermissions",
    "ExtensionPermissions",
    "TaskPermissions",
    "SubaccountPermissions",
    "SubaccountOut",
    "SubaccountsResponse",
    "CreateSubaccountRequest",
    "UpdateSubaccountRequest",
    "DeleteSubaccountRequest",
    "InviteOut",
    "InvitesResponse",
    "DeleteInviteRequest",
]


class ExtensionOut(OctoModel):
    uuid: str
    name: str
    version: str


class ExtensionsListResponse(OctoModel):
    success: bool = True
    msg: str = ""
    code: str = ""
    data: List[ExtensionOut] = Field(default_factory=list)


class DeleteExtensionsRequest(OctoModel):
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


class SubaccountOut(OctoModel):
    uuid: str
    email: str
    master: bool = False
    created_at: Optional[str] = None
    permissions: Optional[SubaccountPermissions] = None


class SubaccountsResponse(OctoModel):
    success: bool = True
    msg: str = ""
    total_count: int = 0
    data: List[SubaccountOut] = Field(default_factory=list)


class CreateSubaccountRequest(OctoModel):
    email: str
    permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None


class UpdateSubaccountRequest(OctoModel):
    email: str
    permissions: Optional[Union[SubaccountPermissions, Dict[str, Any]]] = None


class DeleteSubaccountRequest(OctoModel):
    email: str


class InviteOut(OctoModel):
    receiver: str
    created_at: Optional[str] = None


class InvitesResponse(OctoModel):
    success: bool = True
    msg: str = ""
    total_count: int = 0
    data: List[InviteOut] = Field(default_factory=list)


class DeleteInviteRequest(OctoModel):
    receiver: str

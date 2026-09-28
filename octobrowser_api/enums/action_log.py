from __future__ import annotations

from enum import StrEnum

__all__ = ['ActionType']


class ActionType(StrEnum):
    PROFILES_CREATED = 'profiles.created'
    PROFILES_STARTED = 'profiles.started'
    PROFILES_STOPPED = 'profiles.stopped'
    PROFILES_FORCE_STOPPED = 'profiles.force_stopped'
    PROFILES_TRANSFERRED = 'profiles.transferred'
    PROFILES_TRASHED = 'profiles.trashed'
    PROFILES_UPDATED = 'profiles.updated'
    PROFILES_DELETED = 'profiles.deleted'
    PROFILES_PROXY_ASSIGNED = 'profiles.proxy_assigned'
    PROFILES_PROXY_UNASSIGNED = 'profiles.proxy_unassigned'
    PROFILES_PROXY_CHANGED = 'profiles.proxy_changed'

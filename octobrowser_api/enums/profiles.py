from __future__ import annotations
from enum import StrEnum

__all__ = ['ProfileField']


class ProfileField(StrEnum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    PROXY = 'proxy'
    START_PAGES = 'start_pages'
    TAGS = 'tags'
    FOLDER = 'folder'
    STATUS = 'status'
    LAST_ACTIVE = 'last_active'
    VERSION = 'version'
    STORAGE_OPTIONS = 'storage_options'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'
    HAS_USER_PASSWORD = 'has_user_password'
    PINNED_TAG = 'pinned_tag'
    LAUNCH_ARGS = 'launch_args'
    IMAGES_LOAD_LIMIT = 'images_load_limit'
    LOCAL_CACHE = 'local_cache'
    EXTRA_INFO = 'extra_info'

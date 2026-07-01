from __future__ import annotations
from enum import IntEnum, StrEnum

__all__ = ['PageSize', 'ErrorCode']


class PageSize(IntEnum):
    LEN_10 = 10
    LEN_25 = 25
    LEN_50 = 50
    LEN_100 = 100


class ErrorCode(StrEnum):
    UNKNOWN_ERROR = 'unknown_error'
    INTERNAL_ERROR = 'internal_error'
    API_TOKEN = 'api_token'
    NO_PERMISSION = 'no_permission'
    NO_TOKENS = 'no_tokens'
    LIMIT_REACHED = 'limit_reached'
    NOT_FOUND = 'not_found'
    ALREADY_EXISTS = 'already_exists'
    PROFILES_TRANSFER_ERROR = 'profiles.transfer_error'
    PROFILES_TRANSFER_NO_RECEIVER = 'profiles.transfer_no_receiver'
    PROFILES_TRANSFER_NO_PROFILES = 'profiles.transfer_no_profiles'
    PROFILES_EXPORT_LIMIT_EXCEEDED = 'profiles.export_limit_exceeded'
    PROFILES_EXPORT_ERROR = 'profiles.export_error'
    PROFILES_IMPORT_LIMIT_EXCEEDED = 'profiles.import_limit_exceeded'
    PROFILES_IMPORT_ERROR = 'profiles.import_error'
    PROFILES_IMPORT_NO_VALID_PROFILES = 'profiles.import_no_valid_profiles'
    PROFILES_STARTED = 'profiles.started'
    PROFILES_ALREADY_STARTED = 'profiles.already_started'
    PROFILES_NOT_STARTED = 'profiles.not_started'
    PROFILES_UPDATE_ERROR = 'profiles.update_error'
    PROFILES_CONSISTENCY_ERROR = 'profiles.consistency_error'
    PROFILES_PASSWORD_ERROR = 'profiles.password_error'
    PROFILES_INVALID_COOKIE = 'profiles.invalid_cookie'
    PROFILES_STOP_ERROR = 'profiles.stop_error'
    PROFILES_PROXY_ERROR = 'profiles.proxy_error'
    PROFILES_INVALID_PASSWORD = 'profiles.invalid_password'
    PROFILES_PASSWORD_CHANGE_FAILED = 'profiles.password_change_failed'
    FINGERPRINTS_INVALID = 'fingerprints.invalid'
    SUBSCRIPTIONS_INACTIVE = 'subscriptions.inactive'
    PROXY_PROVIDERS_EMPTY_BALANCE = 'proxy_providers.empty_balance'
    PROXY_MAXIMUM_SAVED_ERROR = 'proxy.maximum_saved_error'
    CLIENT_UPDATE_FAILED = 'client.update_failed'

from __future__ import annotations
from typing import Any, Dict, Optional, Tuple, Type

import httpx
from .enums import ErrorCode


class OctoError(Exception):
    pass


class OctoAPIError(OctoError):
    def __init__(
        self,
        message: str = '',
        *,
        status_code: Optional[int] = None,
        code: Optional[str] = None,
        body: Any = None,
        response: Optional[httpx.Response] = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        self.body = body
        self.response = response
        super().__init__(f'[{status_code}] {code or "-"}: {message}')


class AuthError(OctoAPIError):
    pass


class NotFoundError(OctoAPIError):
    pass


class ConflictError(OctoAPIError):
    pass


class ForbiddenError(OctoAPIError):
    pass


class LimitReachedError(OctoAPIError):
    pass


class SubscriptionError(OctoAPIError):
    pass


class InvalidRequestError(OctoAPIError):
    pass


class RateLimitError(OctoAPIError):
    def __init__(
        self, *args: Any, retry_after: Optional[float] = None, **kwargs: Any
    ) -> None:
        self.retry_after = retry_after
        super().__init__(*args, **kwargs)


_CODE_MAP: Dict[str, Type[OctoAPIError]] = {
    ErrorCode.API_TOKEN: AuthError,
    ErrorCode.NOT_FOUND: NotFoundError,
    ErrorCode.ALREADY_EXISTS: ConflictError,
    ErrorCode.PROFILES_STARTED: ConflictError,
    ErrorCode.PROFILES_NOT_STARTED: ConflictError,
    ErrorCode.PROFILES_CONSISTENCY_ERROR: ConflictError,
    ErrorCode.NO_PERMISSION: ForbiddenError,
    ErrorCode.LIMIT_REACHED: LimitReachedError,
    ErrorCode.NO_TOKENS: LimitReachedError,
    ErrorCode.PROXY_MAXIMUM_SAVED_ERROR: LimitReachedError,
    ErrorCode.SUBSCRIPTIONS_INACTIVE: SubscriptionError,
    ErrorCode.PROFILES_ALREADY_STARTED: ConflictError,
}

_STATUS_MAP: Dict[int, Type[OctoAPIError]] = {
    401: AuthError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    422: InvalidRequestError,
    429: RateLimitError,
}


def _extract(body: Any) -> Tuple[Optional[str], str, bool]:
    if isinstance(body, dict):
        if 'validation_error' in body or 'detail' in body:
            return None, 'Request validation failed', True
        if 'success' in body:
            return body.get('code'), body.get('msg') or '', False
        if 'error' in body:
            return body.get('code'), body.get('error') or '', False
    return None, '', False


def _classify(
    status: int, code: Optional[str], is_validation: bool
) -> Type[OctoAPIError]:
    if is_validation:
        return InvalidRequestError
    if code and code in _CODE_MAP:
        return _CODE_MAP[code]
    return _STATUS_MAP.get(status, OctoAPIError)


def raise_for_response(response: httpx.Response) -> None:
    try:
        body: Any = response.json()
    except Exception:
        body = None

    is_error = response.is_error or (
        isinstance(body, dict) and (body.get('success') is False or 'error' in body)
    )
    if not is_error:
        return

    status = response.status_code
    code, message, is_validation = _extract(body if body is not None else {})
    if not message:
        message = response.text[:200]

    exc_cls = _classify(status, code, is_validation)
    if exc_cls is RateLimitError:
        retry_after = response.headers.get('retry-after')
        raise RateLimitError(
            message,
            status_code=status,
            code=code,
            body=body,
            response=response,
            retry_after=float(retry_after) if retry_after else None,
        )
    raise exc_cls(message, status_code=status, code=code, body=body, response=response)

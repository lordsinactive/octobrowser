from __future__ import annotations

from typing import Any, TypeVar

from .._transport import AsyncTransport, Transport
from ..exceptions import OctoError

T = TypeVar('T')


class Resource:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport


class AsyncResource:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport


def unwrap(value: T | None) -> T:
    if value is None:
        raise OctoError('unexpected empty response data')
    return value


def query(**kwargs: Any) -> dict[str, Any] | None:
    params = {k: v for k, v in kwargs.items() if v is not None}
    return params or None

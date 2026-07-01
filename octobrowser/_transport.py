from __future__ import annotations

import asyncio
import time
from typing import Any, Dict, Optional, Type, TypeVar, overload

import httpx
from pydantic import BaseModel
from .exceptions import RateLimitError, raise_for_response

CLOUD_BASE = 'https://app.octobrowser.net/api/v2/automation'
LOCAL_BASE = 'http://localhost:58888/api'

DEFAULT_TIMEOUT = 30.0
DEFAULT_RETRY_BACKOFF = 30.0

M = TypeVar('M', bound=BaseModel)


def _serialize(model: BaseModel) -> Any:
    return model.model_dump(mode='json', by_alias=True, exclude_none=True)


class Transport:
    def __init__(
        self,
        base_url: str,
        *,
        token: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT,
        wait_on_rate_limit: bool = False,
    ) -> None:
        headers = {'X-Octo-Api-Token': token} if token else {}
        self._client = httpx.Client(base_url=base_url, headers=headers, timeout=timeout)
        self._wait_on_rate_limit = wait_on_rate_limit

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: None = None,
    ) -> httpx.Response: ...

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: Type[M],
    ) -> M: ...

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: Optional[Type[M]] = None,
    ) -> Any:
        payload = _serialize(body) if body is not None else json
        while True:
            response = self._client.request(method, path, params=params, json=payload)
            try:
                raise_for_response(response)
            except RateLimitError as exc:
                if not self._wait_on_rate_limit:
                    raise
                wait = (
                    exc.retry_after
                    if exc.retry_after is not None
                    else DEFAULT_RETRY_BACKOFF
                )
                time.sleep(wait)
                continue
            if out is None:
                return response
            return out.model_validate(response.json())

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Transport:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


class AsyncTransport:
    def __init__(
        self,
        base_url: str,
        *,
        token: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT,
        wait_on_rate_limit: bool = False,
    ) -> None:
        headers = {'X-Octo-Api-Token': token} if token else {}
        self._client = httpx.AsyncClient(
            base_url=base_url, headers=headers, timeout=timeout
        )
        self._wait_on_rate_limit = wait_on_rate_limit

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: None = None,
    ) -> httpx.Response: ...

    @overload
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: Type[M],
    ) -> M: ...

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Any = None,
        body: Optional[BaseModel] = None,
        out: Optional[Type[M]] = None,
    ) -> Any:
        payload = _serialize(body) if body is not None else json
        while True:
            response = await self._client.request(
                method, path, params=params, json=payload
            )
            try:
                raise_for_response(response)
            except RateLimitError as exc:
                if not self._wait_on_rate_limit:
                    raise
                wait = (
                    exc.retry_after
                    if exc.retry_after is not None
                    else DEFAULT_RETRY_BACKOFF
                )
                await asyncio.sleep(wait)
                continue
            if out is None:
                return response
            return out.model_validate(response.json())

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> AsyncTransport:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.aclose()

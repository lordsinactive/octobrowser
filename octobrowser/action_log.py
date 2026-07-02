from __future__ import annotations
import json
from typing import AsyncIterator, Dict, Iterator, NoReturn, Optional
from urllib.parse import urlencode

from websockets.asyncio.client import ClientConnection as _AsyncConnection
from websockets.asyncio.client import connect as _async_connect
from websockets.exceptions import InvalidStatus
from websockets.sync.client import ClientConnection as _SyncConnection
from websockets.sync.client import connect as _sync_connect

from ._transport import CLOUD_BASE
from .exceptions import _classify
from .models import ActionLogEntry, ActionLogPage, ActionLogWatermark


def _ws_url(base_url: str) -> str:
    base = base_url.replace('https://', 'wss://').replace('http://', 'ws://')
    return f'{base}/ws/action_log'


def _with_params(
    url: str, from_timestamp: Optional[int], after_uuid: Optional[str]
) -> str:
    params: Dict[str, object] = {}
    if from_timestamp is not None:
        params['from_timestamp'] = from_timestamp
    if after_uuid is not None:
        params['after_uuid'] = after_uuid
    return f'{url}?{urlencode(params)}' if params else url


def _raise_ws_error(exc: InvalidStatus) -> NoReturn:
    response = exc.response
    raw = bytes(response.body or b'')
    try:
        body: object = json.loads(raw)
    except Exception:
        body = None
    if isinstance(body, dict):
        code = body.get('code')
        message = body.get('msg') or ''
    else:
        code = None
        message = raw.decode('utf-8', 'replace')[:200]
    exc_cls = _classify(response.status_code, code, False)
    raise exc_cls(
        message, status_code=response.status_code, code=code, body=body
    ) from exc


class ActionLogStream:
    def __init__(self, url: str, headers: Dict[str, str]) -> None:
        self._url = url
        self._headers = headers
        self._ws: Optional[_SyncConnection] = None
        self.watermark: Optional[ActionLogWatermark] = None

    def __enter__(self) -> ActionLogStream:
        try:
            self._ws = _sync_connect(self._url, additional_headers=self._headers)
        except InvalidStatus as exc:
            _raise_ws_error(exc)
        return self

    def __exit__(self, *exc: object) -> None:
        if self._ws is not None:
            self._ws.close()

    def __iter__(self) -> Iterator[ActionLogEntry]:
        assert self._ws is not None
        for message in self._ws:
            page = ActionLogPage.model_validate_json(message)
            if page.watermark is not None:
                self.watermark = page.watermark
            yield from page.items


class AsyncActionLogStream:
    def __init__(self, url: str, headers: Dict[str, str]) -> None:
        self._url = url
        self._headers = headers
        self._ws: Optional[_AsyncConnection] = None
        self.watermark: Optional[ActionLogWatermark] = None

    async def __aenter__(self) -> AsyncActionLogStream:
        try:
            self._ws = await _async_connect(self._url, additional_headers=self._headers)
        except InvalidStatus as exc:
            _raise_ws_error(exc)
        return self

    async def __aexit__(self, *exc: object) -> None:
        if self._ws is not None:
            await self._ws.close()

    def __aiter__(self) -> AsyncIterator[ActionLogEntry]:
        return self._iterate()

    async def _iterate(self) -> AsyncIterator[ActionLogEntry]:
        assert self._ws is not None
        async for message in self._ws:
            page = ActionLogPage.model_validate_json(message)
            if page.watermark is not None:
                self.watermark = page.watermark
            for entry in page.items:
                yield entry


class ActionLog:
    def __init__(self, token: str, *, base_url: str = CLOUD_BASE) -> None:
        self._url = _ws_url(base_url)
        self._headers = {'X-Octo-Api-Token': token}

    def stream(
        self, *, from_timestamp: Optional[int] = None, after_uuid: Optional[str] = None
    ) -> ActionLogStream:
        return ActionLogStream(
            _with_params(self._url, from_timestamp, after_uuid), self._headers
        )


class AsyncActionLog:
    def __init__(self, token: str, *, base_url: str = CLOUD_BASE) -> None:
        self._url = _ws_url(base_url)
        self._headers = {'X-Octo-Api-Token': token}

    def stream(
        self, *, from_timestamp: Optional[int] = None, after_uuid: Optional[str] = None
    ) -> AsyncActionLogStream:
        return AsyncActionLogStream(
            _with_params(self._url, from_timestamp, after_uuid), self._headers
        )

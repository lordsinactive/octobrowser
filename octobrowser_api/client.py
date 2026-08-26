from __future__ import annotations

from typing import Any

from ._transport import (
    CLOUD_BASE,
    DEFAULT_TIMEOUT,
    LOCAL_BASE,
    LOCAL_TIMEOUT,
    AsyncTransport,
    Transport,
)
from .action_log import ActionLog, AsyncActionLog
from .resources import (
    AsyncExtensions,
    AsyncFingerprints,
    AsyncFolders,
    AsyncInvites,
    AsyncLocal,
    AsyncProfiles,
    AsyncProxies,
    AsyncSubaccounts,
    AsyncTags,
    Extensions,
    Fingerprints,
    Folders,
    Invites,
    Local,
    Profiles,
    Proxies,
    Subaccounts,
    Tags,
)


class OctoClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = CLOUD_BASE,
        local_base_url: str = LOCAL_BASE,
        timeout: float = DEFAULT_TIMEOUT,
        local_timeout: float = LOCAL_TIMEOUT,
        wait_on_rate_limit: bool = False,
    ) -> None:
        self._transport = Transport(
            base_url,
            token=token,
            timeout=timeout,
            wait_on_rate_limit=wait_on_rate_limit,
        )
        self._local_transport = Transport(local_base_url, timeout=local_timeout)
        self.profiles = Profiles(self._transport)
        self.proxies = Proxies(self._transport)
        self.tags = Tags(self._transport)
        self.folders = Folders(self._transport)
        self.extensions = Extensions(self._transport)
        self.subaccounts = Subaccounts(self._transport)
        self.invites = Invites(self._transport)
        self.fingerprints = Fingerprints(self._transport)
        self.local = Local(self._local_transport)
        self.action_log = ActionLog(token, base_url=base_url)

    def close(self) -> None:
        self._transport.close()
        self._local_transport.close()

    def __enter__(self) -> OctoClient:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


class AsyncOctoClient:
    def __init__(
        self,
        token: str,
        *,
        base_url: str = CLOUD_BASE,
        local_base_url: str = LOCAL_BASE,
        timeout: float = DEFAULT_TIMEOUT,
        local_timeout: float = LOCAL_TIMEOUT,
        wait_on_rate_limit: bool = False,
    ) -> None:
        self._transport = AsyncTransport(
            base_url,
            token=token,
            timeout=timeout,
            wait_on_rate_limit=wait_on_rate_limit,
        )
        self._local_transport = AsyncTransport(local_base_url, timeout=local_timeout)
        self.profiles = AsyncProfiles(self._transport)
        self.proxies = AsyncProxies(self._transport)
        self.tags = AsyncTags(self._transport)
        self.folders = AsyncFolders(self._transport)
        self.extensions = AsyncExtensions(self._transport)
        self.subaccounts = AsyncSubaccounts(self._transport)
        self.invites = AsyncInvites(self._transport)
        self.fingerprints = AsyncFingerprints(self._transport)
        self.local = AsyncLocal(self._local_transport)
        self.action_log = AsyncActionLog(token, base_url=base_url)

    async def aclose(self) -> None:
        await self._transport.aclose()
        await self._local_transport.aclose()

    async def __aenter__(self) -> AsyncOctoClient:
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.aclose()

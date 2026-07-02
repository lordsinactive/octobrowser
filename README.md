# octobrowser

Полностью типизированный **синхронный и асинхронный** Python SDK для API автоматизации [Octo Browser](https://octobrowser.net/).

Управляйте антидетект-профилями, прокси, тегами, фингерпринтами, участниками команды и расширениями прямо из Python — а также запускайте и останавливайте локальные браузеры и получайте журнал действий команды в реальном времени.

> Неофициальный клиент. Не связан с Octo Browser.

---

## Возможности

- **Синхронный и асинхронный** клиенты с идентичным API (`OctoClient` / `AsyncOctoClient`).
- **Два транспорта в одном клиенте** — облачное **Cloud API** (`app.octobrowser.net`) и **Local API** (`localhost:58888`) для управления десктопным приложением.
- **Сквозная типизация** — модели [Pydantic v2](https://docs.pydantic.dev/) для каждого запроса и ответа, `StrEnum`/`IntEnum` для всех перечислений и маркер `py.typed`.
- **Удобные запросы** — передавайте типизированную модель *или* именованные аргументы; SDK сам соберёт тело запроса.
- **Структурированные исключения** — HTTP-коды и коды ошибок Octo сопоставлены с иерархией исключений.
- **Автоматическая обработка rate limit** — включается флагом `wait_on_rate_limit=True` (учитывает заголовок `Retry-After`).
- **Журнал действий в реальном времени** — итерация по журналу через WebSocket, синхронно и асинхронно.

---

## Требования

- Python **3.12+**
- **API-токен** Octo Browser (для Cloud API) — берётся в аккаунте Octo Browser.
- Запущенное **десктопное приложение Octo Browser** (только для ресурса `local` / запуска браузеров).

## Установка

```bash
pip install octobrowser
```

Или через [uv](https://docs.astral.sh/uv/):

```bash
uv add octobrowser
```

---

## Быстрый старт

### Синхронно

```python
from octobrowser import OctoClient

with OctoClient(token="ВАШ_API_ТОКЕН") as octo:
    # Создание профиля (через именованные аргументы — модель ProfileCreate соберётся сама)
    profile = octo.profiles.create(
        title="Мой первый профиль",
        fingerprint={"os": "win"},
        tags=["research"],
    )
    print(profile.uuid)

    # Список профилей
    for p in octo.profiles.list(page_len=50):
        print(p.uuid, p.title)

    # Запуск в локальном приложении и получение CDP-эндпоинта
    browser = octo.local.start(profile.uuid, headless=False, debug_port=True)
    print("Подключайте Playwright/Selenium к:", browser.ws_endpoint)

    octo.local.stop(profile.uuid)
```

### Асинхронно

```python
import asyncio
from octobrowser import AsyncOctoClient

async def main():
    async with AsyncOctoClient(token="ВАШ_API_ТОКЕН") as octo:
        profiles = await octo.profiles.list()
        print(len(profiles), "профилей")

asyncio.run(main())
```

### Управление браузером через Playwright

`local.start(...)` возвращает объект `Browser`, у которого `ws_endpoint` — это CDP-WebSocket, который можно передать в любую библиотеку автоматизации:

```python
from octobrowser import OctoClient
from playwright.sync_api import sync_playwright

with OctoClient(token="ВАШ_API_ТОКЕН") as octo:
    browser = octo.local.start(profile_uuid, debug_port=True)
    with sync_playwright() as pw:
        chromium = pw.chromium.connect_over_cdp(browser.ws_endpoint)
        page = chromium.contexts[0].pages[0]
        page.goto("https://whoer.net")
        ...
    octo.local.stop(profile_uuid)
```

---

## Создание профилей

Метод `profiles.create(...)` можно вызывать тремя способами. Все примеры ниже проверены на боевом API.

### 1. Минимально, именованными аргументами

Фингерпринт можно передать обычным словарём — обязателен только ключ `os`:

```python
profile = octo.profiles.create(
    title="Мой профиль",
    fingerprint={"os": "win"},
)
```

### 2. Подробно, именованными аргументами

Полный набор часто используемых полей. Фингерпринт удобно собрать типизированной моделью `Fingerprint`:

```python
from octobrowser.models import Fingerprint
from octobrowser.enums import OS, WindowsVersion

profile = octo.profiles.create(
    title="Профиль для рисёрча",
    fingerprint=Fingerprint(
        os=OS.WIN,
        os_version=WindowsVersion.V11,
        cpu=8,               # ядер CPU
        ram=16,              # ГБ RAM
    ),
    description="Создан из именованных аргументов",
    tags=["research", "qa"],           # имена тегов
    start_pages=["https://example.com"],
    images_load_limit=0,               # 0 = не ограничивать загрузку картинок
    local_cache=True,
)
print(profile.uuid)
```

### 3. Через модель `ProfileCreate`

Тот же результат, но весь запрос собирается одной типизированной моделью — удобно, когда конфиг профиля формируется заранее и переиспользуется:

```python
from octobrowser.models import ProfileCreate, Fingerprint, StorageOptions, Bookmark
from octobrowser.enums import OS, WindowsVersion, CPUCores, RAMSize

config = ProfileCreate(
    title="Профиль из модели",
    fingerprint=Fingerprint(
        os=OS.WIN,
        os_version=WindowsVersion.V11,
        cpu=CPUCores.CORES_8,   # то же, что cpu=8
        ram=RAMSize.GB_16,      # то же, что ram=16
    ),
    description="Создан из модели ProfileCreate",
    tags=["automation"],
    start_pages=["https://whoer.net"],
    storage_options=StorageOptions(passwords=False, history=True),
    bookmarks=[Bookmark(name="Octo", url="https://octobrowser.net")],
)

profile = octo.profiles.create(config)
print(profile.uuid)
```

> Весь фингерпринт можно собрать на типизированных enum-ах — не нужно помнить допустимые числа и строки. `cpu` принимает `CPUCores` (значения `2, 4, 6, 8, 10, 11, 12, 14, 16, 20, 24`), `ram` — `RAMSize` (`2, 4, 8, 12, 16, 24, 32, 64`). Аналогично типизированы `os` (`OS`), `os_version` (`WindowsVersion` / `MacOSVersion` / `AndroidVersion`), `os_arch` (`Arch`), `device_type` (`DeviceType`) и режимы `IPMode` / `WebRTCMode`. Enum-значение и «сырое» число/строка взаимозаменяемы (`cpu=CPUCores.CORES_8` ≡ `cpu=8`).

> Модели и dict можно смешивать: любое вложенное поле (`fingerprint`, `proxy`, `storage_options`, `bookmarks`, …) принимает как типизированную модель, так и обычный словарь.

---

## Настройка клиента

```python
OctoClient(
    token: str,
    *,
    base_url: str = "https://app.octobrowser.net/api/v2/automation",
    timeout: float = 30.0,
    wait_on_rate_limit: bool = False,
)
```

| Аргумент             | Описание                                                                            |
| -------------------- | ----------------------------------------------------------------------------------- |
| `token`              | API-токен Octo Browser, отправляется в заголовке `X-Octo-Api-Token`.                |
| `base_url`           | Переопределение базового URL Cloud API (например, для тестов).                       |
| `timeout`            | Таймаут запроса Cloud API в секундах. Для Local API используется 120 с.             |
| `wait_on_rate_limit` | Если `True`, при HTTP 429 клиент ждёт `Retry-After` секунд и повторяет запрос.       |

Оба клиента — контекстные менеджеры. Вне блока `with` вызывайте `octo.close()` (sync) или `await octo.aclose()` (async), чтобы освободить соединения.

---

## Ресурсы

Клиент предоставляет по одному атрибуту на ресурс. Каждый метод есть и в синхронном, и в асинхронном клиенте (асинхронная версия — `await`, класс с префиксом `Async`).

### `profiles` — управление облачными профилями

| Метод | Описание |
| ----- | -------- |
| `list(*, fields=, search=, search_tags=, page_len=, page=)` | Список профилей (пагинация, поиск). |
| `get(uuid)` | Получить один профиль. |
| `create(data \| **fields)` | Создать профиль из модели `ProfileCreate` или именованных аргументов. |
| `update(uuid, data \| **fields)` | Обновить профиль. |
| `delete(uuids, *, skip_trash_bin=True)` | Удалить профили по списку UUID. |
| `import_cookies(uuid, cookies)` | Импорт cookies (список словарей или строк в формате Netscape). |
| `force_stop(uuid, version)` | Принудительно остановить один запущенный профиль. |
| `force_stop_many(uuids)` | Принудительно остановить несколько профилей. |
| `set_password(uuids, password, *, old_password=None)` | Установить пароль профиля. |
| `clear_password(uuid, password)` | Снять пароль профиля. |
| `transfer(uuids, receiver_email, *, transfer_proxy=False)` | Передать профили на другой аккаунт. |
| `export(uuids, *, export_proxy=False, app_version=None)` | Запустить экспорт профилей. |
| `exports(*, page=, page_len=)` | Список прошлых экспортов. |
| `get_export(uuid)` | Получить один экспорт. |
| `import_(data)` | Импорт профилей из файлов экспорта. |

> Пагинация: `page_len` принимает только `10`, `25`, `50` или `100`; `page` начинается с `0`.

### `local` — локальное десктопное приложение (localhost:58888)

| Метод | Описание |
| ----- | -------- |
| `active()` | Список запущенных браузеров. |
| `version()` | Версия приложения / информация об обновлении. |
| `username()` | Имя вошедшего аккаунта. |
| `start(uuid \| data, *, headless=, debug_port=, flags=, only_local=, timeout=, password=)` | Запустить профиль; возвращает `Browser` с `ws_endpoint`. |
| `start_one_time(profile_data \| data, *, headless=, debug_port=, flags=, timeout=)` | Запустить временный (несохранённый) профиль. |
| `stop(uuid)` / `force_stop(uuid)` | Остановить / принудительно остановить профиль. |
| `set_password(uuid, password)` / `clear_password(uuid, password)` | Управление локальным паролем профиля. |
| `login(email, password)` / `logout()` | Аутентификация десктопного приложения. |

### `proxies`

`list()` · `create(...)` · `update(uuid, ...)` · `delete(uuid)`

### `tags`

`list()` · `create(name=, color=)` · `update(uuid, ...)` · `delete(uuid)`

### `fingerprints`

`renderers(*, os=, os_arch=, ...)` · `screens(*, os=, os_arch=)` · `device_models(*, device_type=)` — перечисление допустимых значений фингерпринта (WebGL-рендереры, разрешения экрана, модели устройств).

### `extensions`

`list(*, start=, limit=)` · `delete(uuids)`

### `subaccounts` / `invites` — управление командой

`subaccounts`: `list()` · `create(email=, permissions=)` · `update(email=, permissions=)` · `delete(email)`
`invites`: `list()` · `delete(receiver)`

---

## Работа с фингерпринтами

Фингерпринты строго типизированы. Передавайте модель `Fingerprint` или обычный словарь:

```python
from octobrowser import OctoClient
from octobrowser.models import Fingerprint
from octobrowser.enums import OS, WindowsVersion

with OctoClient(token="...") as octo:
    fp = Fingerprint(os=OS.WIN, os_version=WindowsVersion.V11, cpu=8, ram=16)
    profile = octo.profiles.create(title="Типизированный FP", fingerprint=fp)
```

Узнать допустимые значения рендереров / экранов / устройств перед сборкой фингерпринта:

```python
renderers = octo.fingerprints.renderers(os="win")
screens = octo.fingerprints.screens(os="win")
```

---

## Стриминг журнала действий

Журнал действий команды приходит по WebSocket как итерируемый поток объектов `ActionLogEntry`:

```python
from octobrowser import OctoClient

with OctoClient(token="...") as octo:
    with octo.action_log.stream() as stream:
        for entry in stream:
            print(entry)
            # `stream.watermark` хранит последнюю обработанную позицию для возобновления
```

Асинхронно:

```python
async with AsyncOctoClient(token="...") as octo:
    async with octo.action_log.stream(from_timestamp=...) as stream:
        async for entry in stream:
            print(entry)
```

Возобновить с нужного места можно через `from_timestamp=` / `after_uuid=`.

---

## Обработка ошибок

Все ошибки наследуются от `OctoError`. Ошибки API содержат `status_code`, `code`, `message`, `body` и исходный `response`.

```python
from octobrowser import OctoClient
from octobrowser.exceptions import (
    OctoError,          # базовый класс всех ошибок
    OctoAPIError,       # базовый класс всех ошибок API (HTTP)
    AuthError,          # 401 / неверный токен
    ForbiddenError,     # 403 / нет прав
    NotFoundError,      # 404
    ConflictError,      # 409 / уже запущен, уже существует, ...
    InvalidRequestError,# 422 / ошибка валидации
    LimitReachedError,  # лимиты тарифа / токенов / прокси
    SubscriptionError,  # неактивная подписка
    RateLimitError,     # 429 (содержит .retry_after)
)

with OctoClient(token="...") as octo:
    try:
        octo.profiles.get("does-not-exist")
    except NotFoundError as exc:
        print(exc.status_code, exc.code, exc.message)
    except RateLimitError as exc:
        print("Повтор через", exc.retry_after, "секунд")
```

Ошибки классифицируются сначала по полю `code` от Octo, затем по HTTP-статусу.

---

## Лицензия

[MIT](LICENSE) © lordsinactive

"""Adapters: framework-agnostic interfaces for config and logging."""

from typing import Protocol, Any, Optional, Mapping

class Logger(Protocol):
    def debug(self, msg: str, **kwargs: Any) -> None: ...
    def info(self, msg: str, **kwargs: Any) -> None: ...
    def warning(self, msg: str, **kwargs: Any) -> None: ...
    def error(self, msg: str, **kwargs: Any) -> None: ...
    def exception(self, msg: str, **kwargs: Any) -> None: ...

class NoopLogger:
    def debug(self, *a, **k): pass
    def info(self, *a, **k): pass
    def warning(self, *a, **k): pass
    def error(self, *a, **k): pass
    def exception(self, *a, **k): pass

class Config(Protocol):
    def get(self, key: str, default: Optional[str]=None) -> Optional[str]: ...

class EnvConfig:
    def __init__(self, extra: Optional[Mapping[str,str]]=None):
        import os
        self._env = dict(os.environ)
        if extra: self._env.update(extra)
    def get(self, key: str, default: Optional[str]=None) -> Optional[str]:
        return self._env.get(key, default)

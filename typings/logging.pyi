from typing import Any

WARNING: int
INFO: int
CRITICAL: int
ERROR: int
NOTSET: int
DEBUG: int

def info(*args, **kwargs) -> Any: ...
def getLogger(*args, **kwargs) -> Any: ...
def basicConfig(*args, **kwargs) -> Any: ...
def debug(*args, **kwargs) -> Any: ...

class Logger:
    level: int
    def error(self, *args, **kwargs) -> Any: ...
    def warning(self, *args, **kwargs) -> Any: ...
    def setLevel(self, *args, **kwargs) -> Any: ...
    def isEnabledFor(self, *args, **kwargs) -> Any: ...
    def critical(self, *args, **kwargs) -> Any: ...
    def debug(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def log(self, *args, **kwargs) -> Any: ...
    def exception(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

import sys

# FROM: https://github.com/josephcopenhaver/flock/blob/main/flock/__init__.py
__platform = sys.platform
match __platform:
    case "darwin":
        from ._bsd import Flock
    case "win32" | "cygwin" | "msys":
        from ._win32 import Flock
    case _:
        if __platform.startswith("linux"):
            from ._unix import Flock
        elif __platform.startswith("freebsd"):
            from ._bsd import Flock
        else:
            raise ImportError("unknown platform: " + __platform)
del __platform

__all__ = ["Flock"]

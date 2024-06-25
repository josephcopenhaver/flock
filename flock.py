import sys

match sys.platform:
    case "darwin":
        from platforms._bsd import Flock
    case "win32"|"cygwin"|"msys":
        from platforms._win32 import Flock
    case _:
        if sys.platform.startswith("linux"):
            from platforms._unix import Flock
        elif sys.platform.startswith("freebsd"):
            from platforms._bsd import Flock
        else:
            raise ImportError("unknown platform: "+sys.platform)

__all__ = ["Flock"]

def __dir__():
    return [x for x in __all__]

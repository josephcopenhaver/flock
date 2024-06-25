import os
import typing

# FROM: https://github.com/josephcopenhaver/flock/blob/main/platforms/_unix.py
class Flock():
    _type: str = "unix"

    _fd: int|None = None

    def __init__(self, filePath: str):
        fd = os.open(filePath, os.O_RDWR | os.O_CREAT | os.O_NONBLOCK, 0o600)
        try:
            os.lockf(fd, os.F_LOCK, 0)
        except OSError:
            os.close(fd)
            raise
        self._fd = fd

    def __enter__(self):
        return self

    def __exit__(self, *args: typing.Any):
        self.close()

    def close(self):
        fd = self._fd
        if fd is None:
            return
        self._fd = None
        try:
            os.lockf(fd, os.F_ULOCK, 0)
        finally:
            os.close(fd)

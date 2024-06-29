import msvcrt
import os
import typing


# FROM: https://github.com/josephcopenhaver/flock/blob/main/flock/_win32.py
class Flock:
    _type: str = "win32"

    _fd: int | None = None

    def __init__(self, filePath: str):
        fd = os.open(filePath, os.O_RDWR | os.O_CREAT, 0o600)
        try:
            msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)
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
            msvcrt.locking(fd, msvcrt.LK_UNLCK, 1)
        finally:
            os.close(fd)

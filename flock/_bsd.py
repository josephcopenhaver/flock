import os
import typing


# FROM: https://github.com/josephcopenhaver/flock/blob/main/flock/_bsd.py
class Flock:
    _type: str = "bsd"

    _fd: int | None = None

    def __init__(self, filePath: str):
        self._fd = os.open(
            filePath, os.O_RDWR | os.O_CREAT | os.O_NONBLOCK | os.O_EXLOCK, 0o600
        )

    def __enter__(self):
        return self

    def __exit__(self, *args: typing.Any):
        self.close()

    def close(self):
        fd = self._fd
        if fd is None:
            return
        self._fd = None
        os.close(fd)

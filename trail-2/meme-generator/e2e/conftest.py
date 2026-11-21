"""Starts a real uvicorn process on an OS-assigned port; tests talk to it over HTTP only."""

import socket
import subprocess
import sys
import time
from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="session")
def base_url() -> Iterator[str]:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    sock.listen()
    port = sock.getsockname()[1]
    server = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "meme_generator.app:app", "--fd", str(sock.fileno())],
        pass_fds=[sock.fileno()],
    )
    url = f"http://127.0.0.1:{port}"
    try:
        deadline = time.monotonic() + 15
        while True:
            try:
                if httpx.get(f"{url}/health").status_code == 200:
                    break
            except httpx.TransportError:
                pass
            if server.poll() is not None or time.monotonic() > deadline:
                raise RuntimeError("server did not start")
            time.sleep(0.1)
        yield url
    finally:
        server.terminate()
        server.wait(timeout=10)
        sock.close()


@pytest.fixture(scope="session")
def client(base_url: str) -> Iterator[httpx.Client]:
    with httpx.Client(base_url=base_url, timeout=30) as http:
        yield http


@pytest.fixture
def jpeg() -> bytes:
    return (FIXTURES / "gradient-800x600.jpg").read_bytes()

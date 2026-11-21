"""Starts a real uvicorn process on a free port; tests talk to it over HTTP or through a browser."""

import socket
import subprocess
import sys
import time
from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest

FIXTURES = Path(__file__).parent / "fixtures"


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


@pytest.fixture(scope="session")
def base_url() -> Iterator[str]:
    """Also pytest-playwright's base URL, so `page.goto("/")` opens this server."""
    port = free_port()
    server = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "meme_generator.app:app", "--port", str(port)]
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


@pytest.fixture(scope="session")
def client(base_url: str) -> Iterator[httpx.Client]:
    with httpx.Client(base_url=base_url, timeout=30) as http:
        yield http


@pytest.fixture
def jpeg_path() -> Path:
    return FIXTURES / "gradient-800x600.jpg"


@pytest.fixture
def jpeg(jpeg_path: Path) -> bytes:
    return jpeg_path.read_bytes()

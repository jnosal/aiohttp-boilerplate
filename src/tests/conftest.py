import pytest

from ..app import init_app


@pytest.fixture
def test_client(loop, aiohttp_client):
    app = init_app()
    return loop.run_until_complete(aiohttp_client(app))

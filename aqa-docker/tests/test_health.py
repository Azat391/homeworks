import os

import pytest
import requests


def get_base_url() -> str:
    value = os.getenv("BASE_URL", "http://127.0.0.1:8000").strip()
    if not value:
        raise RuntimeError("Переменная BASE_URL не должна быть пустой")
    return value.rstrip("/")


@pytest.mark.api
def test_api_is_available():
    response = requests.get(
        f"{get_base_url()}/ping",
        timeout=5,
    )

    assert response.status_code == 201, response.text

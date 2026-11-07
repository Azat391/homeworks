import os

import pytest

@pytest.mark.auth
def test_training_token_is_available():
    # Проверяем, что переменная окружения существует и не пустая
    assert os.getenv("API_TOKEN", "").strip()

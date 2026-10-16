import pytest
import sys
call_log=[]
@pytest.fixture
def translation_data():
    call_log.append(1)
    return call_log
def test_one(translation_data):
    assert translation_data
def test_two(translation_data):
    assert translation_data
    
@pytest.fixture(scope='session')
def db_connection():
    call_log.append(1)
    return call_log
def test_users(db_connection):
    assert db_connection
def test_products(db_connection):
    assert len(db_connection)==3 #С удивлением обнаружил что def translation_data() оказывается не очищает словарь после завершения теста

@pytest.fixture(scope='module')
def config_data():
    return {
    "env": "test",
}

class TestAPI:
    @pytest.fixture(scope='class')
    def api_client(self):
        return "live_client"

# ИСПРАВЬТЕ SCOPE В ЭТОЙ ФИКСТУРЕ
@pytest.fixture
def shopping_cart():
    return []  # Возвращаем изменяемый список


def test_add_item(shopping_cart):
    shopping_cart.append("apple")

    assert "apple" in shopping_cart


def test_cart_is_initially_empty(shopping_cart):
    # Этот тест упадет, если scope="session",
    # так как в корзине уже будет "apple"
    assert len(shopping_cart) == 0

import pytest
from pages.home_page import HomePage
@pytest.fixture
def home_page(page):
    home_page=HomePage(page)
    home_page.open()
    return home_page
@pytest.fixture
def account_page(home_page):
    def _account_page(name=str('Hermoine Granger')):
        customer_login_page=home_page.open_customer_login()
        return customer_login_page.login_as(name)
    return _account_page


import pytest, playwright
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from data import BOOKS, BookData

@pytest.fixture
def home_page(page):
    home_page = HomePage(page)
    home_page.open()
    return home_page

@pytest.fixture
def get_book():
    def _get(key: str) -> BookData:
        return BookData(**BOOKS[key])
    return _get
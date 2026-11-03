import allure
import pytest
from data import BOOKS, BookData
from pages.header import Header
from pages.home_page import HomePage


@pytest.fixture
@allure.step("Перейти на главную страницу")
def home_page(page):
    home_page = HomePage(page)
    return home_page.open()


@pytest.fixture
@allure.step("Используем элементы управления в шапке страницы")
def header(page):
    return Header(page)


@pytest.fixture
def get_book():
    @allure.step("Используем в тесте книгу: {key}")
    def _get(key: str) -> BookData:
        return BookData(**BOOKS[key])

    return _get


@pytest.fixture
def add_to_cart_books(home_page, header, get_book):
    @allure.step("Добавить в корзину книгу {name_book}")
    def add_to_cart_one_book(name_book):
        book = get_book(name_book)
        search_page = header.search_book(book.search_input)
        card = search_page.find_book(book.title, book.author, book.format)
        book_page = card.open_book()
        book_page.add_to_cart()
        return book

    return add_to_cart_one_book

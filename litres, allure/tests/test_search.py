import allure
import pytest
from playwright.sync_api import expect


@allure.epic("Литрес")
@allure.feature("Поиск")
@allure.story("Поиск одной книги")
@allure.title("Открытие книги из поиска: {title}")
@allure.description(""" Предусловие: главная открыта, есть данные книги main_text.
Действия: поиск → открыть книгу из выдачи.
Проверка: в поле поиска введённый запрос; на странице книги название и автор; URL совпадает.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "smoke", "search")
@pytest.mark.parametrize("title", ("main_text", "audiobook"))
def test_find_one_book(home_page, get_book, header, title):
    book = get_book(f"{title}")
    search_page = header.search_book(book.search_input)
    expect(header.search_input).to_have_value(book.search_input)
    card = search_page.find_book(book.title, book.author, book.format)
    book_page = card.open_book()
    with allure.step("Проверить название и автора книги"):
        expect(book_page.art_title).to_contain_text(book.title)
        expect(book_page.art_title).to_contain_text(book.author)
        assert book.url_part in book_page.url()


@allure.epic("Литрес")
@allure.feature("Поиск")
@allure.story("Исправление неудачного поиска")
@allure.title("Исправление неудачного поиска")
@allure.description("""Предусловие: главная открыта, есть данные книги main_text.
Действия: поиск «мусорного» запроса → проверка «ничего не найдено» → очистка поля → корректный запрос → открыть книгу.
Проверка: сообщение об отсутствии результатов, затем
 книга открывается с названием/автором/URL. """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "search")
def test_unlucky_search(home_page, get_book, header):
    book = get_book("main_text")
    search_page = header.search_book("fflsdmfkdmksdlmfdkfdlmkfdsmfsd")
    with allure.step("Поиск ничего не выдал, с ним можно в разведку идти"):
        expect(search_page.search_result).to_contain_text("ничего не найдено")
    search_page = header.clear_input_and_search_book(book.search_input)
    card = search_page.find_book(book.title, book.author, book.format)
    book_page = card.open_book()
    with allure.step("Проверить название и автора книги"):
        expect(book_page.art_title).to_contain_text(book.title)
        expect(book_page.art_title).to_contain_text(book.author)
        assert book.url_part in book_page.url()


@allure.epic("Литрес")
@allure.feature("Поиск")
@allure.story("Поиск нескольких книг")
@allure.title("Поиск двух книг из одной выдачи")
@allure.description(""" Предусловие: главная открыта, есть данные двух книг одного автора (main_text, second_text).
Действия: поиск по автору → открыть 1-ю книгу → назад → открыть 2-ю книгу.
Проверка: поле поиска сохраняет автора; обе книги корректны; URL книг различаются.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "search")
def test_find_two_books_in_one_search(home_page, get_book, header):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_page = header.search_book(book1.author)

    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url
    with allure.step("Проверить название и автора книги"):
        expect(book1_page.art_title).to_contain_text(book1.title)
        expect(book1_page.art_title).to_contain_text(book1.author)
    search_page = book1_page.go_back()
    expect(header.search_input).to_have_value(book1.author)
    card2 = search_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    url2 = book2_page.url
    with allure.step("Проверить название и автора книги"):
        expect(book2_page.art_title).to_contain_text(book2.title)
        expect(book2_page.art_title).to_contain_text(book2.author)
        assert url1 != url2

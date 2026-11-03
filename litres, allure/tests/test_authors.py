import allure
from playwright.sync_api import expect


@allure.epic("Литрес")
@allure.feature("Авторы")
@allure.story("Переход к автору и поиск другой книги")
@allure.title("Переход к автору книги и поиск другой книги того же авторв")
@allure.description("""Предусловие: две книги одного автора (main_text, second_text).
Действия: поиск → открыть 1-ю → к автору → открыть 2-ю книгу.
Проверка: страница автора открылась (заголовок проверяется через not_to_have_text); 2-я книга с названием/автором; URL различаются. """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "authors")
def test_to_author(home_page, get_book, header):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_page = header.search_book(book1.author)

    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()

    author_page = book1_page.go_to_author(book1.author)
    with allure.step("Имя автора совпадает с ожидаемым"):
        expect(author_page.author_title).to_contain_text(book1.author)
    card2 = author_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    url2 = book2_page.url()
    with allure.step("Название и автор книги 2 совпадает с ожидаемыми, книги разные"):
        expect(book2_page.art_title).to_contain_text(book2.title)
        expect(book2_page.art_title).to_contain_text(book2.author)
        assert url1 != url2


@allure.epic("Литрес")
@allure.feature("Авторы")
@allure.story("Поиск автора двумя маршрутами")
@allure.title("Поиск автора по двум маршрутама")
@allure.description(""" Предусловие: две книги одного автора.
Действия: открыть 1-ю → к автору (запомнить URL и имя) → открыть 2-ю → снова к автору (запомнить).
Проверка: URL автора по обоим маршрутам совпадает; имя совпадает; список книг автора виден.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "authors")
def test_find_author_in_double_way(home_page, get_book, header):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_page = header.search_book(book1.author)

    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()

    author1_page = book1_page.go_to_author(book1.author)
    url_author1, name_author1 = author1_page.url_and_name_author()

    card2 = author1_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    author2_page = book2_page.go_to_author(book2.author)
    url_author2, name_author2 = author2_page.url_and_name_author()
    assert url_author1 == url_author2
    assert name_author1 == name_author2
    expect(author2_page.books_list.first).to_be_visible()

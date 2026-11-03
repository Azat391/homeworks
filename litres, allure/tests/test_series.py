import allure
from playwright.sync_api import expect


@allure.epic("Литрес")
@allure.feature("Серии")
@allure.story("Переход к другой книге серии")
@allure.title("Переход к другой книге серии")
@allure.description("""Предусловие: есть данные двух книг одной серии (series_first, series_second).
Действия: поиск → открыть 1-ю книгу → перейти в серию → открыть 2-ю книгу.
Проверка: заголовок серии совпадает; URL книг различаются; у 2-й книги та же ссылка на серию. """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "series")
def test_go_to_another_book_in_series(home_page, get_book, header):
    book1 = get_book("series_first")
    book2 = get_book("series_second")
    search_page = header.search_book(book1.search_input)
    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()
    series_name = book1_page.series_link.inner_text()
    series_page = book1_page.go_to_series()
    with allure.step("Проверить, что открыта страница нужной серии"):
        expect(series_page.series_title).to_contain_text(series_name)
    card2 = series_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    url2 = book2_page.url()
    with allure.step("Проверить, что URL книг различаются"):
        assert url1 != url2
    with allure.step("Проверить, что у второй книги та же серия"):
        expect(book2_page.series_link).to_contain_text(series_name)


@allure.epic("Литрес")
@allure.feature("Серии")
@allure.story("Возврат к серии")
@allure.title("Возврат к серии из книги")
@allure.description(""" Предусловие: есть данные двух книг одной серии.
Действия: открыть 1-ю → в серию → открыть 2-ю → в серию → вернуться к 1-й через серию.
Проверка: название серии совпадает в обоих переходах; URL 1-й книги после возврата совпадает с исходным.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "series")
def test_back_to_the_series_from_the_book(home_page, get_book, header):
    book1 = get_book("series_first")
    book2 = get_book("series_second")
    search_page = header.search_book(book1.search_input)
    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()
    series1_page = book1_page.go_to_series()
    series1_name = series1_page.series_title.inner_text()
    card2 = series1_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    series2_page = book2_page.go_to_series()
    series2_name = series2_page.series_title.inner_text()
    with allure.step("Проверить, что название серии совпадает в обоих переходах"):
        assert series1_name == series2_name
    return_to_book1_page_card = series2_page.find_book(
        book1.title, book1.author, book1.format
    )
    return_to_book1_page = return_to_book1_page_card.open_book()
    url2 = return_to_book1_page.url()
    with allure.step(
        "Проверить, что URL первой книги после возврата совпадает с исходным"
    ):
        assert url1 == url2


@allure.epic("Литрес")
@allure.feature("Подборки")
@allure.story("Выбор книги из подборки")
@allure.title("Выбрать книгу из подборки")
@allure.description("""Предусловие: есть данные книги collection1 (включая название подборки).
Действия: раздел подборок → открыть нужную подборку → найти и открыть книгу.
Проверка: заголовок подборки; на книге название и автор; URL совпадает. """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "collection")
def test_select_book_from_collection(home_page, get_book, header):
    book = get_book("collection1")
    collection_page = header.go_to_collection()

    current_collection_page = collection_page.open_collection(book.collection)
    with allure.step("Проверить, что открыта нужная подборка"):
        expect(current_collection_page.collection_title).to_contain_text(
            book.collection
        )
    card = current_collection_page.find_book(book.title, book.author, book.format)
    book_page = card.open_book()
    with allure.step("Проверить название, автора и URL открытой книги"):
        expect(book_page.art_title).to_contain_text(book.title)
        expect(book_page.art_title).to_contain_text(book.author)
        assert book.url_part in book_page.url()
        allure.attach(
            book_page.page.screenshot(full_page=True),
            name="Карточка выбранного издания",
            attachment_type=allure.attachment_type.PNG,
        )


@allure.epic("Литрес")
@allure.feature("Подборки")
@allure.story("Просмотр нескольких книг из подборки")
@allure.title("Просмотр двух книг из подборки")
@allure.description("""Предусловие: есть данные двух книг одной подборки (collection1, collection2).
Действия: открыть подборку → открыть 1-ю книгу → назад в подборку → открыть 2-ю книгу.
Проверка: после возврата заголовок подборки соответствует 2-й книге; 2-я книга корректна; URL различаются. """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "collection")
def test_open_two_books_from_one_collection(home_page, get_book, header):
    book1 = get_book("collection1")
    book2 = get_book("collection2")
    collection_page = header.go_to_collection()
    current_collection_page = collection_page.open_collection(book1.collection)
    card1 = current_collection_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()
    expect(book1_page.art_title).to_contain_text(book1.title)
    current_collection_page = book1_page.go_back_to_collection()
    expect(current_collection_page.collection_title).to_contain_text(book2.collection)
    card2 = current_collection_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    url2 = book2_page.url()
    with allure.step("Проверить, что открыта вторая книга"):
        expect(book2_page.art_title).to_contain_text(book2.author)
    with allure.step("Проверить, что URL книг различаются"):
        assert url1 != url2


@allure.epic("Литрес")
@allure.feature("Жанры")
@allure.story("Переход из жанра к автору")
@allure.title("Переход из жанра к автору")
@allure.description(""" Предусловие: есть данные двух книг разных авторов из одного жанра (delegation, exploitation).
Действия: открыть жанр → открыть 1-ю книгу → к автору → открыть 2-ю книгу автора.
Проверка: заголовок жанра; автор 1-й книги; имя на странице автора; 2-я книга корректна; URL различаются.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "genre", "authors")
def test_way_from_genre_to_author(home_page, get_book, header):
    book1 = get_book("delegation")
    book2 = get_book("exploitation")
    genre_page = header.go_to_genre(book1.genre)
    expect(genre_page.genre_title).to_contain_text(book1.genre.lower())
    card1 = genre_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()
    expect(book1_page.art_title).to_contain_text(book1.author)
    author_page = book1_page.go_to_author(book1.author)
    with allure.step("Проверить, что на странице автора нужное имя"):
        expect(author_page.author_title).to_contain_text(book1.author)
        allure.attach(
            author_page.page.screenshot(full_page=True),
            name="Страница автора",
            attachment_type=allure.attachment_type.PNG,
        )
    card2 = author_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    with allure.step("Проверить, что открыта вторая книга автора"):
        expect(book2_page.art_title).to_contain_text(book2.author)
    url2 = book2_page.url()
    with allure.step("Проверить, что URL книг различаются"):
        assert url1 != url2

import allure
from playwright.sync_api import expect


@allure.epic("Литрес")
@allure.feature("Отзывы")
@allure.story("Просмотр отзывов и возврат к книге")
@allure.title("Прочитать отзывы и вернуться к выбору")
@allure.description(""" Предусловие: открыта главная, есть данные книги main_text.
Действия: поиск по автору → открыть книгу → отзывы → назад к книге → к автору.
Проверка: на отзывах есть название/автор и ≥1 отзыв; после возврата книга корректна, URL совпадает; на странице автора нужное имя.""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "reviews")
def test_read_review_and_return_to_search_book(home_page, get_book, header):
    book = get_book("main_text")
    search_page = header.search_book(book.author)

    card = search_page.find_book(book.title, book.author, book.format)
    book1_page = card.open_book()
    reviews_page = book1_page.go_to_reviews()
    with allure.step(
        "Отзывы относятся к выбранному произведению и есть один непкстой отзыв"
    ):
        expect(reviews_page.title_element).to_contain_text(book.title)
        expect(reviews_page.author_element).to_contain_text(book.author)
        assert reviews_page.lenght_one_review() > 0
    book2_page = reviews_page.go_back_to_book()
    with allure.step("После вовзрата страница книги не поменялась"):
        expect(book2_page.art_title).to_contain_text(book.title)
        expect(book2_page.art_title).to_contain_text(book.author)
        assert book.url_part in book2_page.url()
    author_page = book2_page.go_to_author(book.author)
    expect(author_page.author_title).to_contain_text(book.author)


@allure.epic("Литрес")
@allure.feature("Фрагмент и форматы")
@allure.story("Чтение фрагмента и возврат к книге")
@allure.title("Открыть текстовый фрагмент")
@allure.description(""" Предусловие: открыта главная Литрес, подготовлены данные книги 'main_text' (название, автор, формат, часть URL). Текстовый фрагмент доступен для этой книги.

Действия пользователя:
1. Поиск книги по имени автора.
2. В выдаче находится карточка (название + автор + формат) и открывается страница книги.
3. С карточки книги открывается текстовый фрагмент (render).
4. Из фрагмента пользователь возвращается к странице книги.

Ожидаемый результат:
- на странице текстового фрагмента заголовок содержит название книги и имя автора;
- после возврата страница книги снова показывает корректные название и автора;
- часть URL совпадает с ожидаемой для этой книги (тот же артефакт, что открывали).""")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "smoke", "render")
def test_read_render_and_return_to_book(home_page, get_book, header, page):
    book = get_book("main_text")
    search_page = header.search_book(book.author)

    card = search_page.find_book(book.title, book.author, book.format)
    book1_page = card.open_book()
    render_page = book1_page.go_to_render()
    # page.pause()
    with allure.step("Фрагмент относится к выбранному произведению"):
        expect(render_page.render_title).to_contain_text(book.title)
        expect(render_page.render_title).to_contain_text(book.author)
    book2_page = render_page.go_back_to_book()
    with allure.step("После вовзрата страница книги не поменялась"):
        expect(book2_page.art_title).to_contain_text(book.title)
        expect(book2_page.art_title).to_contain_text(book.author)
        assert book.url_part in book2_page.url()


# def test_start_player(home_page,get_book, header,page):
#     book=get_book('audiobook')
#     search_page=header.search_book(book.search_input)

#     card = search_page.find_book(book.title, book.author, book.format)
#     book_page = card.open_book()
#     assert book.url_part in book_page.url()
#     book_page.start_playback()
#     page.pause()
#     book_page.pause_playback()


#     author_page = book1_page.go_to_author()
#     expect(author_page.author_title).to_contain_text(book.author)
@allure.epic("Литрес")
@allure.feature("Фрагмент и форматы")
@allure.story("Переключение между текстовой и аудиоверсией")
@allure.title("Сравнение текстовой и аудио версии")
@allure.description("""Предусловие: открыта главная Литрес, подготовлены данные аудиокниги 'audiobook' (название, автор, формат, поисковый запрос). У книги есть и аудио-, и текстовая версия.

Действия пользователя:
1. Поиск книги по подготовленному поисковому запросу.
2. Из выдачи открывается карточка аудиокниги.
3. Проверяется кнопка «Слушать фрагмент» и корректность заголовка (название + автор).
4. Переключение на текстовую версию книги.
5. Проверка, что доступна кнопка чтения фрагмента (render).
6. Возврат к аудиоверсии.

Ожидаемый результат:
- на исходной аудиоверсии видна кнопка прослушивания фрагмента, заголовок содержит корректные название и автора;
- после переключения на текстовую версию доступна кнопка чтения фрагмента;
- после возврата на аудиоверсию заголовок снова содержит корректные название и автора (переключение версий не ломает карточку). """)
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("ui", "regression", "audio", "versions")
def test_way_to_text_audio_version(home_page, get_book, header, page):
    book = get_book("audiobook")
    search_page = header.search_book(book.search_input)

    card = search_page.find_book(book.title, book.author, book.format)
    book_page = card.open_book()
    with allure.step("Книга совпадает с желаемым и доустпна аудиоверсия"):
        expect(book_page.play_fragment_btn).to_be_visible()
        expect(book_page.art_title).to_contain_text(book.title)
        expect(book_page.art_title).to_contain_text(book.author)
    book_page.go_to_textversion()
    with allure.step("Доступна тестовая версия после перехода"):
        expect(book_page.render_button).to_be_visible()
    book_page.go_to_audioversion()
    expect(book_page.art_title).to_contain_text(book.title)
    expect(book_page.art_title).to_contain_text(book.author)

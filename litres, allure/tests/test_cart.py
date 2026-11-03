import allure
from playwright.sync_api import expect


@allure.epic("Литрес")
@allure.feature("Корзины")
@allure.story("Добавление одной книги")
@allure.title("Добавление одной книги в корзину")
@allure.description("""Предусловие (важно!): через фикстуру add_to_cart_books в корзину уже добавлена одна книга 'main_text'. К началу теста корзина содержит ровно одну книгу. Главная Литрес открыта.

Действия пользователя:
1. Переход в корзину из шапки.
2. Проверка, что в корзине отображается подготовленная книга.
3. Удаление этой книги из корзины.

Ожидаемый результат:
- в корзине есть карточка с названием подготовленной книги;
- после удаления отображается виджет «корзина пуста». """)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "regression", "smoke", "cart")
def test_add_one_book_to_cart(add_to_cart_books, header):
    book = add_to_cart_books("main_text")
    cart_page = header.go_to_cart()
    with allure.step("Книга находится в корзине"):
        expect(cart_page.find_book_in_cart(book.title)).to_contain_text(book.title)
    cart_page.delete_book_on_cart(book.title)
    with allure.step("Книга удалена из корзины"):
        expect(cart_page.empty_vidget).to_be_visible()


@allure.epic("Литрес")
@allure.feature("Корзины")
@allure.story("Добавление двух книги")
@allure.title("Добавление двух книг в корзину")
@allure.description(""" Предусловие (важно!): через фикстуру add_to_cart_books в корзину уже добавлены две книги — аудиокнига 'audiobook' и текстовая 'main_text'. Главная Литрес открыта.

Действия пользователя:
1. Переход в корзину.
2. Проверка, что в корзине одновременно обе подготовленные книги (аудио и текстовая).
3. Удаление сначала первой книги, затем второй.

Ожидаемый результат:
- обе книги видны в корзине одновременно;
- удаление проходит без ошибок для обеих книг.""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "regression", "cart")
def test_add_two_books_to_cart(header, add_to_cart_books):
    book1 = add_to_cart_books("second_text")
    cart_page = header.go_to_cart()
    with allure.step("Аудиокнига в корзине после первого добавления"):
        expect(cart_page.find_book_in_cart(book1.title)).to_contain_text(book1.title)
    book2 = add_to_cart_books("main_text")
    cart_page = header.go_to_cart()
    with allure.step("2 книги находится в корзине"):
        expect(cart_page.find_book_in_cart(book1.title)).to_contain_text(book1.title)
        expect(cart_page.find_book_in_cart(book2.title)).to_contain_text(book2.title)
    cart_page.delete_book_on_cart(book1.title)
    cart_page.reload()
    cart_page.delete_book_on_cart(book2.title)


@allure.epic("Литрес")
@allure.feature("Корзины")
@allure.story("Удаление одной книги")
@allure.title("Удаление одной книги сохраняет вторую в корзине")
@allure.description(""" Предусловие (важно!): через фикстуру add_to_cart_books в корзину уже добавлены две книги 'main_text' и 'audiobook'. Главная Литрес открыта.

Действия пользователя:
1. Переход в корзину.
2. Проверка, что в корзине обе книги.
3. Удаление первой книги (main_text).
4. Перезагрузка страницы корзины.
5. Повторная проверка содержимого корзины.

Ожидаемый результат:
- после удаления и перезагрузки в корзине нет первой книги;
- вторая книга (audiobook) остаётся в корзине.""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "regression", "cart")
def test_delete_one_book_from_cart(add_to_cart_books, header):
    book1 = add_to_cart_books("main_text")
    book2 = add_to_cart_books("second_text")
    cart_page = header.go_to_cart()
    with allure.step("2 книги находится в корзине"):
        expect(cart_page.find_book_in_cart(book1.title)).to_contain_text(book1.title)
        expect(cart_page.find_book_in_cart(book2.title)).to_contain_text(book2.title)
    cart_page.delete_book_on_cart(book1.title)

    cart_page.reload()

    with allure.step("Одна книга не находится, а другая находится в корзине"):
        expect(cart_page.cart_items).not_to_contain_text(book1.title)
        expect(cart_page.find_book_in_cart(book2.title)).to_contain_text(book2.title)
        allure.attach(
            cart_page.page.screenshot(full_page=True),
            name="Корзина после удаления книги",
            attachment_type=allure.attachment_type.PNG,
        )


@allure.epic("Литрес")
@allure.feature("Сквозные сценарии")
@allure.story("Полный сценарий с корзиной")
@allure.title("Полный сценарий")
@allure.description("""Предусловие (важно!): открыта главная Литрес, корзина пуста, подготовлены данные двух книг 'main_text' и 'second_text'.

Действия пользователя:
1. Поиск первой книги → открытие карточки.
2. Переход к отзывам и возврат к книге.
3. Переход к автору первой книги.
4. Со страницы автора открывается вторая книга.
5. Добавление второй книги в корзину → переход в корзину → проверка.
6. Повторный поиск первой книги → открытие → добавление в корзину.
7. Переход в корзину, проверка, что там обе книги.
8. Удаление второй книги, перезагрузка корзины.

Ожидаемый результат:
- на шагах 2–3 страницы книги и автора корректны, URL первой книги совпадает;
- обе книги успешно добавлены и видны в корзине одновременно;
- URL первой и второй книг различаются;
- после удаления второй книги и перезагрузки её нет в корзине, первая книга остаётся. """)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("ui", "regression", "cart", "e2e")
def test_full_scenatio(home_page, get_book, header):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_page = header.search_book(book1.search_input)
    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    reviews_page = book1_page.go_to_reviews()
    book1_page = reviews_page.go_back_to_book()
    with allure.step("Страница автора совпала с ожидаемым"):
        expect(book1_page.art_title).to_contain_text(book1.author)
        assert book1.url_part in book1_page.url()
    author_page = book1_page.go_to_author(book1.author)
    with allure.step(
        "План на тренировку на завтра: жим, тяга верхнего блока, бицепс, ноги чутка, на ход ноги чисто,  трицепс хуицепс и плечи"
    ):
        expect(author_page.author_title).to_contain_text(book1.author)
    card2 = author_page.find_book(book2.title, book2.author, book2.format)
    book2_page = card2.open_book()
    url2 = book2_page.url()
    book2_page.add_to_cart()
    cart_page = header.go_to_cart()
    with allure.step(
        "Если позволите, будьте любезны обратить внимание: после того как пользователь соблаговолил явно перейти на страницу корзины, и страница корзины, не сочтите за труд заметить, полностью загрузилась и отрисовалась, в списке товаров корзины, с присущей всякой осмотрительности точностью, присутствует ровно одна карточка товара, которая, как нетрудно убедиться, однозначно соответствует именно той книге, которую пользователь ранее соблаговолил добавить, — то есть содержит, если позволите так выразиться, корректное название этой книги, имя её автора и её формат (текстовая, аудио- или бумажная версия), — при этом виджет пустой корзины на странице, будьте любезны отметить, отсутствует, количество карточек товара в списке равно ожидаемому, а сама карточка, что особенно отрадно, остаётся в корзине и после перезагрузки страницы, что с должной степенью уверенности подтверждает: книга действительно сохранена в корзине пользователя, а не просто временно отображена в интерфейсе."
    ):
        expect(cart_page.find_book_in_cart(book2.title)).to_contain_text(book2.title)
    search_page = header.search_book(book1.search_input)
    card1 = search_page.find_book(book1.title, book1.author, book1.format)
    book1_page = card1.open_book()
    url1 = book1_page.url()
    assert url1 != url2
    book1_page.add_to_cart()
    cart_page = header.go_to_cart()
    with allure.step("Две книги содеражтся в корзине"):
        expect(cart_page.find_book_in_cart(book1.title)).to_contain_text(book1.title)
        expect(cart_page.find_book_in_cart(book2.title)).to_contain_text(book2.title)
    cart_page.delete_book_on_cart(book2.title)
    cart_page.reload()
    with allure.step("Татарстан - часть планеты, планета- часть Татарстана"):
        expect(cart_page.cart_items).not_to_contain_text(book2.title)
        expect(cart_page.find_book_in_cart(book1.title)).to_contain_text(book1.title)

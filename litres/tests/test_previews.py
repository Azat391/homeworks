from playwright.sync_api import expect


def test_reviews_page(home_page, get_book):
    book = get_book("main_text")
    search_result = home_page
    search_result = home_page.search(book.search_input)
    card = search_result.select_book(
        title=book.title, author=book.author, art=book.format
    )
    book1_page = card.open()
    book1_title = book1_page.title.inner_text()
    reviews_page = book1_page.open_reviews()
    expect(reviews_page.author_title).to_contain_text(book.author)
    assert len(reviews_page.return_one_review()) != 0
    book2_page = reviews_page.go_back()
    book2_title = book2_page.title.inner_text()
    assert book1_title == book2_title


def test_fragment(home_page, get_book, page):
    book = get_book("main_text")
    search_result = home_page
    search_result = home_page.search(book.search_input)
    card = search_result.select_book(
        title=book.title, author=book.author, art=book.format
    )
    book1_page = card.open()
    book1_title = book1_page.title.inner_text()
    render_page = book1_page.open_render()

    expect(render_page.text_book).to_contain_text(
        "В час жаркого весеннего заката на Патриарших "
    )
    book2_page = render_page.go_back_to_book()
    book2_title = book2_page.title.inner_text()
    assert book1_title == book2_title


# не работающая хуебесина
# def test_audio(home_page, get_book,page):
#     book=get_book('audiobook')
#     search_result=home_page.search(book.search_input)
#     card=search_result.select_book(title=book.title, author=book.author, art=book.format)
#     book_page=card.open()
#     assert book.url_part in book_page.url()

#     book_page.start_pause_player()
#     expect(book_page.player_pause).to_be_visible(timeout=10000)
#     book_page.start_pause_player()
#     expect(book_page.player_play).to_be_visible()
#     author_page=book_page.art_person(book.author)
#     expect(author_page.author_title).to_contain_text(book.author)


def test_text_audio_version(home_page, get_book):
    book = get_book("text_audio")
    search_result = home_page.search(book.search_input)
    card = search_result.select_book(
        title=book.title, author=book.author, art=book.format
    )
    book_page = card.open()
    book_text_title = book_page.title.inner_text()
    expect(book_page.text_button).to_contain_text("Читать фрагмент")
    book_page.go_to_audioversion()
    book_audio_title = book_page.title.inner_text()
    expect(book_page.audio_button).to_contain_text("Слушать фрагмент")
    assert book_text_title == book_audio_title

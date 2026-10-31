from playwright.sync_api import expect


def test_series_page(home_page, get_book, page):
    book1 = get_book("series_first")
    book2 = get_book("series_second")
    search_result1 = home_page.search(book1.search_input)
    card1 = search_result1.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    first_url = book1_page.url
    series_page = book1_page.open_series()
    expect(series_page.series_title).to_contain_text(series_page.series_name)

    card2 = series_page.find_book(
        title=book2.title, author=book2.author, art=book2.format
    )
    book2_page = card2.open()
    second_url = book2_page.url
    assert first_url != second_url
    expect(book2_page.title).to_contain_text(book2.title)
    expect(book2_page.author_details).to_contain_text(book2.author)
    assert book2.url_part in book2_page.url()
    expect(book2_page.series_link).to_contain_text(series_page.series_name)


def test_back_to_first_book(home_page, get_book):
    book1 = get_book("series_first")
    book2 = get_book("series_second")
    search_result1 = home_page.search(book1.search_input)
    card1 = search_result1.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    series1_page = book1_page.open_series()
    series1_name = series1_page.get_series_name()
    url1 = series1_page.get_series_url()
    card2 = series1_page.find_book(
        title=book2.title, author=book2.author, art=book2.format
    )
    book2_page = card2.open()
    series2_page = book2_page.open_series()
    series2_name = series2_page.get_series_name()
    url2 = series2_page.get_series_url()
    card1_reload = series2_page.find_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    assert series1_name == series2_name
    expect(card1_reload.card).to_be_visible()
    assert url1.split("?")[0] == url2.split("?")[0]


def test_collections_page(home_page, get_book):
    book = get_book("collection1")
    collection_page = home_page.open_collection()
    collection_page_current = collection_page.open_one_collections(book.collection)
    expect(collection_page.page_title).to_contain_text(book.collection)
    card = collection_page_current.find_book(
        title=book.title, author=book.author, art=book.format
    )
    expect(card.card).to_be_visible()
    book_page = card.open()
    expect(book_page.title).to_contain_text(book.title)
    expect(book_page.author_details).to_contain_text(book.author)
    assert book.url_part in book_page.url()


def test_double_collection_test(home_page, get_book):
    book1 = get_book("collection1")
    book2 = get_book("collection2")
    collection_page = home_page.open_collection()
    collection_page_current = collection_page.open_one_collections(book1.collection)
    card1 = collection_page_current.find_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    expect(book1_page.title).to_contain_text(book1.title)
    expect(book1_page.author_details).to_contain_text(book1.author)
    assert book1.url_part in book1_page.url()
    title_book1 = book1_page.title.inner_text()
    collection_page_current = book1_page.go_back_in_collection()
    expect(collection_page_current.page_title).to_contain_text(book1.collection)
    card2 = collection_page_current.find_book(
        title=book2.title, author=book2.author, art=book2.format
    )
    book2_page = card2.open()
    title_book2 = book2_page.title.inner_text()
    assert title_book1 != title_book2
    author2_page = book2_page.art_person(book2.author)
    _, author2 = author2_page.author_and_url()
    assert author2 == book2.author


def test_genres(home_page, get_book):
    book1 = get_book("delegation")
    book2 = get_book("exploitation")
    genres_page = home_page.open_genres(book1.genre)
    expect(genres_page.page_title).to_contain_text((book1.genre).lower())
    card1 = genres_page.find_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    expect(book1_page.title).to_contain_text(book1.title)
    expect(book1_page.author_details).to_contain_text(book1.author)
    url_book1 = book1_page.url()
    assert book1.url_part in book1_page.url()
    author1_page = book1_page.art_person(book1.author)
    card2 = author1_page.select_authors_book(title=book2.title, author=book2.author)
    expect(author1_page.author_title).to_contain_text(book2.author)
    book2_page = card2.open()
    url_book2 = book2_page.url()
    assert url_book1 != url_book2

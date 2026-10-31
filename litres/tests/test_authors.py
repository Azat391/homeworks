from playwright.sync_api import expect


def test_authors_book(home_page, get_book):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_result1 = home_page.search(book1.author)
    card1 = search_result1.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    main_url = book1_page.url()
    author_page = book1_page.art_person()
    expect(author_page.author_title).to_contain_text(book1.author)
    card2 = author_page.select_authors_book(title=book2.title, author=book2.author)
    book2_page = card2.open()
    expect(book2_page.title).to_contain_text(book2.title)
    expect(book2_page.author_details).to_contain_text(book2.author)
    second_url = book2_page.url()
    assert main_url != second_url


def test_double_way_author(home_page, get_book, page):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search_result1 = home_page.search(book1.author)
    card1 = search_result1.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()

    author1_page = book1_page.art_person()
    main_url, main_author = author1_page.author_and_url()
    card2 = author1_page.select_authors_book(title=book2.title, author=book2.author)
    book2_page = card2.open()
    author2_page = book2_page.art_person()
    second_url, second_author = author2_page.author_and_url()
    assert main_url == second_url and main_author == second_author
    page.pause()

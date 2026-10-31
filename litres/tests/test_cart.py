from playwright.sync_api import expect


def test_add_to_cart(home_page, get_book, page):
    book = get_book("text_audio")
    search_result = home_page.search(book.search_input)
    card = search_result.select_book(
        title=book.title, author=book.author, art=book.format
    )
    book_page = card.open()

    book_page.add_to_cart()

    cart_page = book_page.go_to_cart()
    expect(cart_page.cart_list).to_contain_text(book.title)
    expect(cart_page.cart_list).to_contain_text(book.format)

    cart_page.delete_book_on_cart(book.title)

    expect(cart_page.empty_vidget).to_be_visible()


def test_add_double_to_cart(home_page, get_book, page):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search1_result = home_page.search(book1.search_input)
    card1 = search1_result.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    book1_page.add_to_cart()

    search2_result = book1_page.search(book2.search_input)
    card2 = search2_result.select_book(
        title=book2.title, author=book2.author, art=book2.format
    )
    book2_page = card2.open()
    book2_page.add_to_cart()
    cart_page = book2_page.go_to_cart()
    expect(cart_page.cart_list).to_contain_text(book1.title)
    expect(cart_page.cart_list).to_contain_text(book1.format)
    expect(cart_page.cart_list).to_contain_text(book2.title)
    expect(cart_page.cart_list).to_contain_text(book2.format)
    cart_page.delete_book_on_cart(book1.title)
    cart_page.delete_book_on_cart(book2.title)
    expect(cart_page.empty_vidget).to_be_visible()


def test_delete_one_book(home_page, get_book):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search1_result = home_page.search(book1.search_input)
    card1 = search1_result.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    book1_page.add_to_cart()

    search2_result = book1_page.search(book2.search_input)
    card2 = search2_result.select_book(
        title=book2.title, author=book2.author, art=book2.format
    )
    book2_page = card2.open()
    book2_page.add_to_cart()
    cart_page = book2_page.go_to_cart()
    expect(cart_page.cart_list).to_contain_text(book1.title)
    expect(cart_page.cart_list).to_contain_text(book1.format)
    expect(cart_page.cart_list).to_contain_text(book2.title)
    expect(cart_page.cart_list).to_contain_text(book2.format)
    cart_page.delete_book_on_cart(book1.title)
    cart_page.reload()
    expect(cart_page.cart_items).to_contain_text(book2.title)
    expect(cart_page.cart_items).not_to_contain_text(book1.title)


def test_full_scenatio(home_page, get_book):
    book1 = get_book("main_text")
    book2 = get_book("second_text")
    search1_result = home_page.search(book1.search_input)
    card1 = search1_result.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    book1_title = book1_page.title.inner_text()
    reviews_page = book1_page.open_reviews()
    expect(reviews_page.author_title).to_contain_text(book1.author)
    assert len(reviews_page.return_one_review()) != 0
    book1_page = reviews_page.go_back()
    author_page = book1_page.art_person(book1.author)
    expect(author_page.author_title).to_contain_text(book1.author)
    card2 = author_page.select_authors_book(title=book2.title, author=book2.author)
    book2_page = card2.open()
    book2_title = book2_page.title.inner_text()
    assert book1_title != book2_title
    book2_page.add_to_cart()
    cart_page = book2_page.go_to_cart()
    expect(cart_page.cart_items).to_contain_text(book2.title)
    search1_result = cart_page.search(book1.search_input)
    card1 = search1_result.select_book(
        title=book1.title, author=book1.author, art=book1.format
    )
    book1_page = card1.open()
    book1_page.add_to_cart()
    cart_page = book1_page.go_to_cart()
    expect(cart_page.cart_list).to_contain_text(book1.title)
    expect(cart_page.cart_list).to_contain_text(book2.title)
    cart_page.delete_book_on_cart(book1.title)
    cart_page.reload()
    expect(cart_page.cart_list).to_contain_text(book2.title)
    expect(cart_page.cart_list).not_to_contain_text(book1.title)

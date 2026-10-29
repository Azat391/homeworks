import pytest, playwright
from playwright.sync_api import Page, expect

# def test_search(home_page,get_book):
#     book = get_book("audiobook")
#     search_result = home_page.search(book.search_input)
#     expect(search_result.search_input).to_have_value(book.search_input)

#     card = search_result.select_book(title=book.title, author=book.author, art=book.format)
#     book_page = card.open()

#     expect(book_page.title).to_contain_text(book.title)
#     expect(book_page.author_details).to_contain_text(book.author)
#     assert book.url_part in book_page.url()

# def test_undefined_search(home_page,get_book):
#     book = get_book("audiobook")
#     search_result_undefined=home_page.search('dfsfdssdfdsdfs')
#     expect(search_result_undefined.search_title).to_have_text('ничего не найдено')
#     search_result_undefined.clear
#     search_result=search_result_undefined.search(book.search_input)
#     expect(search_result.search_input).to_have_value(book.search_input)

#     card = search_result.select_book(title=book.title, author=book.author, art=book.format)
#     book_page = card.open()

#     expect(book_page.title).to_contain_text(book.title)
#     expect(book_page.author_details).to_contain_text(book.author)
#     assert book.url_part in book_page.url()
# def test_double_book(home_page, get_book):
#     book1=get_book('main_text')
#     book2=get_book('second_text')
#     search_result1=home_page.search(book1.author)
#     card1=search_result1.select_book(title=book1.title, author=book1.author, art=book1.format)
#     book1_page=card1.open()
#     main_url=book1_page.url()
#     search_result2=book1_page.go_back()
#     expect(search_result2.search_input).to_have_value(book1.author)
#     card2=search_result2.select_book(title=book2.title, author=book2.author, art=book2.format)
#     book2_page=card2.open()
#     expect(book2_page.title).to_contain_text(book2.title)
#     expect(book2_page.author_details).to_contain_text(book2.author)
#     second_url=book2_page.url()
#     assert main_url!=second_url

# test author
def test_authors_book(home_page, get_book):
    book1=get_book('main_text')
    book2=get_book('second_text')
    search_result1=home_page.search(book1.author)
    card1=search_result1.select_book(title=book1.title, author=book1.author, art=book1.format)
    book1_page=card1.open()
    main_url=book1_page.url()
    author_page=book1_page.art_person()
    expect(author_page.author_title).to_contain_text(book1.author)
    card2=author_page.select_authors_book(title=book2.title, author=book2.author)
    book2_page=card2.open()
    expect(book2_page.title).to_contain_text(book2.title)
    expect(book2_page.author_details).to_contain_text(book2.author)
    second_url=book2_page.url()
    assert main_url!=second_url


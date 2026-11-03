import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Найти книгу по названию:{title}, автору:{author} и формату:{format}")
    def find_book(self, title, author, format=None):
        from components.book_card import BookCard

        chat_btn = self.page.get_by_role("button", name="Открыть чат поддержки")
        if chat_btn.count() > 0:
            chat_btn.evaluate("el => el.remove()")
        card = self.books_list.filter(has_text=title).filter(has_text=author)
        if format:
            card = card.filter(has_text=format)
        return BookCard(self.page, card.first)

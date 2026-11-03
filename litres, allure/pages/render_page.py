import allure
from playwright.sync_api import Page


class RenderPage:
    def __init__(self, page: Page):
        self.page = page
        self.read_in_app_button = page.get_by_role("button", name="Закрыть")
        self.render_title = page.get_by_test_id("readOnline__text--wrapper")
        self.render_author = self.render_title.locator("div")

    @allure.step("Переход к странице книги")
    def go_back_to_book(self):
        from pages.book_page import BookPage

        self.page.go_back()
        return BookPage(self.page)

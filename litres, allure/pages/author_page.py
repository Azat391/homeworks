import allure
from pages.base_page import BasePage
from playwright.sync_api import Page


class AuthorPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.books_list = page.get_by_test_id(
            "popular__artsGreedSlider--block"
        ).get_by_test_id("slider__item")
        self.author_title = page.get_by_test_id("author__namePerson")

    @allure.step("Возврат урл страницы и имя автора")
    def url_and_name_author(self):
        return self.page.url, self.author_title.inner_text()

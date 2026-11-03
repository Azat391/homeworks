import allure
from pages.base_page import BasePage
from playwright.sync_api import Page


class CollectionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.collection_list = page.get_by_test_id("slider__block--titleText")
        self.books_list = page.get_by_test_id(
            "collection__content--wrapper"
        ).get_by_test_id("art__wrapper")
        self.collection_title = page.get_by_test_id("pageTitle")

    @allure.step("Открыть колекцию: {collection_name}")
    def open_collection(self, collection_name):
        self.collection_list.filter(has_text=collection_name).first.click()
        return self

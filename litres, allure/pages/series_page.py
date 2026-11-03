from pages.base_page import BasePage
from playwright.sync_api import Page


class SeriesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.books_list = page.get_by_test_id("series__arts--tile").get_by_test_id(
            "art__wrapper"
        )
        self.series_title = page.get_by_test_id("series__title--text")

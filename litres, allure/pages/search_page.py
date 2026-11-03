from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.books_list = page.get_by_test_id("art__wrapper")
        self.search_result = page.get_by_test_id("search-title__wrapper")

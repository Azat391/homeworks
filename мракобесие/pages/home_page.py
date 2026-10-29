import playwright
from playwright.sync_api import Page, expect
from pages.search_page import SearchPage
class HomePage:
    base_url='https://www.litres.ru/'
    def __init__(self, page: Page):
        self.page=page
        self.search_input=page.get_by_test_id('search__input')
        self.search_button=page.get_by_test_id('search__button')
    def open(self):
        self.page.goto(self.base_url)
    def search(self, query : str):
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        self.search_input.click()
        self.search_input.fill(query)

        self.search_button.click()
        return SearchPage(self.page)
        
    
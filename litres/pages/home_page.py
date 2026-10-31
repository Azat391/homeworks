from playwright.sync_api import Page

from pages.search_page import SearchPage


class HomePage:
    base_url = "https://www.litres.ru/"

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")

    def open(self):
        self.page.goto(self.base_url)

    def search(self, query: str):
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        self.search_input.click()
        self.search_input.fill(query)

        self.search_button.click()
        return SearchPage(self.page)

    def open_collection(self):
        from pages.collection_page import CollectionPage

        collection_button = self.page.get_by_test_id("lowerMenu__item--compilations")
        collection_button.click()
        return CollectionPage(self.page)

    def open_genres(self, genre):
        from pages.ganre_page import GenrePage

        self.page.get_by_test_id("header-catalog-button").click()
        self.page.get_by_role("link", name=genre, exact=True).click()
        return GenrePage(self.page)

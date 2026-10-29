import playwright
from playwright.sync_api import Page, expect
from components.book_card import BookCard
class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.art_filter = page.get_by_test_id('art__filters-art_types')
        self.search_title = page.get_by_test_id('search-title__wrapper')
        self.search_input = page.get_by_test_id('search__input')
        self.cards = page.get_by_test_id('art__wrapper')
        self.search_button=page.get_by_test_id('search__button')
        self.clear_input=page.get_by_role('button', name='Очистить строку поиска')

    def select_book(self, title: str, author: str, art: str = None):
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        card=(self.cards.filter(has_text=title).filter(has_text=author).filter(has_text=art).first)
        link_locator = card.locator('a[data-testid="art__title"]')
        link = link_locator.get_attribute('href')
        
        return BookCard(self.page, card)
    def clear(self):
        self.clear_input.click()
    def search(self, query : str):
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        self.search_input.click()
        self.search_input.fill(query)

        self.search_button.click()
        return SearchPage(self.page)
    
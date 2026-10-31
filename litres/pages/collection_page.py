import playwright
from playwright.sync_api import Page, expect
class CollectionPage:
    def __init__(self, page):
        self.page=page
        self.page_title=self.page.get_by_test_id('pageTitle')
        self.collection_cards = page.get_by_test_id('art__wrapper')
        self.collections=page.get_by_test_id('content__type--link')
        self.slider_block=page.get_by_test_id('slider__block--titleText').first
    def open_one_collections(self, name: str):
        collection=(self.collections.filter(has_text=name).first).click()

        return self
    def find_book(self, title: str, author: str, art: str = None):
        from components.book_card import BookCard
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        card=(self.collection_cards.filter(has_text=title).filter(has_text=author).filter(has_text=art).first)
        return BookCard(self.page, card)
    def get_collection_url(self):
        current_url=self.page.url
        return current_url
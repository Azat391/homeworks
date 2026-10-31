import playwright
from playwright.sync_api import Page, expect
class SeriesPage:
    def __init__(self, page:Page, name):
        self.page=page
        self.series_name=name
        self.series_title=page.get_by_test_id('series__title--text')
        self.series_cards=page.get_by_test_id('art__wrapper')
    def find_book(self, title: str, author: str, art: str = None):
        from components.book_card import BookCard
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        card=(self.series_cards.filter(has_text=title).filter(has_text=author).filter(has_text=art).first)
        return BookCard(self.page, card)
    def get_series_name(self):
        return self.series_title.inner_text()
    def get_series_url(self):
        current_url=self.page.url
        return current_url
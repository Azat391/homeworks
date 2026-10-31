import playwright
from playwright.sync_api import Page, expect
class GenrePage:
    def __init__(self, page: Page):
        self.page=page
        self.page_title=page.get_by_test_id('pageTitle')
        self.cards = page.get_by_test_id('art__wrapper')
    def find_book(self, title: str, author: str, art: str = None):
        from components.book_card import BookCard
        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        
        card=(self.cards.filter(has_text=title).filter(has_text=author).filter(has_text=art).first)
        return BookCard(self.page, card)
    
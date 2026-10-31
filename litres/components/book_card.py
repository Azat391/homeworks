import playwright
from playwright.sync_api import Page, expect
from pages.book_page import BookPage
class BookCard:
    def __init__(self, page: Page, card_locator):
        self.page = page
        self.card = card_locator
        self.link_locator = self.card.locator('a[data-testid="art__title"]')
    def return_href(self):
        return self.link_locator.get_attribute('href')
    def open(self):
        link = self.card.locator('a[data-testid="art__title"]')
        link.evaluate("el => el.removeAttribute('target')")
        link.click()
        return BookPage(self.page)
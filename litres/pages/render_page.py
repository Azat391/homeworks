import playwright
from playwright.sync_api import Page, expect
class RenderPage:
    def __init__(self, page:Page):
        self.page=page
        self.text_book=page.get_by_test_id("readOnline__fontSize--style")
    def go_back_to_book(self):
        from pages.book_page import BookPage
        self.page.go_back()
        self.page.wait_for_load_state()
        return BookPage(self.page)
    

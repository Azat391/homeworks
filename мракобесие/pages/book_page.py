import playwright
from playwright.sync_api import Page, expect
from pages.author_page import AuthorPage
class BookPage:
    def __init__(self, page: Page):
        self.page=page
        self.title = page.locator('h1[itemprop="name"]')
        self.author_details=page.get_by_test_id('art__author--details')
        self.art_person_link=page.get_by_test_id('art__personName--link')
    def url(self):
        current_url=self.page.url
        return current_url
    def go_back(self):
        from pages.search_page import SearchPage
        self.page.go_back()
        self.page.wait_for_load_state()
        return SearchPage(self.page)
    def art_person(self):
        
        self.art_person_link.click()
        return AuthorPage(self.page)
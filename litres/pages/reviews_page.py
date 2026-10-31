from playwright.sync_api import Page


class ReviewsPage:
    def __init__(self, page: Page):
        self.page = page
        self.author_title = page.get_by_test_id("chitatOnlayn__author--wrapper")
        self.reviews = page.get_by_test_id("review__wrapper")

    def go_back(self):
        from pages.book_page import BookPage

        self.page.go_back()
        self.page.wait_for_load_state()
        return BookPage(self.page)

    def return_one_review(self):
        return self.reviews.first.inner_text()

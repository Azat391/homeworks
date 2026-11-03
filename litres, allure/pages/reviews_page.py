import allure
from playwright.sync_api import Page


class ReviewsPage:
    def __init__(self, page: Page):
        self.page = page
        self.reviews_text = page.get_by_test_id("review__text").first
        self.book_info = page.locator(".JN9GQq_rightBlock__mainActions")
        self.title_element = self.book_info.locator('[itemprop="name"]')
        self.author_element = self.book_info.get_by_test_id(
            "chitatOnlayn__author--wrapper"
        )

    @allure.step("Возврат длины одного отзыва")
    def lenght_one_review(self):
        return len(self.reviews_text.inner_text())

    @allure.step("Возврат к странице книги")
    def go_back_to_book(self):
        from pages.book_page import BookPage

        self.page.go_back()
        return BookPage(self.page)

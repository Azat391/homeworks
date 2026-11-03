import allure
from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.litres.ru/"

    @allure.step("Открыть главную страницу")
    def open(self):
        self.page.goto(self.url)
        try:
            self.page.get_by_test_id("cookieAcceptPopup__accept").click()
        except PlaywrightTimeoutError:
            pass
        return self

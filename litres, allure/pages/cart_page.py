import allure
from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_list = page.get_by_test_id("cart__list--wrapper")
        self.cart_items = self.cart_list.locator('[data-testid^="cart__listItem--"]')
        self.empty_vidget = page.get_by_test_id("empty-state-content")

    @allure.step("Удалить книгу из корзины {name}")
    def delete_book_on_cart(self, name):
        deleting_book = self.cart_items.filter(has_text=name).first
        delete_button = deleting_book.get_by_test_id("cart__listDeleteButton")
        delete_button.click()
        self.page.get_by_test_id("cart__modalDeleteArt--button-primary").click()
        return self

    @allure.step("Найти книгу в корзине {name}")
    def find_book_in_cart(self, name):
        find_book = self.cart_items.filter(has_text=name).first
        return find_book.get_by_test_id("cart__bookCardTitle--wrapper")

    @allure.step("Перезагрузить страницу корзины")
    def reload(self):
        self.page.reload()
        return self

from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_list = page.get_by_test_id("cart__list--wrapper")
        self.cart_items = self.cart_list.locator('[data-testid^="cart__listItem--"]')
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")
        self.empty_vidget = page.get_by_test_id("empty-state-content")

    def delete_book_on_cart(self, name):
        deleting_book = self.cart_items.filter(has_text=name).first
        delete_button = deleting_book.get_by_test_id("cart__listDeleteButton")
        delete_button.click()
        self.page.get_by_test_id("cart__modalDeleteArt--button-primary").click()
        return self

    def is_item_present(self, title: str):
        return self.cart_items.filter(has_text=title).count() > 0

    def reload(self):
        self.page.reload()
        return self

    def search(self, query: str):
        from pages.search_page import SearchPage

        try:
            self.page.get_by_role("button", name="Принять").click(timeout=2000)
        except Exception:
            pass
        self.search_input.click()
        self.search_input.fill(query)

        self.search_button.click()
        return SearchPage(self.page)

import allure
from pages.search_page import SearchPage
from playwright.sync_api import Page


class Header:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")
        self.clear_button = page.get_by_role("button", name="Очистить строку поиска")
        self.collection_button = page.get_by_test_id("lowerMenu__item--compilations")
        self.genre_catalog = page.get_by_test_id("header-catalog-button")
        self.genre_button = page.get_by_test_id("popup__subGenre--link")
        self.cart_button = page.get_by_test_id("tab-basket")

    @allure.step("ВВести в поиск {query}")
    def search_book(self, query):
        self.search_input.fill(query)
        self.search_button.click()
        return SearchPage(self.page)

    @allure.step("Удалить предудущий поиск и ввести в поиск {query}")
    def clear_input_and_search_book(self, query):
        self.clear_button.click()
        self.search_input.fill(query)
        self.search_button.click()
        return SearchPage(self.page)

    @allure.step("Открыть подборки")
    def go_to_collection(self):
        from pages.collection_page import CollectionPage

        self.collection_button.click()
        return CollectionPage(self.page)

    @allure.step("Открыть жанры")
    def go_to_genre(self, genre_name):
        from pages.genre_page import GenrePage

        self.genre_catalog.click()
        self.genre_button.filter(has_text=genre_name).first.click()
        return GenrePage(self.page)

    @allure.step("Открыть корзину")
    def go_to_cart(self):
        from pages.cart_page import CartPage

        self.cart_button.click()
        return CartPage(self.page)

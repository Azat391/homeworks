from playwright.sync_api import Page, expect

from pages.author_page import AuthorPage


class BookPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('h1[itemprop="name"]')
        self.author_details = page.get_by_test_id("art__author--details")
        self.art_person_link = self.author_details.get_by_test_id(
            "art__personName--link"
        )
        self.series_info = page.get_by_test_id("art__inSeries--title")
        self.series_link = self.series_info.locator("a")
        self.sticky_player = page.get_by_test_id("sticky-player__wrapper")
        self.player_button = self.sticky_player.get_by_test_id(
            "sticky-player__play-pause-button"
        )
        self.text_button = page.get_by_test_id("book__fragmentReadListen--button")
        self.audio_button = page.get_by_test_id("book-player-button__wrapper")
        self.search_input = page.get_by_test_id("search__input")
        self.search_button = page.get_by_test_id("search__button")

    def url(self):
        current_url = self.page.url
        return current_url

    def go_back(self):
        from pages.search_page import SearchPage

        self.page.go_back()
        self.page.wait_for_load_state()
        return SearchPage(self.page)

    def go_back_in_collection(self):
        from pages.collection_page import CollectionPage

        self.page.go_back()
        self.page.wait_for_load_state()
        return CollectionPage(self.page)

    def art_person(self, author=None):

        self.art_person_link.filter(has_text=author).click()
        return AuthorPage(self.page)

    def open_series(self):
        from pages.series_page import SeriesPage

        self.series_name = self.series_link.inner_text()
        self.series_link.click()
        return SeriesPage(self.page, self.series_name)

    def open_reviews(self):
        from pages.reviews_page import ReviewsPage

        self.page.get_by_test_id("see__allReviews--button").click()
        return ReviewsPage(self.page)

    def open_render(self):
        from pages.render_page import RenderPage

        self.page.get_by_test_id("book__fragmentReadListen--button").click()
        return RenderPage(self.page)

    def start_pause_player(self):
        self.player_button.click()
        return self

    def go_to_audioversion(self):
        self.page.get_by_test_id("book-tabs-format__element_аудио").click()
        return self

    def go_to_textversion(self):
        self.page.get_by_test_id("book-tabs-format__element_текст").click()
        return self

    def add_to_cart(self):
        self.page.evaluate("document.getElementById('flomni')?.remove()")

        btn_add = self.page.get_by_test_id("book__addToCartButton").first
        expect(btn_add).to_be_enabled()
        btn_add.click()
        try:
            # Ждем до 5 секунд, пока кнопка сменится на "Перейти в корзину"
            # (это значит, что сервер ответил и React перерисовал кнопку)
            expect(self.page.get_by_test_id("book__goToCartButton")).to_be_visible(
                timeout=5000
            )
        except Exception:
            # Если через 5 секунд кнопка не поменялась, значит клик не сработал.
            # Бьем второй раз с силой.
            btn_add.click(force=True)
        self.page.get_by_role("button", name="Закрыть").click()

        return self

    def go_to_cart(self):
        from pages.cart_page import CartPage

        self.page.get_by_test_id("tab-basket").get_by_test_id("tab__link").click()
        return CartPage(self.page)

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

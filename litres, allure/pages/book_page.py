import allure
from playwright.sync_api import expect


class BookPage:
    def __init__(self, page):
        self.page = page
        self.art_title = page.get_by_test_id("book__name--wrapper")
        self.author_links = page.get_by_test_id("art__personName--link")
        self.series_link = page.get_by_test_id("art__inSeries--title").locator("a")
        self.reviews_link = page.get_by_test_id("see__allReviews--button")
        self.render_button = page.get_by_test_id("book__fragmentReadListen--button")
        self.play_fragment_btn = page.get_by_test_id("book-player-button__wrapper")
        self.play_pause_btn = page.get_by_test_id("sticky-player__play-pause-button")
        self.add_to_cart_button = page.get_by_test_id("book__addToCartButton")

    @allure.step("Возврат урл страницы")
    def url(self):
        return self.page.url

    @allure.step("Возврат на страницу поиска")
    def go_back(self):
        from pages.search_page import SearchPage

        self.page.go_back()
        return SearchPage(self.page)

    @allure.step("Переход к автора: {author}")
    def go_to_author(self, author=None):
        from pages.author_page import AuthorPage

        if author:
            target_author = self.author_links.filter(has_text=author).first
        else:
            target_author = self.author_links.first
        target_author.click()
        return AuthorPage(self.page)

    @allure.step("Переход к серии")
    def go_to_series(self):
        from pages.series_page import SeriesPage

        self.series_link.click()
        return SeriesPage(self.page)

    @allure.step("Возврат к странице коллекции")
    def go_back_to_collection(self):
        from pages.collection_page import CollectionPage

        self.page.go_back()
        return CollectionPage(self.page)

    @allure.step("Открыть отзывы")
    def go_to_reviews(self):
        from pages.reviews_page import ReviewsPage

        self.reviews_link.click()
        return ReviewsPage(self.page)

    @allure.step("Открыть текстовую версию")
    def go_to_render(self):
        from pages.render_page import RenderPage

        self.render_button.click()
        return RenderPage(self.page)

    @allure.step("Переход к текстовой версии")
    def go_to_textversion(self):
        self.page.get_by_test_id("book-tabs-format__element_текст").click()
        return self

    @allure.step("Переход к аудиоверсии")
    def go_to_audioversion(self):
        self.page.get_by_test_id("book-tabs-format__element_аудио").click()
        return self

    # Пришлось взять из прошлой работы , так как кнопка добавления в корзину прожимается а ничего не добавляется
    @allure.step("Добавление книги в корзину")
    def add_to_cart(self):
        self.page.evaluate("document.getElementById('flomni')?.remove()")

        btn_add = self.page.get_by_test_id("book__addToCartButton").first
        expect(btn_add).to_be_enabled()
        btn_add.click()
        try:
            # Ждем до 5 секунд, пока кнопка сменится на  "Перейти в корзину"
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

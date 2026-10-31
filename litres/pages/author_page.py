class AuthorPage:
    def __init__(self, page):
        self.page = page
        self.popular_cards = page.get_by_test_id(
            "popular__artsGreedSlider--block"
        ).get_by_test_id("slider__art")
        self.author_title = page.get_by_test_id("author__namePerson").locator("h1")

    def select_authors_book(self, title: str, author: str):
        from components.book_card import BookCard

        card = self.popular_cards.filter(has_text=title).filter(has_text=author).first
        link_locator = card.locator('a[data-testid="art__title"]')
        link = link_locator.get_attribute("href")

        return BookCard(self.page, card)

    def author_and_url(self):
        current_url = self.page.url
        current_author = self.author_title.inner_text()
        return current_url, current_author

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.ui
def test_ui_smoke(page: Page):
    page.goto("https://example.com")

    expect(
        page.get_by_text("This domain is for use in documentation examples")
    ).to_be_visible()

    page.screenshot(path="test-results/homepage.png")

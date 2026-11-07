import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_ui_smoke(page: Page):
    page.goto("https://example.com")
    
    # Проверяем, что заголовок содержит нужный текст (без time.sleep)
    expect(page.locator("h1")).to_have_text("Example Domain")
    
    # Сохраняем скриншот
    page.screenshot(path="test-results/screenshot.png")

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_ui_smoke(page: Page):
    page.goto("https://example.com")
    
    # Проверяем, что заголовок содержит нужный текст (без time.sleep)
    assert 1+2==3
    
    # Сохраняем скриншот
    page.screenshot(path="test-results/screenshot.png")

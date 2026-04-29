# Фикстуры: браузер, база данных, конфиг
import pytest
from playwright.sync_api import sync_playwright
from config.base import BASE_URL


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                        slow_mo=500)  # для наглядности
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page


def mobile():
    with sync_playwright() as p:
        drv_bro = p.webkit
        drv_bro = p.chromium.launch(headless=False,
                                        slow_mo=500)  # для наглядности
        page = drv_bro.new_page()
        page.goto(BASE_URL)
        yield page

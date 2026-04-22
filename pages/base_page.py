# Базовый класс страницы
from playwright.sync_api import sync_playwright, expect
import pytest
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page




# @pytest.fixture
# def page(self):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False,
#                                     slow_mo=500)  # для наглядности
#         page = browser.new_page()


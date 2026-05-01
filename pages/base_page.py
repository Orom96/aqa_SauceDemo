# Базовый класс страницы
from playwright.sync_api import sync_playwright, expect
from config.base import BASE_URL


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def expect_to_have_url(self, url_endpoint: str):
        expect(self.page).to_have_url(BASE_URL + url_endpoint)





# Базовый класс страницы
from playwright.sync_api import sync_playwright, expect
from config.base import BASE_URL
import allure


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def open(self, url=BASE_URL):
        pass

    def expect_to_have_url(self, url_endpoint: str):
        expect(self.page).to_have_url(BASE_URL + url_endpoint)

    @allure.step("Проверка: открыта страница '{url}'")
    def check_url(self, url):
        expect(self.page).to_have_url(url)



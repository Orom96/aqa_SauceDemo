# Страница авторизации
from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def assert_logged_in(self, url):
        expect(self.page).to_have_url(url)

# Страница авторизации
from playwright.sync_api import expect
from pages.base_page import BasePage
from config.base import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.field_username = self.page.locator("#user-name")
        self.field_password = self.page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Login")

    def login(self, name: str, password: str):
        self.field_password.fill(name)
        self.field_password.fill(password)
        self.login_button.click()

    def fill_username(self, username):
        self.field_username.fill(username)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_login_btn_and_check_url(self, page):
        self.login_button.click()
        expect(page).to_have_url(f'{BASE_URL}inventory.html')

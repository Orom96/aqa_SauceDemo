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
        self.error = self.page.locator('[data-test="error"]')

    def login(self, name: str, password: str):
        self.field_username.fill(name)
        self.field_password.fill(password)
        self.login_button.click()

    def fill_username(self, username):
        self.field_username.fill(username)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_login_btn_and_check_url(self, page):
        self.login_button.click()
        expect(page).to_have_url(f'{BASE_URL}inventory.html')

    def check_error_message_log_inf(self):
        expect(self.error).\
            to_contain_text("Epic sadface: Username and password do not match")

    def check_error_message_empty_username(self):
        expect(self.error).to_contain_text\
            ("Epic sadface: Username is required")

    def check_error_message_empty_password(self):
        expect(self.error).to_contain_text\
            ("Epic sadface: Password is required")

    def check_error_message_sql_injection(self):
        expect(self.error).\
            to_contain_text("Epic sadface: Username and password do not\
             match any user in this service")

    def check_error_message_xss(self):
        expect(self.error). \
            to_contain_text("Epic sadface: Username and password do not\
                     match any user in this service")
        return self.error


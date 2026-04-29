# Страница авторизации
from playwright.sync_api import expect

import config.users
from pages.base_page import BasePage
from config.base import BASE_URL

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.page = page
        self.field_username = self.page.locator("#user-name")
        self.field_password = self.page.locator("#password")
        self.login_button = self.page.get_by_role("button", name="Login")

    def login(self, name: str, password: str):
        self.field_password.fill(name)
        self.field_password.fill(password)
        self.login_button.click()

    def fill_username(self, username):
        self.field_username.fill(username)

    # def check_username(self, username):
    #     expect(self.field_username).to_have_value(username)

    def fill_password(self, password):
        self.field_password.fill(password)

    def click_login_btn_and_check_url(self, page):
        self.login_button.click()
        expect(page).to_have_url(f'{BASE_URL}inventory.html')


# class LoginPage(BasePage):
#
#     def open(self, page):
#         self.page.goto(BASE_URL)
#
#     def login(self, username, password):
#         self.page.fill("#user-name", username)
#         self.page.fill("#password", password)
#         self.page.click("#login-button")
#
#     def assert_logged_in(self, url):
#         expect(self.page).to_have_url(url)

    # def login_page(page):
    #
    # # === ШАГ 1: Авторизация ===
    # page.goto(BASE_URL)
    # # 2	Ввести логин
    # page.fill("#user-name", name)
    # expect(page.locator("#user-name")).to_have_value(name)
    #
    # # 3	Ввести пароль
    # page.fill("#password", password)
    # expect(page.locator("#password")).to_have_value(password)
    #
    # # 4	Нажать Login
    # page.click("#login-button")
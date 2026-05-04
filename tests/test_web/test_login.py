# # Кейсы TC_AUTH_*
from playwright.sync_api import expect
from config.base import BASE_URL
from config.users import (NAME, PASSWORD, NAME_PROBLEM_USER, \
                          NAME_PERFORMANCE_GLITCH_USER, WRONG_PASS, FAKE_USER,
                          EMPTY_NAME, EMPTY_PASSWORD,NAME_SQL_INJ,\
                          PASSWORD_SQL_INJ, NAME_XSS)
from config.products import BACKPACK_NAME
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage


class TestLogin:

    # TC_AUTH_001
    def test_login_001(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.fill_username(NAME)
        expect(login_page.field_username).to_have_value(NAME)
        login_page.fill_password(PASSWORD)
        expect(login_page.field_password).to_have_value(PASSWORD)
        login_page.click_login_btn_and_check_url(page)
        inventory_page = InventoryPage(page)
        expect(inventory_page.get_product()).to_be_visible()
        assert "/inventory.html" in page.url

    # TC_AUTH_002	Успешный вход с другими валидными пользователями
    def test_login_002(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        expect(inventory_page.get_product()).to_be_visible()

    # TC_AUTH_003	Вход с неверным паролем

    def test_login_003(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_PERFORMANCE_GLITCH_USER, WRONG_PASS)
        login_page.check_error_message_log_inf()

    # TC_AUTH_004	Вход с несуществующим логином
    def test_login_004(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(FAKE_USER, PASSWORD)
        login_page.check_error_message_log_inf()

    # TC_AUTH_005	Пустой логин
    def test_login_005(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(EMPTY_NAME, PASSWORD)
        login_page.check_error_message_empty_username()

    # TC_AUTH_006	Пустой пароль

    def test_login_006(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, EMPTY_PASSWORD)
        login_page.check_error_message_empty_password()

    #TC_AUTH_007	SQL-инъекция в логин (базовая безопасность)
    def test_login_007(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_SQL_INJ, PASSWORD_SQL_INJ)
        login_page.check_error_message_sql_injection()

    #TC_AUTH_008	XSS-попытка в поле логина
    def test_login_008(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_XSS, PASSWORD_SQL_INJ)
        login_page.check_error_message_xss()

    #TC_AUTH_009	Блокировка после 5 неудачных попыток
    def test_login_009(self, page):
        login_page = LoginPage(page)
        login_page.open()
        for _ in range(6):
            login_page.login("standard_user", "wrong_password")
        expect(login_page.check_error_message_xss()).to_be_visible()

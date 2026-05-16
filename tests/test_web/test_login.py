# # Кейсы TC_AUTH_*
import allure
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
from config.base import (LOG_INF, EMPTY_USERNAME, EMPTY_PASSWORD_TEXT,
                         SQL_INJECTION, XSS_TEXT)
import allure


@allure.epic("TestLogin")
@allure.feature("test")
@allure.story("tc_auth")
class TestLogin:
    @allure.title("test_login_001 Успешный вход со стандартным пользователем")
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

    # TC_AUTH_002
    @allure.title("test_login_002_Успешный вход с другими валидными пользователями")
    def test_login_002(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        expect(inventory_page.get_product()).to_be_visible()

    # TC_AUTH_003
    @allure.title("test_login_003_Вход с неверным паролем")
    def test_login_003(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_PERFORMANCE_GLITCH_USER, WRONG_PASS)
        login_page.check_error_message(LOG_INF)

    # TC_AUTH_004	Вход с несуществующим логином
    @allure.title("test_login_004_Вход с несуществующим логином")
    def test_login_004(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(FAKE_USER, PASSWORD)
        login_page.check_error_message(LOG_INF)

    # TC_AUTH_005	Пустой логин
    @allure.title("test_login_005_Пустой логин")
    def test_login_005(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(EMPTY_NAME, PASSWORD)
        login_page.check_error_message(EMPTY_USERNAME)

    # TC_AUTH_006	Пустой пароль
    @allure.title("test_login_006_Пустой пароль")
    def test_login_006(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, EMPTY_PASSWORD)
        login_page.check_error_message(EMPTY_PASSWORD_TEXT)

    #TC_AUTH_007	SQL-инъекция в логин (базовая безопасность)
    @allure.title("test_login_007_SQL-инъекция в логин (базовая безопасность)")
    def test_login_007(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_SQL_INJ, PASSWORD_SQL_INJ)
        login_page.check_error_message(SQL_INJECTION)

    #TC_AUTH_008	XSS-попытка в поле логина
    @allure.title("test_login_008_XSS-попытка в поле логина")
    def test_login_008(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME_XSS, PASSWORD_SQL_INJ)
        login_page.check_error_message(XSS_TEXT)

    #TC_AUTH_009	Блокировка после 5 неудачных попыток
    @allure.title("test_login_009_Блокировка после 5 неудачных попыток")
    def test_login_009(self, page):
        login_page = LoginPage(page)
        login_page.open()
        for _ in range(6):
            login_page.login(NAME, WRONG_PASS)
            login_page.check_error_message(XSS_TEXT)

        #TC_AUTH_010	Сохранение сессии после перезагрузки страницы
    @allure.title("test_login_010_Сохранение сессии после перезагрузки страницы")
    def test_login_010(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, PASSWORD)
        # expect(page).to_have_url("**/inventory.html")
        # перезагрузка
        page.reload()
        assert page.url.endswith("/inventory.html")
        # expect(page.locator(".inventory_list")).to_be_visible()

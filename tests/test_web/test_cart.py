from playwright.sync_api import expect
from config.users import (NAME, PASSWORD)
from config.products import BACKPACK_NAME, BIKE_LIGHT, T_SHIRT
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure


@allure.epic("")
class TestCart:

    # TC_CART_001	Добавление одного товара
    @allure.title("test_cart_001_Добавление одного товара")
    def test_cart_001(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, PASSWORD)
        inventory_page = InventoryPage(page)
        inventory_page.add_to_cart(BACKPACK_NAME)
        inventory_page.check_badge_of_cart()

    #TC_CART_002 Добавление нескольких разных товаров
    @allure.title("test_cart_002_Добавление нескольких разных товаров")
    def test_cart_002(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, PASSWORD)
        inventory_page = InventoryPage(page)
        inventory_page.add_to_cart(BACKPACK_NAME)
        inventory_page.add_to_cart(BIKE_LIGHT)
        inventory_page.add_to_cart(T_SHIRT)
        expect(inventory_page.check_badge_of_cart_several()).to_have_text("3")

    #TC_CART_003	Добавление одного товара несколько раз
    @allure.title("test_cart_003_Добавление одного товара несколько раз")
    def test_cart_002(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, PASSWORD)
        inventory_page = InventoryPage(page)
        inventory_page.add_to_cart(BACKPACK_NAME)
        inventory_page.add_cart(BACKPACK_NAME)
        # inventory_page.add_cart(BACKPACK_NAME)
        inventory_page.check_badge_of_cart()

    def test_cart_003(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(NAME, PASSWORD)

        inventory_page = InventoryPage(page)
        inventory_page.add_item_multiple_times(BACKPACK_NAME, 3)
        inventory_page.check_cart_badge("1")
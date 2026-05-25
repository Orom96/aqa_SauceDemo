from config.products import EXPECTED_ITEMS, EXPECTED_PRICES, \
    EXPECTED_SORT_PRICES
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.products import BACKPACK_NAME
import allure


@allure.epic("TestInventory")
@allure.feature("test")
@allure.story("TC_INVENTORY")
class TestInventory:
    #TC_INV_001	Отображение всех 6 товаров
    @allure.title("test_inv_001_Отображение всех 6 товаров")
    def test_inv_001(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        assert inventory_page.check_count_item() == 6

        #TC_INV_002	Проверка названий всех товаров
    @allure.title("test_inv_002_Проверка названий всех товаров")
    def test_inv_002(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        actual_items = inventory_page.get_list_of_item()
        assert actual_items == EXPECTED_ITEMS

    #TC_INV_003	Проверка цен всех товаров
    @allure.title("test_inv_003_Проверка цен всех товаров")
    def test_inv_003(self,logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        actual_data = inventory_page.get_item_price()
        assert actual_data == EXPECTED_PRICES

    #TC_INV_004	Проверка изображений товаров
    def test_in_004(self,logged_in_page):
        inventory_page = InventoryPage(logged_in_page)

    @allure.title("test_inv_005_Сортировка по цене (низкая → высокая)")
    #TC_INV_005	Сортировка по цене (низкая → высокая)
    def test_inv_005(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        sort_low_to_high = inventory_page.check_sort_low_high()
        actual_items_prices = inventory_page.get_item_price()
        # print(actual_items)
        # assert actual_items_prices == sorted(actual_items_prices)
        prices = [float(p.replace("$", "")) for p in actual_items_prices]
        assert prices == sorted(prices)

    #TC_INV_006	Сортировка по цене (высокая → низкая)
    @allure.title(" #test_inv_006_Сортировка по цене (высокая → низкая)")
    def test_inv_006(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        sort_high_to_low = inventory_page.check_sort_high_low()
        actual_items_prices = inventory_page.get_item_price()
        prices = [float(p.replace("$", "")) for p in actual_items_prices]
        assert prices == sorted(prices, reverse=True)

    @allure.title("test_inv_007_Сортировка по названию (A→Z)")
    #TC_INV_007	Сортировка по названию (A→Z)
    def test_inv_007(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        sort_a_to_z = inventory_page.check_sort_a_to_z()
        actual_items_names = inventory_page.get_list_of_item()
        with allure.step("Проверка сортировки товаров по имени A-Z"):
            assert actual_items_names == sorted(actual_items_names)

    @allure.title("test_inv_008_Фильтрация после добавления в корзину")
    #TC_INV_008	Фильтрация после добавления в корзину
    def test_inv_008(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.add_to_cart(product_name=BACKPACK_NAME)
        sort_low_to_high = inventory_page.check_sort_low_high()
        inventory_page.check_badge_of_cart()
        assert inventory_page.check_remove_btn_visible

    @allure.title("test_inv_009_Фильтрация после добавления в корзину")
    #TC_INV_009	Клик по изображению товара (если есть переход)
    def test_inv_009(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.click_on_img()
        inventory_page.check_url("inventory-item.html")

    # TC_INV_010	Проверка кнопки "Remove" после добавления в корзину
    @allure.title("test_inv_010_Проверка кнопки 'Remove'после добавления в корзину")
    def test_inv_010(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.add_to_cart(product_name=BACKPACK_NAME)
        inventory_page.check_sort_low_high()
        inventory_page.check_badge_of_cart()
        inventory_page.check_remove_btn_visible()







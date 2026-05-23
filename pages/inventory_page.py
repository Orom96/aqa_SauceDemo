# Страница товаров
from playwright.sync_api import expect
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.product = self.page.get_by_text("Sauce Labs Backpack")
        self.price_of_product = self.page.\
            locator('.inventory_item:has-text("Sauce Labs Backpack") \
                     .inventory_item_price'
                    )
        self.add_cart = self.page.\
            locator('#add-to-cart-sauce-labs-backpack')

        self.remove_cart = self.page.\
            locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_badge = self.page.\
            locator('[data-test="shopping-cart-badge"]')

        self.ship_cart_badge = self.page.locator(".shopping_cart_badge")
        self.inventory_item = self.page.locator(".inventory_item")
        self.inventory_item_name = self.page.locator(".inventory_item_name")
        self.inventory_item_price = self.page.locator(".inventory_item_price")
        self.sort_lo_hi = self.page.\
            locator('[data-test="product-sort-container"]')
        self.remove_btn = self.page.\
            locator("[data-test='remove-sauce-labs-backpack']")

        self.img = self.page.\
            locator("[data-test = 'inventory-item-sauce-labs-backpack-img']")
    def get_product(self):
        return self.product

    def save_price(self):
        return self.price_of_product.inner_text()

    def add_to_cart(self, product_name):
        self.add_cart.click()

    def check_badge_of_cart(self):
        expect(self.cart_badge).to_have_text("1")

    def click_shipping_cart_badge(self):
        self.ship_cart_badge.click()

    def check_count_item(self):
        return self.inventory_item.count()

    def get_list_of_item(self):
        return self.inventory_item_name.all_text_contents()

    def get_item_price(self):
        return self.inventory_item_price.all_text_contents()

    def check_sort_low_high(self):
        return self.sort_lo_hi.select_option("lohi")

    def check_sort_high_low(self):
        return self.sort_lo_hi.select_option("hilo")

    def check_sort_a_to_z(self):
        return self.sort_lo_hi.select_option("az")

    # def check_remove_btn_visible(self):
    #     expect(self.remove_btn).to_be_visible()

    def click_on_img(self):
        self.img.click()

    def check_remove_btn_visible(self):
        assert self.remove_btn.is_visible(), \
            "Кнопка Remove не отображается после добавления товара в корзину"

    def check_product_visible(self):
        with allure.step("Проверка: товар отображается на странице"):
            expect(self.get_product()).to_be_visible()

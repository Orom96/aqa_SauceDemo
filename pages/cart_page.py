# Корзина
from pages.base_page import BasePage
from config.products import BACKPACK_NAME
from playwright.sync_api import expect


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.items_in_cart = self.page.locator(".cart_item")
        self.cart_quantity = self.page.locator(".cart_quantity")
        self.name_of_product = self.page.locator(".inventory_item_name")
        self.price_of_product = self.page.locator(".inventory_item_price")
        self.checkout = self.page.locator("#checkout")

    def get_items_in_cart(self):
        return self.items_in_cart.all()

    def get_quantity_in_cart(self):
        return self.cart_quantity

    def verify_product_name(self):
        expect(self.name_of_product).to_contain_text(BACKPACK_NAME)
        return self.name_of_product.first

    def get_price(self):
        return self.price_of_product.inner_text()

    def click_checkout_btn(self, page):
        self.checkout.click()


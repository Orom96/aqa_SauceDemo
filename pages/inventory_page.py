# Страница товаров
from playwright.sync_api import expect
from pages.base_page import BasePage
from config.base import BASE_URL
from config.products import BACKPACK_NAME


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.product = self.page.get_by_text("Sauce Labs Backpack")
        self.price_of_product = self.page.\
            locator('.inventory_item:has-text("Sauce Labs Backpack") .inventory_item_price')
        self.add_cart = self.page.\
            locator('#add-to-cart-sauce-labs-backpack')

        self.remove_cart = self.page.\
            locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_badge = self.page.\
            locator('[data-test="shopping-cart-badge"]')

        self.ship_cart_badge = self.page.locator(".shopping_cart_badge")

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

    def check_url_cart(self, page):
        expect(page).to_have_url(f'{BASE_URL}cart.html')
    # def open_cart_url(self, page):
    #     expect(page).to_have_url(f'{BASE_URL}cart.html')
    # def val_badge(self):
    #     self.ship_cart_badge.






    #
    # def get_product_price(self, product_name):
    #     item = self.page.locator(f'.inventory_item:has-text("{product_name}")')
    #     price = item.locator('.inventory_item_price').inner_text()
    #     return price

    # def add_to_cart(self, product_name):
    #     item = self.page.locator(f'.inventory_item:has-text("{product_name}")')
    #     item.get_by_role("button", name="Add to cart").click()

    # def go_to_cart(self):
    #     self.page.click('[data-test="shopping-cart-link"]')

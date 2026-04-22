# Страница товаров
from playwright.sync_api import expect
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def get_product_price(self, product_name):
        item = self.page.locator(f'.inventory_item:has-text("{product_name}")')
        price = item.locator('.inventory_item_price').inner_text()
        return price

    def add_to_cart(self, product_name):
        item = self.page.locator(f'.inventory_item:has-text("{product_name}")')
        item.get_by_role("button", name="Add to cart").click()

    def go_to_cart(self):
        self.page.click('[data-test="shopping-cart-link"]')

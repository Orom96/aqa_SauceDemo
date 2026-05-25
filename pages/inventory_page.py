# Страница товаров
from playwright.sync_api import expect
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.product = self.page.get_by_text("Sauce Labs Backpack")
        self.price_of_product = self.page.\
            locator('.inventory_item:has-text("Sauce Labs Backpack") \
                     .inventory_item_price'
                    )
        self.add_cart = self.page.get_by_role("button", name="Add to cart")

        self.remove_cart = self.page.\
            locator('[data-test="remove-sauce-labs-backpack"]')
        self.cart_badge = self.page.\
            locator('[data-test="shopping-cart-badge"]')

        self.ship_cart_badge = self.page.locator(".shopping_cart_badge")

    def get_product(self):
        return self.product

    def save_price(self):
        return self.price_of_product.inner_text()

    # def add_to_cart(self, product_name):
    #     self.add_cart.click()
    def add_to_cart(self, product_name):
        product = self.page.locator(
            f'.inventory_item:has-text("{product_name}")'
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def check_badge_of_cart(self):
        expect(self.cart_badge).to_have_text("1")

    def check_badge_of_cart_several(self):
        return self.cart_badge


    def click_shipping_cart_badge(self):
        self.ship_cart_badge.click()



# Корзина
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.items_in_cart = self.page.locator(".cart_item")
        self.cart_quantity = self.page.locator(".cart_quantity")
        self.name_of_product = self.page.locator(".inventory_item_name")
        self.price_of_product = self.page.locator(".inventory_item_price")
        self.checkout = self.page.locator("#checkout")

    def cart(self):
      return self.items_in_cart.all()

    def quantity(self):
       return self.cart_quantity

    def product_name(self):
        return self.name_of_product.first

    def price(self):
        return self.price_of_product.inner_text()

    def checkout_btn(self):
        return self.checkout

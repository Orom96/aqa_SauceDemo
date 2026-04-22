# Корзина
from pages.base_page import BasePage


class CartPage(BasePage):

    def checkout(self):
        self.page.click('[data-test="checkout"]')

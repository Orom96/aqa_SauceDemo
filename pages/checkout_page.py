# Чекаут (2 шага)
from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.name = self.page.locator("#first-name")
        self.surname = self.page.locator("#last-name")
        self.post_code = self.page.locator("#postal-code")
        self.loc_continue = self.page.locator("#continue")


    def first_name(self):
        return self.name

    def last_name(self):
        return self.surname

    def postal_code(self):
        return self.post_code

    def btn_continue(self):
        return self.loc_continue

    def summary_item(self):
        return self.loc_summary_item


class CheckoutPage2(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.loc_summary_item = self.page.locator(".summary_item")
        self.cart_list = self.page.locator('.cart_item')
        self.price_checkout = self.page.\
            locator('[data-test="inventory-item-price"]')
        self.payment_info = self.page.\
            locator('[data-test="payment-info-value"]')
        self.shipping_info = self.page.\
            locator('[data-test="shipping-info-value"]')
        self.item_total = self.page.locator(".summary_subtotal_label")
        self.tax_label = self.page.locator(".summary_tax_label")
        self.tax_and_total = self.page.locator(".summary_total_label")

    def list_of_item(self):
        return self.cart_list.all()

    def price_in_checkout_page(self):
        return self.price_checkout.inner_text()

    def payment_info_loc(self):
        return self.payment_info

    def shipping_info_loc(self):
        return self.shipping_info

    def item_total_loc(self):
        return self.item_total.inner_text()

    def tax_loc(self):
        return self.tax_label

    def abs_total_tax(self):
        return self.tax_and_total.inner_text()


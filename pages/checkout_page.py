# Чекаут (2 шага)
from playwright.sync_api import expect
from pages.base_page import BasePage
from config.users import FIRST_NAME, LAST_NAME, POSTAL_CODE
from config.base import BASE_URL


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # self.page = page

        self.name = self.page.locator("#first-name")
        self.surname = self.page.locator("#last-name")
        self.post_code = self.page.locator("#postal-code")
        self.loc_continue = self.page.locator("#continue")
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

    def fill_first_name_and_verify(self):
        self.name.fill(FIRST_NAME)
        expect(self.name).to_have_value("Joe")

    def fill_last_name_and_verify(self):
        self.surname.fill(LAST_NAME)
        expect(self.surname).to_have_value("Lowson")

    def fill_postal_code(self):
        self.post_code.fill(POSTAL_CODE)

    def click_continue_and_wait_for_url(self,page):
        self.loc_continue.click()
        expect(page).to_have_url(f'{BASE_URL}checkout-step-two.html')

    def get_list_of_item(self):
        return self.cart_list.all()

    def get_price_in_checkout_page(self):
        return self.price_checkout.inner_text()

    def check_payment_info(self):
        expect(self.payment_info).to_contain_text("SauceCard #31337")

    def check_shipping_info(self):
        expect(self.shipping_info).to_contain_text("Pony Express")

    def get_item_total_price(self):
        return self.item_total.inner_text()

    def verify_tax(self):
        expect(self.tax_label).to_have_text("Tax: $2.40")

    def get_tax_and_total_text(self):
        self.tax_and_total.inner_text()




#
# class CheckoutPage2(BasePage):
#
#     def __init__(self, page):
#         super().__init__(page)
#         self.page = page
#         self.loc_summary_item = self.page.locator(".summary_item")
#         self.cart_list = self.page.locator('.cart_item')
#         self.price_checkout = self.page.\
#             locator('[data-test="inventory-item-price"]')
#         self.payment_info = self.page.\
#             locator('[data-test="payment-info-value"]')
#         self.shipping_info = self.page.\
#             locator('[data-test="shipping-info-value"]')
#         self.item_total = self.page.locator(".summary_subtotal_label")
#         self.tax_label = self.page.locator(".summary_tax_label")
#         self.tax_and_total = self.page.locator(".summary_total_label")
#
#     def list_of_item(self):
#         return self.cart_list.all()
#
#     def price_in_checkout_page(self):
#         return self.price_checkout.inner_text()
#
#     def payment_info_loc(self):
#         return self.payment_info
#
#     def shipping_info_loc(self):
#         return self.shipping_info
#
#     def item_total_loc(self):
#         return self.item_total.inner_text()
#
#     def tax_loc(self):
#         return self.tax_label
#
#     def abs_total_tax(self):
#         return self.tax_and_total.inner_text()
#

# Чекаут (2 шага)
from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def fill_info(self, first_name, last_name, zip_code):
        self.page.fill('[data-test="firstName"]', first_name)
        self.page.fill('[data-test="lastName"]', last_name)
        self.page.fill('[data-test="postalCode"]', zip_code)
        self.page.click('[data-test="continue"]')

    def finish(self):
        self.page.click('[data-test="finish"]')

    def assert_success(self):
        expect(self.page.locator("text=Thank you for your order!")).to_be_visible()

    def back_home(self):
        self.page.click('[data-test="back-to-products"]')
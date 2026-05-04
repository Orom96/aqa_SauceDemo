# Страница успеха

from pages.base_page import BasePage
from playwright.sync_api import expect


class CompletePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.finish = self.page.locator("#finish")
        self.header = self.page.locator('[data-test="title"]')
        self.text_thanks = self.page.locator("text=Thank you for your order!")
        self.text_dispatched = self.page.\
            locator("text=Your order has been dispatched")
        self.back_home = self.page.locator("#back-to-products")

    def click_btn_finish(self, page):
        self.finish.click()
        # expect(page).to_have_url("/checkout-complete.html")

    def check_text_in_header(self):
        expect(self.header).to_have_text("Checkout: Complete!")

    def check_text_thanks(self):
        expect(self.text_thanks).to_be_visible()

    def check_text_dispatched(self, page):
        expect(self.text_dispatched).to_contain_text("dispatched")

    def back_home_button_visible_clickable(self):
        expect(self.back_home).to_be_enabled()
        self.back_home.click()
from playwright.sync_api import expect
from config.base import BASE_URL
from config.users import NAME, PASSWORD
from config.products import BACKPACK_NAME
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage


class TestE2eCheck:

    def test_e2e_cases(self, page):
        #1-Открыть сайт
        expect(page).to_have_url(BASE_URL)
        login_page = LoginPage(page)
        #2-Ввести логин
        login_page.fill_username(NAME)
        expect(login_page.field_username).to_have_value(NAME)
        #3-Ввести пароль
        login_page.fill_password(PASSWORD)
        expect(login_page.field_password).to_have_value(PASSWORD)
        #4-Нажать Login
        login_page.click_login_btn_and_check_url(page)
        #5-Найти товар "Sauce Labs Backpack
        inventory_page = InventoryPage(page)
        expect(inventory_page.get_product()).to_be_visible()
        #6-Сохранить цену товара
        saved_price = inventory_page.save_price()
        print(saved_price)
        assert saved_price.startswith("$")
        #7-Нажать "Add to cart" для товара
        inventory_page.add_to_cart(BACKPACK_NAME)
        #Смены кнопки Add to cart на  Remove
        expect(inventory_page.remove_cart).to_be_visible()
        # 8-Проверить бейдж корзины
        inventory_page.check_badge_of_cart()
        #9-Открыть корзину
        inventory_page.click_shipping_cart_badge()
        base_page = BasePage(page)
        base_page.expect_to_have_url('cart.html')
        #10-Проверить количество товаров в корзине
        cart_page = CartPage(page)
        cart_items = cart_page.get_items_in_cart()
        assert len(cart_items) == 1
        #11-Проверить количество единиц товара
        qty_locator = cart_page.get_quantity_in_cart()
        expect(qty_locator).to_have_text("1")
        #12-Проверить название товара
        cart_page.verify_product_name()
        #13-Проверить цену в корзине
        cart_price = cart_page.get_price()
        assert cart_price == saved_price
        #14-Нажать Checkout
        cart_page.click_checkout_btn(page)
        base_page.expect_to_have_url('checkout-step-one.html')
        #15-Заполнить First name
        checkout_page = CheckoutPage(page)
        checkout_page.fill_first_name_and_verify()
        #16-Заполнить Last name
        checkout_page.fill_last_name_and_verify()
        #17-Заполнить postal_code
        checkout_page.fill_postal_code()
        #18-Нажать Continue
        checkout_page.click_continue_and_wait_for_url(page)
        #19-Проверить товар на чекауте
        items = checkout_page.get_list_of_item()
        print(len(items))
        assert len(items) == 1 and "Backpack" in BACKPACK_NAME
        #20	Проверить цену на чекауте
        checkout_price = checkout_page.get_price_in_checkout_page()
        assert checkout_price == saved_price
        #21 Проверить Payment Information
        checkout_page.check_payment_info()
        #22	Проверить Shipping Information
        checkout_page.check_shipping_info()
        #23	Проверить Item total
        item_total = checkout_page.get_item_total_price()
        # assert item_total == saved_price
        assert saved_price in item_total
        #24	Проверить Tax
        checkout_page.verify_tax()
        #25 Проверить Total
        total = checkout_page.get_tax_and_total_text()
        # assert abs(total - (item_total + 2.40)) < 0.01
        #26 Нажать Finish
        complete_page = CompletePage(page)
        complete_page.click_btn_finish(page)
        base_page.expect_to_have_url('checkout-complete.html')
        #27 Проверить заголовок успеха
        complete_page.check_text_in_header()
        #28 Проверить благодарность
        complete_page.check_text_thanks()
        #29	Проверить сообщение о доставке
        complete_page.check_text_dispatched(page)
        #30 Проверить кнопку Back Home
        #31	Нажать Back Home
        complete_page.back_home_button_visible_clickable()
        base_page.expect_to_have_url("inventory.html")


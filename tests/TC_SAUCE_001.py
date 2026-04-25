from playwright.sync_api import sync_playwright, expect, Page
from config.base import BASE_URL, URL_INVENTORY, URL_CART
from config.users import name, password,first_name,last_name, postal_code
from config.products import backpack_name
from pages.base_page import BasePage
# import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_page import CheckoutPage2


class TestE2eCheck:

    def test_e2e_cases(self, page):
        #1-Открыть сайт
        expect(page).to_have_url(BASE_URL)
        login_page = LoginPage(page)
        #2-Ввести логин
        login_page.fill_username(name)
        expect(login_page.field_username).to_have_value(name)
        #3-Ввести пароль
        login_page.fill_password(password)
        expect(login_page.field_password).to_have_value(password)
        #4-Нажать Login
        login_page.login_btn()
        expect(page).to_have_url(f'{BASE_URL}inventory.html')
        #5-Найти товар "Sauce Labs Backpack
        inventory_page = InventoryPage(page)
        expect(inventory_page.get_product()).to_be_visible()
        #6-Сохранить цену товара
        saved_price = inventory_page.save_price()
        print(saved_price)
        assert saved_price.startswith("$")
        #7-Нажать "Add to cart" для товара
        inventory_page.add_to_cart(backpack_name)
        #Смены кнопки Add to cart на  Remove
        expect(inventory_page.remove_cart).to_be_visible()
        val_badge = inventory_page.badge_of_cart()
        expect(val_badge).to_have_text("1")
        # 8-Проверить бейдж корзины
        expect(val_badge).to_contain_text("1")
        #9-Открыть корзину
        inventory_page.ship_cart_badge.click()
        expect(page).to_have_url(f'{BASE_URL}cart.html')
        #10-Проверить количество товаров в корзине
        cart_page = CartPage(page)
        cart_items = cart_page.cart()
        assert len(cart_items) == 1
        #11-Проверить количество единиц товара
        qty_locator = cart_page.quantity()
        # print(qty_locator)
        expect(qty_locator).to_have_text("1")
        #12-Проверить название товара
        name_locator = cart_page.product_name()
        expect(name_locator).to_contain_text(backpack_name)
        #13-Проверить цену в корзине
        cart_price = cart_page.price()
        assert cart_price == saved_price
        #14-Нажать Checkout
        cart_page.checkout_btn().click()
        expect(page).to_have_url(f'{BASE_URL}checkout-step-one.html')
        #15-Заполнить First name
        checkout_page = CheckoutPage(page)
        checkout_page.first_name().fill(first_name)
        expect(page.locator("#first-name")).to_have_value("Joe")
        #16-Заполнить Last name
        checkout_page.last_name().fill(last_name)
        expect(page.locator("#last-name")).to_have_value("Lowson")
        #17-Заполнить postal_code
        checkout_page.postal_code().fill(postal_code)
        #18-Нажать Continue
        checkout_page.btn_continue().click()
        expect(page).to_have_url(f'{BASE_URL}checkout-step-two.html')
        #19-Проверить товар на чекауте
        checkout_page2 = CheckoutPage2(page)
        items = checkout_page2.list_of_item()
        print(len(items))
        assert len(items) == 1 and "Backpack" in backpack_name
        #20	Проверить цену на чекауте
        checkout_price = checkout_page2.price_in_checkout_page()
        assert checkout_price == saved_price
        #21 Проверить Payment Information
        payment_locator = checkout_page2.payment_info_loc()
        expect(payment_locator).to_contain_text("SauceCard #31337")
        #22	Проверить Shipping Information
        shipping_locator = checkout_page2.shipping_info_loc()
        expect(shipping_locator).to_contain_text("Pony Express")
        #23	Проверить Item total
        item_total = checkout_page2.item_total_loc()
        # assert item_total == saved_price
        assert saved_price in item_total
        #24	Проверить Tax
        tax_locator = checkout_page2.tax_loc()
        expect(tax_locator).to_have_text("Tax: $2.40")
        total = checkout_page2.abs_total_tax()
        assert abs(total - (item_total + 2.40)) < 0.01

















def test_page_inventory(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    #вызов теста логинна

    expect(page).to_have_url(URL_INVENTORY)
        #5 Найти товар "Sauce Labs Backpack"
    expect(page.locator('//*[@id="item_4_title_link"]/div'))\
        .to_be_visible()

    #6	Сохранить цену товара
    item = page.locator('.inventory_item:has-text("Sauce Labs Backpack")')
    price_locator = item.locator('.inventory_item_price')
    price_text = price_locator.inner_text()
    print(price_text)
    assert price_text.startswith("$")

    #7	Нажать "Add to cart" для товара
    find_product = page.get_by_text(backpack)
    find_product.click()
    add_to_cart = page.locator('[data-test="add-to-cart"]')
    add_to_cart.click()

    # text = add_to_cart.text_content()
    # assert "Remove" in text

    #проверка корзины
    cart_badge = page.locator('[data-test="shopping-cart-badge"]')
    # expect(cart_badge).to_have_text("1")

    cart = page.locator('[data-test="shopping-cart-link"]')
    cart.click()


def test_page_cart(page):
    login_page(page)  #вызов теста логинна
    test_page_inventory(page)  #вызов теста где идет выборка товара
    page.goto(URL_CART)
    expect(page).to_have_url(URL_CART)
    qty_locator = page.locator('[data-test="item-quantity"]')
    qty_locator.count()
    expect(qty_locator).to_have_text("1")
    item = page.locator('.cart_item').all()
    assert len(item) == 1
    # assert len(qty_locator) == 1
    # expect(cart_badge).to_contain_text("1")
    # expect(cart).to_have_text("1")
    #
    # #оформление заказа заполнение данных
    checkout = page.locator('[data-test="checkout"]')
    checkout.click()

    checkout_fill_name = page.locator('[data-test="firstName"]')
    checkout_fill_name.fill('Orom')
    checkout_fill_last_name = page.locator('[data-test="lastName"]')
    checkout_fill_last_name.fill('Anvarov')
    checkout_fill_zip = page.locator('[data-test = "postalCode"]')
    checkout_fill_zip.fill('734000')
    btn_continue = page.locator('[data-test="continue"]')
    btn_continue.click()
    btn_finish = page.locator('[data-test="finish"]')
    btn_finish.click()
    locator = page.locator("text=Thank you for your order!")
    expect(locator).to_be_visible()
    btn_back_to_home = page.locator('[data-test="back-to-products"]')
    btn_back_to_home.click()




        #
        # # === ШАГ 2: Найти товар и сохранить цену ===
        # backpack_item = page.locator("text=Sauce Labs Backpack").locator(
        #     "..")  # родительский контейнер
        # price_on_listing = backpack_item.locator(
        #     ".inventory_item_price").text_content().strip()
        # # price_on_listing = "$29.99"
        #
        # backpack_item.get_by_role("button", name="Add to cart").click()
        #
        # # === ШАГ 3: Проверить индикатор корзины ===
        # cart_badge = page.locator(".shopping_cart_badge")
        # assert cart_badge.text_content() == "1", "В корзине должен быть 1 товар"
        #
        # # === ШАГ 4: Перейти в корзину ===
        # page.click(".shopping_cart_link")
        #
        # # === ШАГ 5: Проверки в корзине ===
        # cart_items = page.locator(".cart_item")
        # assert cart_items.count() == 1, "Должен быть один товар в корзине"
        #
        # item_name = page.locator(".inventory_item_name").text_content()
        # assert "Sauce Labs Backpack" in item_name
        #
        # item_qty = page.locator(".cart_quantity").text_content()
        # assert item_qty == "1"
        #
        # price_in_cart = page.locator(
        #     ".inventory_item_price").text_content().strip()
        # assert price_in_cart == price_on_listing, "Цена в корзине должна совпадать с ценой на странице"
        #
        # # === ШАГ 6: Оформление заказа ===
        # page.click("#checkout")
        #
        # page.fill("#first-name", "Joe")
        # page.fill("#last-name", "Lowson")
        # page.fill("#postal-code", "1234")
        # page.click("#continue")
        #
        # # === ШАГ 7: Проверки на странице подтверждения ===
        # assert page.get_by_text("Payment Information:").is_visible()
        # assert "SauceCard #31337" in page.text_content()
        #
        # assert page.get_by_text("Shipping Information:").is_visible()
        # assert "Free Pony Express Delivery!" in page.text_content()
        #
        # # Считываем цены
        # item_total_text = page.get_by_text("Item total:").text_content()
        # item_total = float(item_total_text.replace("Item total: $", ""))
        #
        # expected_item_total = float(price_on_listing.replace("$", ""))
        # assert item_total == expected_item_total
        #
        # tax = float(
        #     page.get_by_text("Tax:").text_content().replace("Tax: $", ""))
        # assert tax == 2.40, "Налог должен быть $2.40"
        #
        # total_text = page.get_by_text("Total:").text_content()
        # total = float(total_text.replace("Total: $", ""))
        #
        # expected_total = round(item_total + tax, 2)
        # assert total == expected_total, f"Ожидалось {expected_total}, получено {total}"
        #
        # # === ШАГ 8: Завершение заказа ===
        # page.click("#finish")
        #
        # # === ШАГ 9: Финальная проверка ===
        # assert page.get_by_text("Checkout: Complete!").is_visible()
        # assert page.get_by_text("Thank you for your order!").is_visible()
        # assert page.get_by_text("Your order has been dispatched").is_visible()
        # assert page.get_by_role("button", name="Back Home").is_visible()
        #
        # browser.close()


if __name__ == '__main__':
    test_complete_checkout_flow()

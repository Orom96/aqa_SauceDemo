from playwright.sync_api import sync_playwright,expect
# import pytest

BASE_URL = "https://www.saucedemo.com"


def test_complete_checkout_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    slow_mo=500)  # для наглядности
        page = browser.new_page()

        # === ШАГ 1: Авторизация ===
        page.goto(BASE_URL)

        page.fill("#user-name", "standard_user")
        expect(page.locator("#user-name")).to_have_value("standard_user")
        page.fill("#password", "secret_sauce")
        expect(page.locator("#password")).to_have_value("secret_sauce")
        page.click("#login-button")
        expect(page).to_have_url(f"{BASE_URL}/inventory.html")
        # === ШАГ 2: добавление товара  ===
        expect(page.locator('//*[@id="item_4_title_link"]/div'))\
            .to_be_visible()
        item = page.locator('.inventory_item:has-text("Sauce Labs Backpack")')
        price_locator = item.locator('.inventory_item_price')
        price_text = price_locator.inner_text()
        print(price_text)
        assert price_text.startswith("$")
        add_to_cart = page.get_by_text("Sauce Labs Backpack")
        add_to_cart.click()

        #проверка корзины
        # cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        # expect(cart_badge).to_be_visile
        cart = page.locator('[data-test="shopping-cart-link"]')
        # expect(cart).to_have_text("1")
        cart.click()

        #оформление заказа заполнение данных
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

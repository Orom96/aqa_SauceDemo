# Кейсы TC_AUTH_*
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from config.base import BASE_URL, URL_INVENTORY
from config.users import NAME, PASSWORD
from config.products import backpack


def test_complete_checkout_flow(page):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.open(BASE_URL)
    login_page.login(NAME, PASSWORD)
    login_page.assert_logged_in(URL_INVENTORY)

    # Product
    price = inventory_page.get_product_price(backpack)
    print(price)
    assert price.startswith("$")

    inventory_page.add_to_cart(backpack)
    inventory_page.go_to_cart()

    # Checkout
    cart_page.checkout()

    checkout_page.fill_info("Orom", "Anvarov", "734000")
    checkout_page.finish()
    checkout_page.assert_success()
    checkout_page.back_home()
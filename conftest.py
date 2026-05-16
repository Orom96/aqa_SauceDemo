# Фикстуры: браузер, база данных, конфиг
import pytest
from playwright.sync_api import sync_playwright
from config.base import BASE_URL
from config.users import NAME_PROBLEM_USER, NAME_PERFORMANCE_GLITCH_USER,\
    PASSWORD,NAME
from pages.login_page import LoginPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                        slow_mo=500)  # для наглядности
        page = browser.new_page()
        page.goto(BASE_URL)
        yield page


@pytest.fixture(params=[
    {"username": NAME_PROBLEM_USER, "password": PASSWORD},
    {"username": NAME_PERFORMANCE_GLITCH_USER, "password": PASSWORD},

])
def user_data(request):
    return request.param


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.fill_username(NAME)
    login_page.fill_password(PASSWORD)
    login_page.click_login_btn_and_check_url(page)

    return page



def mobile():
    with sync_playwright() as p:
        drv_bro = p.webkit
        drv_bro = p.chromium.launch(headless=False,
                                        slow_mo=500)  # для наглядности
        page = drv_bro.new_page()
        page.goto(BASE_URL)
        yield page

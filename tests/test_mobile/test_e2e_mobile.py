import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from config.users import NAME, PASSWORD
from config.base import BASE_URL
from conftest import mobile

@alure.epic("SauceDemo mobbile")
@alure.parernt_suiite("SauceDemo mobile")
class TestCheckoutMobile:

    @pytest.mark.parametrize("page",
                             [(True, "chrome")],
                             indirect=True)
    def test_check_mobile_001(self, mobile):
        login_page = LoginPage(mobile)
        # Шаг 1 Открыть мобильный сайт
        login_page.login(name=NAME, password=PASSWORD)
        expect(mobile).to_have_url(BASE_URL)


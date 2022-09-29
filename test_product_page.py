import pytest
from .pages.product_page import ProductPage
import time
offers = [(f'offer{i}') for i in range(10)]
offers[7] = pytest.param(offers[6], marks=pytest.mark.xfail)
@pytest.mark.parametrize('offer',offers)
def test_guest_can_add_product_to_bascket(browser,offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_button_to_add_product()
    page.add_product_to_basket()
    page.should_be_alert_message()
    page.should_be_alert_message_contains_product_name()
    page.should_be_alert_message_contains_product_price()

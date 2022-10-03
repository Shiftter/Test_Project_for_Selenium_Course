import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import faker

offers = [(f'offer{i}') for i in range(10)]
offers[7] = pytest.param(offers[7], marks=pytest.mark.xfail)
@pytest.mark.need_review
@pytest.mark.parametrize('offer',offers)
def test_guest_can_add_product_to_basket(browser,offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_button_to_add_product()
    page.add_product_to_basket()
    page.should_be_alert_message()
    page.should_be_alert_message_contains_product_name()
    page.should_be_alert_message_contains_product_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link, 10)
    page.open()
    page.should_be_button_to_add_product()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link, 0)
    page.open()
    page.should_be_button_to_add_product()
    page.add_product_to_basket()
    page.should_be_success_message_is_disappeared()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_backet_page()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_presented_message_about_empty_basket()
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        f = faker.Faker()
        email = f.email()
        page.register_new_user(email,"qawsedrftg1!")
        print(f'Email account is {email}')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(4)
        page.should_be_button_to_add_product()
        page.add_product_to_basket()
        page.should_be_alert_message()
        page.should_be_alert_message_contains_product_name()
        page.should_be_alert_message_contains_product_price()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_not_be_success_message()
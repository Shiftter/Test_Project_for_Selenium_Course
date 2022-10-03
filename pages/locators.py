from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,'.basket-mini a.btn')
    BASKET_LINK_INVALID = (By.CSS_SELECTOR,'.basket-mini a.btn_inc')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR,'#register_form')
    INPUT_EMAIL = (By.CSS_SELECTOR,'#id_registration-email')
    INPUT_PASSWORD1 = (By.CSS_SELECTOR,'#id_registration-password1')
    INPUT_PASSWORD2 = (By.CSS_SELECTOR,'#id_registration-password2')
    BUTTOM_REGISTRATION = (By.CSS_SELECTOR,'[name=registration_submit]')
class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    ALERT_MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages strong')
    ALERT_MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, '#messages')
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main h1')
    PRODUCT_PRICE= (By.CSS_SELECTOR,'.product_main .price_color')
class BasketPageLocators:
    EMPTY_MESSAGES = (By.CSS_SELECTOR,'#content_inner>p')
    EMPTY_BASKET = (By.CSS_SELECTOR,'#content_inner .row')
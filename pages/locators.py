from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR,'#register_form')
class ProductPageLocators:
    BUY_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_MESSAGE = (By.CSS_SELECTOR, '#messages')
    ALERT_MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages strong')
    ALERT_MESSAGE_PRICE_PRODUCT = (By.CSS_SELECTOR, '#messages')
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main h1')
    PRODUCT_PRICE= (By.CSS_SELECTOR,'.product_main .price_color')
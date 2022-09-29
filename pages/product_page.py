from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_to_add_product(self):
        assert self.is_element_present(*ProductPageLocators.BUY_BUTTON), 'Buy button is not presented'
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUY_BUTTON).click()
        self.solve_quiz_and_get_code()
    def should_be_alert_message(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_MESSAGE), 'Alert message is nor presented'
    def should_be_alert_message_contains_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.ALERT_MESSAGE_NAME_PRODUCT).text, 'Message allert is not contains product name'
    def should_be_alert_message_contains_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.ALERT_MESSAGE_PRICE_PRODUCT).text, 'Message allert is not contains product price'
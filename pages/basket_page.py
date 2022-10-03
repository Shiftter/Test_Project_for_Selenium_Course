from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"
    def should_be_presented_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGES), "Empty message is not presented"
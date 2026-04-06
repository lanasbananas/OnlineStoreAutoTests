from .base_page import BasePage
from .locators import BasePageLocators

MESSAGE_EMPTY_BASKET = "Your basket is empty."

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE)
        empty_basket_message = self.browser.execute_script(BasePageLocators.EMPTY_BASKET_MESSAGE_EXTRACTION, message)
        assert empty_basket_message == MESSAGE_EMPTY_BASKET, f"Incorrect message. Got: {empty_basket_message}, expected: {MESSAGE_EMPTY_BASKET}"

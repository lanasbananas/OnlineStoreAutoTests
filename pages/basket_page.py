from .base_page import BasePage
from .locators import BasePageLocators

MESSAGE_EMPTY_BASKET = "Ваша корзина пуста"

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        message = self.browser.find_element(*BasePageLocators.BASKET_MESSAGE)
        empty_basket_message = self.browser.execute_script(BasePageLocators.EMPTY_BASKET_MESSAGE_EXTRACTION, message)
        assert empty_basket_message == MESSAGE_EMPTY_BASKET, f"Uncorrect message. Got: {empty_basket_message}"

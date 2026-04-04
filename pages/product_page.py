from .base_page import BasePage
from .locators import ProductPageLocators

ADD_TO_BASKET_MESSAGE = " был добавлен в вашу корзину."

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_message_about_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_from_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_MESSAGE).text
        full_message_element = self.browser.find_element(*ProductPageLocators.FULL_MESSAGE)
        message_add_to_basket = " " + self.browser.execute_script(ProductPageLocators.ADD_TO_BASKET_MESSAGE_EXTRACTION, full_message_element)
        assert product_name_from_message + message_add_to_basket == product_name + ADD_TO_BASKET_MESSAGE, \
            f"Uncorrect message. Got {product_name_from_message + message_add_to_basket}"

    def should_be_correct_amount(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_amount = self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT).text
        assert product_price == basket_amount, f"Uncorrect amount. Got {basket_amount}, expected {product_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.FULL_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.FULL_MESSAGE), "Disappeared message is presented, but should not be"


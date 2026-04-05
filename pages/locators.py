from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')

    PRODUCT_NAME_FROM_MESSAGE =(By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    FULL_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    ADD_TO_BASKET_MESSAGE_EXTRACTION = "return arguments[0].querySelector('strong').nextSibling.textContent.trim();"

    BASKET_AMOUNT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
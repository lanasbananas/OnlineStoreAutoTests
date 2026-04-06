from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Missing login form"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, f"Incorrect url. Got: {login_url}, expected: url ended with 'login'"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Missing register form"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)

        password_input_again = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_AGAIN)
        password_input_again.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit_button.click()

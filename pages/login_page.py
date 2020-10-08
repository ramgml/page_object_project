from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in self.browser.current_url, f'{current_url} is not login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not found login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Not found register from'

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LOGIN)
        login.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
        password2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT)
        submit.click()

from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_NAME)

    def get_product_price(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)

    def should_be_message_about_product(self, product_name):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            'Message about product not found'
        assert self.get_element_text(*ProductPageLocators.PRODUCT_ADDED_MESSAGE) == product_name, \
            'Name is not correct'

    def should_be_message_product_price(self, product_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE)
        assert self.get_element_text(*ProductPageLocators.BASKET_PRICE) == product_price, \
            'Basket price is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

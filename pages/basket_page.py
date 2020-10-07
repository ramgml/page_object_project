from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Basket is not empty'

    def should_be_text_about_empty_basket(self, text):
        actually_text = self.get_element_text(*BasketPageLocators.BASKET_EMPTY_TEXT)
        assert text in actually_text, \
            f'actually empty basket text is "{actually_text}"'

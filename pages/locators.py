from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form .btn-add-to-basket')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1)')


class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#content_inner .basket_items')

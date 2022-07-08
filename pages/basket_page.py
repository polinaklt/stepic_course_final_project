from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST_IN_BASKET), \
            "There are products in the basket, but should not be"

    def message_about_empty_basket_is_presented(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)

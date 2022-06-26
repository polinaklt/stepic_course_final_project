from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def check_added_book_name(self):
        book_name_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name_element.text
        added_to_cart_alert = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        added_to_cart_alert_text = added_to_cart_alert.text
        assert book_name == added_to_cart_alert_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE), \
            "Success message is presented, but should not be"

    def check_that_alert_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_MESSAGE), \
            "Success message is presented, but should not be"

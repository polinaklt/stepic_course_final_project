from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ALERT_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

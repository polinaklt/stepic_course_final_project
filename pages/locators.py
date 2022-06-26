from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")


class BasketPageLocators():
    PRODUCTS_LIST_IN_BASKET = (By.CSS_SELECTOR, ".btn-group>a.btn.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[value='Add to basket']")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1) .alertinner>strong")

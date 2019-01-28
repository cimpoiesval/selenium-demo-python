import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    @staticmethod
    def price_to_int(product_price):
        price = re.sub(r"[\,\-\s]", "", product_price)
        return price


class HomePage(BasePage):
    def navigate_to_wearables(self):
        self.hover(*HomePageLocators.smart_menu)
        self.wait.until(EC.element_to_be_clickable(
            HomePageLocators.wearables_menu)).click()
        return CategoryPage(self.driver)


class CategoryPage(BasePage):

    def navigate_to_smart_watch_category(self):
        self.find_element(*CategoryPageLocators.smart_watch_menu).click()
        return CategoryPage(self.driver)

    def get_product_name(self):
        return self.find_element(*CategoryPageLocators.product_name).text

    def get_product_price(self):
        price = self.find_element(*CategoryPageLocators.product_price).text
        return self.price_to_int(price)

    def open_product_page(self):
        self.find_element(*CategoryPageLocators.product_name).click()
        return ProductPage(self.driver)


class ProductPage(BasePage):

    def get_product_name(self):
        return self.find_element(*ProductPageLocators.product_name).text

    def get_product_price(self):
        price = self.find_element(*ProductPageLocators.product_price).text
        return self.price_to_int(price)

import unittest
from selenium import webdriver


class BaseTests:

    class SetupTests(unittest.TestCase):
        driver_name = "chrome"

        def set_driver_name(self, driver_name):
            self.driver_name = driver_name

        def get_driver_name(self):
            return self.driver_name

        def setUp(self):
            if self.get_driver_name() == "chrome":
                self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
            if self.get_driver_name() == "firefox":
                self.driver = webdriver.Firefox(executable_path=r'./drivers/geckodriver.exe')
            else:
                self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
            self.driver.get("https://www.alza.cz/")

        def tearDown(self):
            self.driver.close()

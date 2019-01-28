import unittest
import pytest
from selenium import webdriver


class BaseTests:

    class SetupTests(unittest.TestCase):

        @pytest.fixture(scope="session")
        def driver_init(self, request):
            current_browser = request.config.getoption("--browser")
            if current_browser == "chrome":
                self.driver = webdriver.Chrome('./drivers/chromedriver.exe')
            if current_browser == "firefox":
                self.driver = webdriver.Firefox(
                    executable_path=r'./drivers/geckodriver.exe')
            else:
                self.driver = webdriver.Chrome('./drivers/chromedriver.exe')

            self.session = request.node
            for item in self.session.items:
                cls = item.getparent(pytest.Class)
                setattr(cls.obj, "driver", self.driver)
            yield
            self.driver.close()

        @pytest.fixture(autouse=True)
        def around_tests(self):
            self.driver.get("https://www.alza.cz/")

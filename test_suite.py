import unittest
from pyunitreport import HTMLTestRunner
from test_cases import TestProduct
from setup import BaseTests

BaseTests.SetupTests.driver_name = "firefox"
test_suite_chrome = unittest.defaultTestLoader.loadTestsFromTestCase(TestProduct)
kwargs = {
    "output": "",
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(test_suite_chrome)

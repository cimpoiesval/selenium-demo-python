import unittest
from pyunitreport import HTMLTestRunner
from scenarios.test_cases import TestProduct
from scenarios.setup import BaseTests

BaseTests.SetupTests.driver_name = "firefox"
test_suite_chrome = unittest.defaultTestLoader.loadTestsFromTestCase(TestProduct)
kwargs = {
    "output": "../../reports",
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(test_suite_chrome)

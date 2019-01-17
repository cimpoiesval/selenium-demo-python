from setup import BaseTests
from pages import HomePage


class TestProduct(BaseTests.SetupTests):

    def test_product_info(self):
        home_page = HomePage(self.driver)
        category_page = home_page.navigate_to_wearables()
        sub_category_page = category_page.navigate_to_smart_watch_category()
        name_1 = sub_category_page.get_product_name()
        price_1 = sub_category_page.get_product_price()

        product_page = sub_category_page.open_product_page()
        name_2 = product_page.get_product_name()
        price_2 = product_page.get_product_price()

        self.assertEqual(name_1, name_2, "Name is not equal")
        self.assertEqual(price_1, price_2, "Price is not equal")

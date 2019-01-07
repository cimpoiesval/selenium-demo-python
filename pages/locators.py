from selenium.webdriver.common.by import By


class HomePageLocators(object):
    smart_menu = (By.XPATH, "//div[@class='bx']/a[contains(text(),'Smart')]")
    wearables_menu = (By.XPATH, "//a[@class='head'][contains(text(),'Wearables')]")


class CategoryPageLocators(object):
    smart_watch_menu = (By.XPATH, "//div[@class='catlist top']//span[contains(@class,'text')][contains(text(),'Chytré hodinky')]")
    product_name = (By.XPATH, "//div[@class='box browsingitem canBuy inStockAvailability action firstRow'][1]/div[1]/div/a")
    product_price = (By.XPATH, "//div[@class='box browsingitem canBuy inStockAvailability action firstRow'][1]/div[2]/div/div/span[1]")


class ProductPageLocators(object):
    product_name = (By.XPATH, "//h1[@itemprop='name']")
    product_price = (By.XPATH, "//span[@class='bigPrice price_withVat']")

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class ProductCategoryPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def openProducts2(driver, index):
        # Function to open product by list
        if index >= 0 and index < 60:
            product_list = .driver.find_elements(By.CSS_SELECTOR,".product-grid-item:not(.storetail) .product-card-image")
            product_list[index].click()
        else:
            print("Index value is out of range. Should be between 0 and 59")


    def open_product_page(3):
        openProducts2(driver, 3)

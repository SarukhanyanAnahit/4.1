from selenium.webdriver.common.by import By


class ProductPageLocators():
    add_bsk=(By.XPATH, '//button[@value="Add to basket"]')
    prod_name = (By.CSS_SELECTOR, ".product_main h1")
    prod_price = (By.XPATH, '//p[@class="price_color"]')
    name_in_message = (By.XPATH, '//div[@class="alertinner "]/strong')
    total_message = (By.XPATH, '(//div[@class="alertinner "])[3]/p/strong')

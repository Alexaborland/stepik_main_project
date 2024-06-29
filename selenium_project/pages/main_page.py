from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base

class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    select_product_1_locator = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart_locator = '//div[@id="shopping_cart_container"]'


    '''Getters'''
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1_locator)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_locator)))


    '''Actions'''

    def click_select_product_1(self):
        self.get_product_1().click()
        print('Clicked select product 1')

    def click_cart(self):
        self.get_cart().click()
        print('Clicked cart')

    '''Methods'''
    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

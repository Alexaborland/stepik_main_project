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
    select_product_2_locator = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3_locator = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart_locator = '//div[@id="shopping_cart_container"]'
    menu_button_locator = '//button[@id="react-burger-menu-btn"]'
    about_button = '//a[@id="about_sidebar_link"]'


    '''Getters'''
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1_locator)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2_locator)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3_locator)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_locator)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button_locator)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

    '''Actions'''

    def click_select_product_1(self):
        self.get_product_1().click()
        print('Clicked select product 1')

    def click_select_product_2(self):
        self.get_product_2().click()
        print('Clicked select product 2')

    def click_select_product_3(self):
        self.get_product_3().click()
        print('Clicked select product 3')

    def click_cart(self):
        self.get_cart().click()
        print('Clicked cart')

    def click_menu_button(self):
        self.get_menu_button().click()
        print('Clicked menu button')

    def click_about_button(self):
        self.get_about_button().click()
        print('Clicked about button')

    '''Methods'''
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.assert_url('https://saucelabs.com/')

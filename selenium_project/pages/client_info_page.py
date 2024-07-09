from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base

class Client_Info(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    first_name_locator = '//input[@id="first-name"]'
    last_name_locator = '//input[@id="last-name"]'
    postal_code_locator = '//input[@id="postal-code"]'
    button_continue = '//input[@id="continue"]'

    '''Getters'''
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code_locator)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    '''Actions'''
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Input postal code')

    def click_button_continue(self):
        self.get_button_continue().click()
        print('Clicked continue button')

    '''Methods'''
    def input_information(self):
        self.get_current_url()
        self.input_first_name('Aleksandra')
        self.input_last_name('Borland')
        self.input_postal_code('123456')
        self.click_button_continue()


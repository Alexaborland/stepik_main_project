from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_project.base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''

    '''Getters'''

    '''Actions'''

    '''Methods'''

    def finish(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_project.pages.login_page import LoginPage
from selenium_project.pages.main_page import MainPage
from selenium_project.pages.cart_page import CartPage
from selenium_project.pages.client_info_page import Client_Info
from selenium_project.pages.payment_page import PaymentPage
from selenium_project.pages.finish_page import FinishPage

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    yield driver
    driver.quit()

def test_link_about(driver):
    login_page = LoginPage(driver)
    login_page.authorisation()

    main_page = MainPage(driver)
    main_page.select_menu_about()






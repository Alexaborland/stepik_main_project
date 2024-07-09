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


# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service()
#     driver = webdriver.Chrome(options=options, service=g)
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     yield driver
#     driver.quit()


@pytest.mark.run(order=2)
def test_buy_product_1(set_up):
    driver = set_up
    print('Start test 1')
    login_page = LoginPage(driver)
    login_page.authorisation()

    main_page = MainPage(driver)
    main_page.select_product_1()

    checkout = CartPage(driver)
    checkout.product_confirmation()

    client_info = Client_Info(driver)
    client_info.input_information()
    time.sleep(2)

    payment = PaymentPage(driver)
    payment.payment()
    time.sleep(5)

    finish = FinishPage(driver)
    finish.finish()
    print('Finish test 1')


@pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    driver = set_up
    print('Start test 2')
    login_page = LoginPage(driver)
    login_page.authorisation()

    main_page = MainPage(driver)
    main_page.select_product_2()

    checkout = CartPage(driver)
    checkout.product_confirmation()

    print('Finish test 2')


@pytest.mark.run(order=3)
def test_buy_product_3(set_up):
    driver = set_up
    print('Start test 3')
    login_page = LoginPage(driver)
    login_page.authorisation()

    main_page = MainPage(driver)
    main_page.select_product_3()

    checkout = CartPage(driver)
    checkout.product_confirmation()

    print('Finish test 3')

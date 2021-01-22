from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import PhoneDemoProductLocators, DemoCategoryLocators
from pages.cart_page import CartPage, OrderPage
from pages.login_page import LoginPage
from pages.main_page import DemoMainPage, PhonesCategory, EachProductClass
from utils import wait_for_alert_and_accept
from selenium.webdriver.support import expected_conditions as EC


def test_add_cart_item(browser, test_creds):
    main_page = DemoMainPage(browser)
    main_page.navigate_lo_login_page()
    LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
    DemoMainPage(browser).navigate_to_phones_category()
    PhonesCategory(browser).navigate_to_nokia_lumia_product()
    EachProductClass(browser).add_product_to_cart()
    wait_for_alert_and_accept(browser, 10)


def test_make_an_order(browser, order_info, test_creds):
    main_page = DemoMainPage(browser)
    main_page.navigate_lo_login_page()
    main_page = LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
    main_page.navigate_to_cart()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[.='Nokia lumia 1520']")))
    CartPage(browser).click_on_place_order()
    OrderPage(browser).enter_order_data(name=order_info['name'],
                                        city=order_info['city'],
                                        country=order_info['country'],
                                        credit_card=order_info['credit_card'],
                                        month=order_info['month'],
                                        year=order_info['year'])
    OrderPage(browser).click_purchase_button()

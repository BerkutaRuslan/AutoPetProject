from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.main_page import DemoMainPage,ContactFormPage, AboutUsPage
from utils import wait_for_alert_and_accept
from selenium.webdriver.support import expected_conditions as EC

#
# def test_contact(browser, contact_message_data):
#     main_page = DemoMainPage(browser)
#     main_page.contact_button.click()
#     ContactFormPage(browser).send_message(contact_email=contact_message_data['contact_email'],
#                                           contact_name=contact_message_data['contact_name'],
#                                           message=contact_message_data['message'])
#     wait_for_alert_and_accept(browser, 5)
#
#
# def test_about_us(browser):
#     main_page = DemoMainPage(browser)
#     main_page.about_us_button.click()
#     AboutUsPage(browser).play_button.click()
#     AboutUsPage(browser).close_button.click()


def test_cart_button(browser):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_cart()


def test_cart_button_after_login(browser, test_creds):
    main_page = DemoMainPage(browser)
    main_page.navigate_lo_login_page()
    LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "cartur")))
    DemoMainPage(browser).navigate_to_cart()


# def test_next_previous_category_buttons(browser):
#     main_page = DemoMainPage(browser)
#     main_page.category_next_page_button.click()
#     main_page.category_previous_page_button.click()
#
#
# def test_categories_navigation(browser):
#     main_page = DemoMainPage(browser)
#     main_page.navigate_to_phones_category()
#     main_page.navigate_to_laptops_category()
#     main_page.navigate_to_monitors_category()
#
#
# def test_logout_button(browser, test_creds):
#     main_page = DemoMainPage(browser)
#     main_page.navigate_lo_login_page()
#     LoginPage(browser).enter_valid_credentials(login=test_creds["login"], password=test_creds["password"])
#     WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[.='Log out']")))
#     DemoMainPage(browser, registered=True).logout_button.click()

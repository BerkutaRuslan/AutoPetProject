from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages.main_page import DemoMainPage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage

from utils import wait_for_alert_and_accept, wait_for_element_be_located


def test_login_into_account(browser, user):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_signup_page()

    SignUpPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_alert_and_accept(browser, 5)
    alert = browser.switch_to.alert
    alert.accept()

    main_page.navigate_lo_login_page()
    LoginPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    wait_for_element_be_located(browser, 10, 'nameofuser')
    assert DemoMainPage(browser, registered=True).welcome_label.text == f"Welcome {user['login']}"

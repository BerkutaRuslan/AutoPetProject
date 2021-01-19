from pages.main_page import DemoMainPage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from time import sleep


def test_login_into_account(browser, user):
    main_page = DemoMainPage(browser)
    main_page.navigate_to_signup_page()
    SignUpPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    sleep(2)
    obj = browser.switch_to.alert
    obj.accept()
    main_page.navigate_lo_login_page()
    LoginPage(browser).enter_valid_credentials(login=user["login"], password=user["password"])
    sleep(2)
    assert DemoMainPage(browser, registered=True).welcome_label.text == f"Welcome {user['login']}"

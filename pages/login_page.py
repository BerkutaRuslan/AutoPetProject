from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginWindowLocators
from pages.main_page import DemoMainPage


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

        self.login_header = self.browser.find_element(*LoginWindowLocators.LOGIN_HEADER)
        self.username_label = self.browser.find_element(*LoginWindowLocators.USERNAME_LABEL)
        self.password_label = self.browser.find_element(*LoginWindowLocators.PASSWORD_LABEL)
        self.login_input = self.browser.find_element(*LoginWindowLocators.LOGIN_INPUT)
        self.password_input = self.browser.find_element(*LoginWindowLocators.PASSWORD_INPUT)
        self.close_button = self.browser.find_element(*LoginWindowLocators.CLOSE_BUTTON)
        self.enter_button = self.browser.find_element(*LoginWindowLocators.ENTER_BUTTON)

    def enter_valid_credentials(self, login, password):
        wait = WebDriverWait(self.browser, 2)

        self.login_input.send_keys(login)
        try:
            wait.until(EC.text_to_be_present_in_element_value((By.ID, "loginusername"), login))
        except TimeoutException:
            self.login_input.send_keys(login)
        self.password_input.send_keys(password)
        try:
            wait.until(EC.text_to_be_present_in_element_value((By.ID, "loginpassword"), password))
        except TimeoutException:
            self.password_input.send_keys(password)
        self.enter_button.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout2']")))
        return DemoMainPage(self.browser)

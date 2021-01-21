from locators.login_locators import LoginWindowLocators


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
        self.login_input.send_keys(login)
        self.password_input.send_keys(password)
        self.enter_button.click()

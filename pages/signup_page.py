from locators.signup_page_locators import SignUpWindowLocators


class SignUpPage:
    def __init__(self, browser):
        self.browser = browser

        self.signup_header = self.browser.find_element(*SignUpWindowLocators.SIGNUP_HEADER)
        self.username_label = self.browser.find_element(*SignUpWindowLocators.USERNAME_LABEL)
        self.password_label = self.browser.find_element(*SignUpWindowLocators.PASSWORD_LABEL)
        self.login_input = self.browser.find_element(*SignUpWindowLocators.LOGIN_INPUT)
        self.password_input = self.browser.find_element(*SignUpWindowLocators.PASSWORD_INPUT)
        self.close_button = self.browser.find_element(*SignUpWindowLocators.CLOSE_BUTTON)
        self.enter_button = self.browser.find_element(*SignUpWindowLocators.ENTER_BUTTON)

    def enter_valid_credentials(self, login, password):
        self.login_input.send_keys(login)
        self.password_input.send_keys(password)
        self.enter_button.click()

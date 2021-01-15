from locators.main_page_locators import DemoMainPageLocators


class DemoMainPage:
    def __init__(self, browser):
        self.browser = browser

        self.home_icon = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_ICON)
        self.homepage_button = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_BUTTON)
        self.contact_button = self.browser.find_element(*DemoMainPageLocators.CONTACT_BUTTON)
        self.about_us_button = self.browser.find_element(*DemoMainPageLocators.ABOUT_US_BOTTON)
        self.cart_button = self.browser.find_element(*DemoMainPageLocators.CART_BUTTON)
        self.login_button = self.browser.find_element(*DemoMainPageLocators.LOGIN_BUTTON)
        self.sign_up_button = self.browser.find_element(*DemoMainPageLocators.SIGN_UP_BUTTON)
        self.previous_advertising_image_button = self.browser\
            .find_element(*DemoMainPageLocators.PREVIOUS_ADVERTISING_IMAGE)
        self.next_advertising_image_button = self.browser.find_element(*DemoMainPageLocators.NEXT_ADVERTISING_IMAGE)

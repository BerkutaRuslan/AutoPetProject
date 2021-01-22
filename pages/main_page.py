from locators.about_us_page_locators import AboutUsPageLocators
from locators.contact_page_locators import ContactPageLocators
from locators.main_page_locators import DemoMainPageLocators, PhoneDemoProductLocators, EachProduct
from locators.main_page_locators import DemoCategoryLocators
from locators.main_page_locators import LaptopDemoProductLocators
from locators.main_page_locators import MonitorsDemoProductLocators


class DemoMainPage:
    def __init__(self, browser, registered=False):
        self.browser = browser

        self.home_icon = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_ICON)
        self.homepage_button = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_BUTTON)
        self.contact_button = self.browser.find_element(*DemoMainPageLocators.CONTACT_BUTTON)
        self.about_us_button = self.browser.find_element(*DemoMainPageLocators.ABOUT_US_BUTTON)
        self.cart_button = self.browser.find_element(*DemoMainPageLocators.CART_BUTTON)
        self.sign_up_button = self.browser.find_element(*DemoMainPageLocators.SIGN_UP_BUTTON)
        self.category_phone_button = self.browser.find_element(*DemoCategoryLocators.PHONES_BUTTON)
        self.category_laptop_button = self.browser.find_element(*DemoCategoryLocators.LAPTOPS_BUTTON)
        self.category_monitor_button = self.browser.find_element(*DemoCategoryLocators.MONITORS_BUTTON)
        self.category_previous_page_button = self.browser.find_element(*DemoCategoryLocators.PREVIOUS_BUTTON)
        self.category_next_page_button = self.browser.find_element(*DemoCategoryLocators.NEXT_BUTTON)

        if registered:
            self.welcome_label = self.browser.find_element(*DemoMainPageLocators.WELCOME_BUTTON)
            self.logout_button = self.browser.find_element(*DemoMainPageLocators.LOGOUT_BUTTON)
        else:
            self.login_button = self.browser.find_element(*DemoMainPageLocators.LOGIN_BUTTON)

    def navigate_to_phones_category(self):
        self.category_phone_button.click()

    def navigate_to_laptops_category(self):
        self.category_laptop_button.click()

    def navigate_to_monitors_category(self):
        self.category_monitor_button.click()

    def navigate_lo_login_page(self):
        self.login_button.click()

    def navigate_to_signup_page(self):
        self.sign_up_button.click()

    def navigate_to_cart(self):
        self.cart_button.click()


class ContactFormPage:
    def __init__(self, browser):
        self.browser = browser
        self.contact_email = self.browser.find_element(*ContactPageLocators.CONTACT_EMAIL_FORM)
        self.contact_name = self.browser.find_element(*ContactPageLocators.CONTACT_NAME_FORM)
        self.message = self.browser.find_element(*ContactPageLocators.MESSAGE_FORM)
        self.close_button = self.browser.find_element(*ContactPageLocators.CLOSE_BUTTON)
        self.send_message_button = self.browser.find_element(*ContactPageLocators.SEND_MESSAGE_BUTTON)

    def send_message(self, contact_email, contact_name, message):
        self.contact_email.send_keys(contact_email)
        self.contact_name.send_keys(contact_name)
        self.message.send_keys(message)
        self.send_message_button.click()


class AboutUsPage:
    def __init__(self, browser):
        self.browser = browser
        self.play_button = self.browser.find_element(*AboutUsPageLocators.PLAY_BUTTON)
        self.close_button = self.browser.find_element(*AboutUsPageLocators.CLOSE_BUTTON)


class PhonesCategory:
    def __init__(self, browser):
        self.browser = browser

        self.phones_SAMSUNG_GALAXY_S6 = self.browser.find_element(*PhoneDemoProductLocators.SAMSUNG_GALAXY_S6)
        self.phones_NOKIA_LUMIA_1520 = self.browser.find_element(*PhoneDemoProductLocators.NOKIA_LUMIA_1520)
        self.phones_NEXUS_6 = self.browser.find_element(*PhoneDemoProductLocators.NEXUS_6)
        self.phones_SAMSUNG_GALAXY_S7 = self.browser.find_element(*PhoneDemoProductLocators.SAMSUNG_GALAXY_S7)
        self.phones_IPHONE_6_32GB = self.browser.find_element(*PhoneDemoProductLocators.IPHONE_6_32GB)
        self.phones_SONY_XPERIA = self.browser.find_element(*PhoneDemoProductLocators.SONY_XPERIA)
        self.phones_HTC_ONE_M9 = self.browser.find_element(*PhoneDemoProductLocators.HTC_ONE_M9)

    def navigate_to_nokia_lumia_product(self):
        self.phones_NOKIA_LUMIA_1520.click()


class LaptopsCategory:
    def __init__(self, browser):
        self.browser = browser

        self.laptop_SONY_VAIO_I5 = self.browser.find_element(*LaptopDemoProductLocators.SONY_VAIO_I5)
        self.laptop_SONY_VAIO_i7 = self.browser.find_element(*LaptopDemoProductLocators.SONY_VAIO_I7)
        self.laptop_MACBOOK_PRO = self.browser.find_element(*LaptopDemoProductLocators.MACBOOK_PRO)
        self.laptop_MACBOOK_AIR = self.browser.find_element(*LaptopDemoProductLocators.MACBOOK_AIR)
        self.laptop_DELL_I7 = self.browser.find_element(*LaptopDemoProductLocators.DELL_I7)
        self.laptop_DELL_2017 = self.browser.find_element(*LaptopDemoProductLocators.DELL_2017)


class MonitorsCategory:
    def __init__(self, browser):
        self.browser = browser
        self.monitor_APPLE_MONITOR_24 = self.browser.find_element(*MonitorsDemoProductLocators.APPLE_MONITOR_24)
        self.monitor_ASUS_FULL_HD = self.browser.find_element(*MonitorsDemoProductLocators.ASUS_FULL_HD)


class EachProductClass:
    def __init__(self, browser):
        self.browser = browser

        self.add_to_cart = self.browser.find_element(*EachProduct.ADD_TO_CART_BUTTON)

    def add_product_to_cart(self):
        self.add_to_cart.click()

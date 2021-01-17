from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from locators.main_page_locators import DemoMainPageLocators, PhoneDemoProductLocators
from locators.main_page_locators import DemoCategoryLocators
from locators.main_page_locators import LaptopDemoProductLocators
from locators.main_page_locators import MonitorsDemoProductLocators


class DemoMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.home_icon = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_ICON)
        self.homepage_button = self.browser.find_element(*DemoMainPageLocators.HOMEPAGE_BUTTON)
        self.contact_button = self.browser.find_element(*DemoMainPageLocators.CONTACT_BUTTON)
        self.about_us_button = self.browser.find_element(*DemoMainPageLocators.ABOUT_US_BUTTON)
        self.cart_button = self.browser.find_element(*DemoMainPageLocators.CART_BUTTON)
        self.login_button = self.browser.find_element(*DemoMainPageLocators.LOGIN_BUTTON)
        self.sign_up_button = self.browser.find_element(*DemoMainPageLocators.SIGN_UP_BUTTON)
        self.category_phone_button = self.browser.find_element(*DemoCategoryLocators.PHONES_BUTTON)
        self.category_laptop_button = self.browser.find_element(*DemoCategoryLocators.LAPTOPS_BUTTON)
        self.category_monitor_button = self.browser.find_element(*DemoCategoryLocators.MONITORS_BUTTON)
        self.category_previous_page_button = self.browser.find_element(*DemoCategoryLocators.PREVIOUS_BUTTON)
        self.category_next_page_button = self.browser.find_element(*DemoCategoryLocators.NEXT_BUTTON)

    def navigate_to_phones_category(self):
        self.category_phone_button.click()

    def navigate_to_laptops_category(self):
        self.category_laptop_button.click()

    def navigate_to_monitors_category(self):
        self.category_monitor_button.click()


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

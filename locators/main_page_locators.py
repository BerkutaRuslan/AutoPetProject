from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class DemoMainPageLocators:
    HOMEPAGE_ICON = (By.XPATH, "//a[@id='nava']")
    HOMEPAGE_BUTTON = (By.XPATH, "//a[.='Home (current)']")
    CONTACT_BUTTON = (By.XPATH, "//a[.='Contact']")
    ABOUT_US_BUTTON = (By.XPATH, "//a[.='About us']")
    CART_BUTTON = (By.ID, "cartur")
    LOGIN_BUTTON = (By.XPATH, "//a[@id='login2']")
    SIGN_UP_BUTTON = (By.XPATH, "//a[@id='signin2']")
    LOGOUT_BUTTON = (By.XPATH, "//a[@id='logout2']")
    WELCOME_BUTTON = (By.ID, "nameofuser")


@dataclass
class DemoCategoryLocators:
    PHONES_BUTTON = (By.XPATH, "//a[.='Phones']")
    LAPTOPS_BUTTON = (By.XPATH, "//a[.='Laptops']")
    MONITORS_BUTTON = (By.XPATH, "//a[.='Monitors']")
    PREVIOUS_BUTTON = (By.XPATH, "//button[.='Previous']")
    NEXT_BUTTON = (By.XPATH, "//button[.='Next']")


@dataclass
class PhoneDemoProductLocators:
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    NOKIA_LUMIA_1520 = (By.XPATH, "//a[contains(text(),'Nokia lumia 1520')]")
    NEXUS_6 = (By.XPATH, "//a[contains(text(),'Nexus 6')]")
    SAMSUNG_GALAXY_S7 = (By.XPATH, "//a[contains(text(),'Samsung galaxy s7')]")
    IPHONE_6_32GB = (By.XPATH, "//a[contains(text(),'Iphone 6 32gb')]")
    SONY_XPERIA = (By.XPATH, "//a[contains(text(),'Sony xperia z5')]")
    HTC_ONE_M9 = (By.XPATH, "//a[contains(text(),'HTC One M9')]")


@dataclass
class LaptopDemoProductLocators:
    SONY_VAIO_I5 = (By.XPATH, "//a[contains(text(),'Sony vaio i5')]")
    SONY_VAIO_I7 = (By.XPATH, "//a[contains(text(),'Sony vaio i7')]")
    MACBOOK_PRO = (By.XPATH, "//a[contains(text(),'MacBook Pro')]")
    MACBOOK_AIR = (By.XPATH, "//a[contains(text(),'MacBook air')]")
    DELL_I7 = (By.XPATH, "//a[contains(text(),'Dell i7 8gb')]")
    DELL_2017 = (By.XPATH, "//a[contains(text(),'2017 Dell 15.6 Inch')]")


@dataclass
class MonitorsDemoProductLocators:
    APPLE_MONITOR_24 = (By.XPATH, "//a[contains(text(),'Apple monitor 24')]")
    ASUS_FULL_HD = (By.XPATH, "//a[contains(text(),'ASUS Full HD')]")


@dataclass
class EachProduct:
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[.='Add to cart']")

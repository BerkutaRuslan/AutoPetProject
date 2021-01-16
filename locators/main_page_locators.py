from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class DemoMainPageLocators:
    HOMEPAGE_ICON = (By.XPATH, "//a[@id='nava']")
    HOMEPAGE_BUTTON = (By.XPATH, "//a[.='Home (current)']")
    CONTACT_BUTTON = (By.XPATH, "//a[.='Contact']")
    ABOUT_US_BOTTON = (By.XPATH, "//a[.='About us']")
    CART_BUTTON = (By.XPATH, "//a[@id='cartur']")
    LOGIN_BUTTON = (By.XPATH, "//a[.='Log in']")
    SIGN_UP_BUTTON = (By.XPATH, "//a[.='Sign up']")
    PREVIOUS_ADVERTISING_IMAGE = (By.XPATH, "//span[@class='carousel-control-prev-icon']")
    NEXT_ADVERTISING_IMAGE = (By.XPATH, "//span[@class='carousel-control-next-icon']")


@dataclass
class DemoCategoryLocators:
    PHONES_BUTTON = (By.XPATH, "//a[.='Phones']")
    LAPTOPS_BUTTON = (By.XPATH, "//a[.='Laptops']")
    MONITORS_BUTTON = (By.XPATH, "//a[.='Monitors']")
    PREVIOUS_BUTTON = (By.XPATH, "//button[.='Previous']")
    NEXT_BUTTON = (By.XPATH, "//button[.='Next']")


@dataclass
class PhoneDemoProductLocators:
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//a[.='Samsung galaxy s6']")
    NOKIA_LUMIA_1520 = (By.XPATH, "//a[.='Nokia lumia 1520']")
    NEXUS_6 = (By.XPATH, "//a[.='Nexus 6']")
    SAMSUNG_GALAXY_S7 = (By.XPATH, "//a[.='Samsung galaxy s7']")
    IPHONE_6_32GB = (By.XPATH, "//a[.='Iphone 6 32gb']")
    SONY_XPERIA = (By.XPATH, "//a[.='Sony xperia z5']")
    HTC_ONE_M9 = (By.XPATH, "//a[.='HTC One M9']")


@dataclass
class LaptopDemoProductLocators:
    SONY_VAIO_I5 = (By.XPATH, "//a[.='Sony vaio i5']")
    SONY_VAIO_i7 = (By.XPATH, "//a[contains(.,'Sony vaio i7')]")
    MACBOOK_PRO = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a")
    MACBOOK_AIR = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[3]/div/div/h4/a")
    DELL_I7 = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a")
    DELL_2017 = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[5]/div/div/h4/a")


@dataclass
class MonitorsDemoProductLocators:
    APPLE_MONITOR_24 = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")
    ASUS_FULL_HD = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a")

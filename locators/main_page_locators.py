from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class GoogleMainPageLocators:
    GMAIL_URL = (By.XPATH, "//a[contains(text(),'Gmail')]")
    IMAGES_URL = (By.XPATH, "//a[contains(text(),'Images')]")
    GOOGLE_LOGO = (By.XPATH, "//img[@id='hplogo']")
    SEARCH_GLASS_ICON = (By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/*[1]")  # noqa
    INPUT_FIELD = (By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")  # noqa
    MIC_ICON = (By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/*[1]")  # noqa
    GOOGLE_SEARCH = (By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[3]/center[1]/input[1]")
    IM_FEELING_LUCKY = (By.XPATH, "//body/div[@id='viewport']/div[@id='searchform']/form[@id='tsf']/div[2]/div[1]/div[3]/center[1]/input[2]")
    GOOGLE_OFFERED_IN = (By.XPATH, "//div[@id='SIvCob']")
    BOTTOM_COUNTRY = (By.XPATH, "//span[contains(text(),'Ukraine')]")
    BOTTOM_ADVERTISING = (By.XPATH, "//a[contains(text(),'Advertising')]")
    BOTTOM_BUSINESS = (By.XPATH, "//a[contains(text(),'Business')]")
    BOTTOM_ABOUT = (By.XPATH, "//a[contains(text(),'About')]")
    BOTTOM_HOW_SEARCH_WORKS = (By.XPATH, "//a[contains(text(),'How Search works')]")
    BOTTOM_PRIVACY = (By.XPATH, "//body/div[@id='viewport']/div[@id='main']/div[@id='footer']/div[@id='fbarcnt']/div[@id='footcnt']/div[@id='fbar']/div[1]/span[1]/a[1]")
    BOTTOM_TERMS = (By.XPATH, "//body/div[@id='viewport']/div[@id='main']/div[@id='footer']/div[@id='fbarcnt']/div[@id='footcnt']/div[@id='fbar']/div[1]/span[1]/a[2]")
    BOTTOM_SETTINGS = (By.XPATH, "//a[@id='fsettl']")


@dataclass
class DemoMainPageLocators:
    HOMEPAGE_ICON = (By.XPATH, "//a[@id='nava']")
    HOMEPAGE_BUTTON = (By.XPATH, "//a[.='Home (current)']")
    CONTACT_BUTTON = (By.XPATH, "//a[.='Contact']")
    ABOUT_US_BOTTON = (By.XPATH, "//a[.='About us']")
    CART_BUTTON = (By.XPATH, "//a[@id='cartur']")
    LOGIN_BUTTON = (By.XPATH, "//a[.='Log in']")
    SIGN_UP_BUTTON = (By.XPATH, "//a[.='Sign up']")
    PREVIOUS_ADVERTISING_IMAGE = (By.XPATH, "span[@class='carousel-control-prev-icon']")
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
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//div[@id='tbodyid']/div[1]//img[@src='imgs/galaxy_s6.jpg']")
    NOKIA_LUMIA_1520 = (By.XPATH, "//img[@src='imgs/Lumia_1520.jpg']")
    NEXUS_6 = (By.XPATH, "//img[@src='imgs/Nexus_6.jpg']")
    SAMSUNG_GALAXY_S7 = (By.XPATH, "//a[.='Samsung galaxy s7']")
    IPHONE_6_32GB = (By.XPATH, "//img[@src='imgs/iphone_6.jpg']")
    SONY_XPERIA = (By.XPATH, "//a[.='Sony xperia z5']")
    HTC_ONE_M9 = (By.XPATH, "//a[.='HTC One M9']")


@dataclass
class LaptopDemoProductLocators:
    SONY_VAIO_I5 = (By.XPATH, "//a[.='Sony vaio i5']")
    SONY_VAIO_i7 = (By.XPATH, "//a[contains(.,'Sony vaio i7')]")
    MACBOOK_PRO = (By.XPATH, "//a[.='MacBook Pro']")
    MACBOOK_AIR = (By.XPATH, "//a[.='MacBook air']")
    DELL_I7 = (By.XPATH, "//a[.='Dell i7 8gb']")
    DELL_2017 = (By.XPATH, "//a[.='2017 Dell 15.6 Inch']")


@dataclass
class MonitorsDemoProductLocators:
    APPLE_MONITOR_24 = (By.XPATH, "//a[.='Apple monitor 24']")
    ASUS_FULL_HD = (By.XPATH, "//a[.='ASUS Full HD']")

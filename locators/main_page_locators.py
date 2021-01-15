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

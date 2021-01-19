from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class LoginWindowLocators:
    LOGIN_HEADER = (By.XPATH, "//h5[@id='logInModalLabel']")
    USERNAME_LABEL = (By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[2]/form[1]/div[1]/label[1]")
    PASSWORD_LABEL = (By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[2]/form[1]/div[2]/label[1]")
    LOGIN_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    CLOSE_BUTTON = (By.XPATH, "//body/div[@id='logInModal']/div[1]/div[1]/div[3]/button[1]")
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Log in')]")

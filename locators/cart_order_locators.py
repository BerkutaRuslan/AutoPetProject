from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class OrderPageLocators:
    TOTAL_AMOUNT = (By.ID, 'totalm')
    NAME_INPUT = (By.ID, 'name')
    COUNTRY_INPUT = (By.ID, 'country')
    CITY_INPUT = (By.ID, 'city')
    CREDIT_CARD_INPUT = (By.ID, 'card')
    MONTH_INPUT = (By.ID, 'month')
    YEAR_INPUT = (By.ID, 'year')
    CLOSE_BUTTON = (By.ID, 'orderModal')
    PURCHASE_BUTTON = (By.XPATH, "//button[.='Purchase']")

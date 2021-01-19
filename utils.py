from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def wait_for_alert_to_appear(browser, time_to_wait):
    return WebDriverWait(browser, time_to_wait).until(EC.alert_is_present())


def wait_for_element_be_located(browser, time_to_wait, element_id):
    return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.ID, element_id)))

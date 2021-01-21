from locators.cart_locators import CartLocators
from locators.cart_order_locators import OrderPageLocators


class CartPage:
    def __init__(self, browser):
        self.browser = browser

        self.delete_button = self.browser.find_element(*CartLocators.DELETE_BUTTON)
        self.place_order_button = self.browser.find_element(*CartLocators.PLACE_ORDER_BUTTON)

    def click_on_place_order(self):
        self.place_order_button.click()

    def click_on_delete_button(self):
        self.delete_button.click()


class OrderPage:
    def __init__(self, browser):
        self.browser = browser

        self.name_input = self.browser.find_element(*OrderPageLocators.NAME_INPUT)
        self.country_input = self.browser.find_element(*OrderPageLocators.COUNTRY_INPUT)
        self.city_input = self.browser.find_element(*OrderPageLocators.CITY_INPUT)
        self.credit_card_input = self.browser.find_element(*OrderPageLocators.CREDIT_CARD_INPUT)
        self.month_input = self.browser.find_element(*OrderPageLocators.MONTH_INPUT)
        self.year_input = self.browser.find_element(*OrderPageLocators.YEAR_INPUT)
        self.close_button = self.browser.find_element(**OrderPageLocators.CLOSE_BUTTON)
        self.purchase_button = self.browser.find_element(**OrderPageLocators.PURCHASE_BUTTON)

    def enter_order_data(self, name, country, city, credit_card, month, year):
        self.name_input.send_keys(name)
        self.country_input.send_keys(country)
        self.city_input.send_keys(city)
        self.credit_card_input.send_keys(credit_card)
        self.month_input.send_keys(month)
        self.year_input.send_keys(year)

    def click_purchase_button(self):
        self.purchase_button.click()

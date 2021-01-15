from locators.main_page_locators import GoogleMainPageLocators


class GoogleMainPage:
    def __init__(self, browser):
        self.browser = browser

        self.gmail_url = self.browser.find_element(*GoogleMainPageLocators.GMAIL_URL)
        self.images_url = self.browser.find_element(*GoogleMainPageLocators.IMAGES_URL)
        self.search_glass_icon = self.browser.find_element(*GoogleMainPageLocators.SEARCH_GLASS_ICON)
        self.input_field = self.browser.find_element(*GoogleMainPageLocators.INPUT_FIELD)
        self.mic_icon = self.browser.find_element(*GoogleMainPageLocators.MIC_ICON)
        self.google_search = self.browser.find_element(*GoogleMainPageLocators.GOOGLE_SEARCH)
        self.im_feeling_lucky = self.browser.find_element(*GoogleMainPageLocators.IM_FEELING_LUCKY)
        self.google_offered_in = self.browser.find_element(*GoogleMainPageLocators.GOOGLE_OFFERED_IN)
        self.bottom_country = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_COUNTRY)
        self.bottom_advertising = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_ADVERTISING)
        self.bottom_business = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_BUSINESS)
        self.bottom_about = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_ABOUT)
        self.bottom_how_search_works = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_HOW_SEARCH_WORKS)
        self.bottom_privacy = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_PRIVACY)
        self.bottom_terms = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_TERMS)
        self.bottom_settings = self.browser.find_element(*GoogleMainPageLocators.BOTTOM_SETTINGS)

    def input_search(self, text="Default text"):
        self.input_field.send_keys(text)
        self.google_search.click()

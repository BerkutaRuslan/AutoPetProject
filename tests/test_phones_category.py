from pages.main_page import DemoMainPage, PhonesCategory


def test_check_phones_category(browser):
    DemoMainPage(browser).navigate_to_phones_category()
    PhonesCategory(browser)

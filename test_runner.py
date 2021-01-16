from pages.main_page import DemoMainPage


def test_basic_search(browser):
    DemoMainPage(browser)
    print(browser.title)

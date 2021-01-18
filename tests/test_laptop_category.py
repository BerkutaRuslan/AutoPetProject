from pages.main_page import DemoMainPage, LaptopsCategory


def test_check_laptops_category(browser):
    DemoMainPage(browser).navigate_to_laptops_category()
    LaptopsCategory(browser)

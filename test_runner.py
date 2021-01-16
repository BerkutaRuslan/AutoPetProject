from pages.main_page import DemoMainPage


def test_product_samsung_g_6_page(browser):
    DemoMainPage(browser).phones_SAMSUNG_GALAXY_S6.click()
    assert browser.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'


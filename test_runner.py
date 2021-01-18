from pages.main_page import PhonesCategory


def test_product_samsung_g_6_page(browser):
    PhonesCategory(browser).phones_SAMSUNG_GALAXY_S6.click()
    assert browser.current_url == 'https://www.demoblaze.com/prod.html?idp_=1'

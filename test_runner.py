from pages.main_page import GoogleMainPage


def test_basic_search(browser, random_word):
    GoogleMainPage(browser).input_search(text=random_word)
    assert browser.title == f"{random_word} - орлорлоe Search"

import pytest
import chromedriver_binary
from RandomWordGenerator import RandomWord
from selenium import webdriver


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.get("https://www.google.com/?hl=en")
    b.implicitly_wait(5)
    yield b
    b.quit()


@pytest.fixture(scope="function")
def random_word():
    r = RandomWord(max_word_size=5)
    return r.generate()

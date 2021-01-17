import pytest
import chromedriver_binary
from RandomWordGenerator import RandomWord
from selenium import webdriver


@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path=chromedriver_binary.chromedriver_filename)
    b.get("https://www.demoblaze.com/")
    b.implicitly_wait(5)
    yield b
    b.quit()

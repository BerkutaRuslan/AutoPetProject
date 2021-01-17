import pytest
from selenium import webdriver
import chromedriver_binary


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.get("https://www.demoblaze.com/")
    b.implicitly_wait(5)
    yield b
    b.quit()

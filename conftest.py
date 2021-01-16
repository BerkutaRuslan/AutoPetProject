import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.get("https://www.demoblaze.com/")
    b.implicitly_wait(5)
    yield b
    b.quit()


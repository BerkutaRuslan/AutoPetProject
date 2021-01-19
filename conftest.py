import random
import string
import pytest
import chromedriver_binary
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    b = webdriver.Chrome()
    b.get("https://www.demoblaze.com/")
    b.implicitly_wait(5)
    yield b
    b.quit()


def random_data():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(5))


@pytest.fixture(scope="function")
def user():
    return {"login": random_data(),
            "password": random_data()}

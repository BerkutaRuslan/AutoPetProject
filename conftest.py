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


@pytest.fixture(scope="function")
def test_creds():
    return {'login': 'Kazinaki',
            'password': 'qwe123qwer'}


@pytest.fixture(scope="function")
def order_info():
    return {
        "name": "Adjara Gudju",
        "country": "Ukraine",
        "city": "Kiev",
        "credit_card": "1234 5678 1234 5678",
        "month": "07",
        "year": "2025"
    }


@pytest.fixture(scope="function")
def contact_message_data():
    return {
        "contact_email": "admin@admin.com",
        "contact_name": "test_name",
        "message": "test test to fill message form"
    }
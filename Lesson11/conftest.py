import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


if __name__ == "__main__":
    pytest.main()

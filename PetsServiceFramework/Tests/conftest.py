import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    load_dotenv()
    browser = BrowserFactory.get_browser(os.environ["Browser_type"])
    yield browser
    browser.quit()


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name):
        if browser_name.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox()
        elif browser_name.lower() == "edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")


if __name__ == "__main__":
    pytest.main()

import os

from dotenv import load_dotenv


class BasePage:
    def __init__(self, browser):
        load_dotenv()
        self.browser = browser
        self.browser.implicitly_wait(int(os.environ["Timeout_Seconds"]))

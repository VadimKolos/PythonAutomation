import os

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Assertion:
    @staticmethod
    def assert_is_invisible(browser, xpath_string):
        try:
            WebDriverWait(browser, float(os.environ["Timeout_Seconds"])).until(
                EC.invisibility_of_element_located((By.XPATH, xpath_string))
            )
            return False
        except TimeoutException:
            return True

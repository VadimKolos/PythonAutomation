from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


class WaitElement:
    @staticmethod
    def wait_until_element_be_visible(browser, xpath_string):
        WebDriverWait(browser, float(os.environ["Timeout_Seconds"])).until(
            EC.visibility_of_element_located(xpath_string))

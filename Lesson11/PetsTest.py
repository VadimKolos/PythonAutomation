from conftest import browser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config import link, mail, password

class TestLogin:
        def test_input_login(self, browser):
            browser.get(link)
            browser.find_element(By.ID, "login").send_keys(mail)
            browser.find_element(By.CSS_SELECTOR, "#password > input").send_keys(password)
            browser.find_element(By.CLASS_NAME, "p-button-label").submit()
            locator = (By.CLASS_NAME, "product-list-item")
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))
            names = browser.find_elements(By.CLASS_NAME, "product-list-item")

            assert len(names) == 3

from .base_page import BasePage
from .locators import LoginPageLocators, AccountPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class LoginPage(BasePage):
    def login_to_account(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)

        login_email.send_keys('vadim@gmail.com')
        login_password.send_keys('2281488')
        submit_button.submit()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_BUTTON_HEADER))

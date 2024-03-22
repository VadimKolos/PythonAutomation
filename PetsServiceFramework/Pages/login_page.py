import os

from Core.Waiter import WaitElement
from Pages.base_page import BasePage

from Pages.locators import LoginPageLocators, AccountPageLocators


class LoginPage(BasePage):
    def login_to_account(self):
        go_to_login_page_button = self.browser.find_element(*LoginPageLocators.GOTO_LOGIN)
        go_to_login_page_button.click()

        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)

        WaitElement.wait_until_element_be_visible(self.browser, LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(os.environ["Login"])
        login_password.send_keys(os.environ["Password"])
        submit_button.submit()
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)

    def open(self, url):
        self.browser.get(url)

    def go_to_registration(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def login_page_is_displayed(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).is_displayed(), "Login page is not displayed"

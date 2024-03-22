import os

from Core.Waiter import WaitElement
from Pages.base_page import BasePage
from Pages.locators import LoginPageLocators


class RegistrationPage(BasePage):
    def register_account(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)

        WaitElement.wait_until_element_be_visible(self.browser, LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(os.environ["Login"])
        login_password.send_keys(os.environ["Password"])
        confirm_password.send_keys(os.environ["Password"])
        submit_button.submit()

    def error_message_is_displayed(self):
        assert self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE).is_displayed(), \
            "Error message is not displayed."

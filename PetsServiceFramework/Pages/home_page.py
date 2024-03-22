import time

from Core.Waiter import WaitElement
from Core.assertions import Assertion
from Pages.base_page import BasePage
from Pages.locators import AccountPageLocators, EditPetPageLocators, CreatePetPageLocators, LoginPageLocators


class HomePage(BasePage):
    def add_pet(self):
        add_pet_button = self.browser.find_element(*AccountPageLocators.PLUS_BUTTON)
        add_pet_button.click()
        WaitElement.wait_until_element_be_visible(self.browser, CreatePetPageLocators.SUBMIT_BUTTON)

    def pet_count(self):
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)
        pets = self.browser.find_elements(*AccountPageLocators.PET)
        return len(pets)

    def pet_is_added(self, count):
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)
        pets = len(self.browser.find_elements(*AccountPageLocators.PET))
        assert (pets - count) == 1, "Pet is not added"

    def pet_is_not_added(self, count):
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)
        pets = len(self.browser.find_elements(*AccountPageLocators.PET))
        assert (pets - count) == 0, "but was{0}".format((pets - count).__str__())

    def delete_pet(self, name):
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)
        self.browser.find_element(
            *(AccountPageLocators.XPATH, AccountPageLocators.DELETE_PET_BUTTON_TEMPLATE.format(name))).click()
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.BUTTON_YES)
        self.browser.find_element(*AccountPageLocators.BUTTON_YES).click()

    def open_edit_pet_mode(self, name):
        WaitElement.wait_until_element_be_visible(self.browser, AccountPageLocators.PLUS_BUTTON)
        self.browser.find_element(
            *(AccountPageLocators.XPATH, AccountPageLocators.EDIT_PET_BUTTON_TEMPLATE.format(name))).click()
        WaitElement.wait_until_element_be_visible(self.browser, EditPetPageLocators.SAVE_BUTTON)
        time.sleep(1)
        self.browser.find_element(*CreatePetPageLocators.PET_NAME_INPUT).clear()

    def pet_name_is_changed(self, first_name, second_name):
        Assertion.assert_is_invisible(self.browser, (AccountPageLocators.PET_NAME_TEMPLATE.format(first_name)))
        HomePage.pet_with_name_added(self, second_name)

    def pet_name_is_not_changed(self, first_name, second_name):
        Assertion.assert_is_invisible(self.browser, (AccountPageLocators.PET_NAME_TEMPLATE.format(second_name)))
        HomePage.pet_with_name_added(self, first_name)

    def pet_with_name_added(self, name):
        edited_pet = self.browser.find_element(AccountPageLocators.XPATH,
                                               AccountPageLocators.PET_NAME_TEMPLATE.format(name))
        assert edited_pet.is_displayed(), "Card with {} name not found.".format(name)

    def quit_account(self):
        self.browser.find_element(*AccountPageLocators.QUIT_BUTTON).click()
        WaitElement.wait_until_element_be_visible(self.browser, LoginPageLocators.GOTO_LOGIN)

import time

import pyautogui
from selenium.webdriver.common.by import By

from Core.Waiter import WaitElement
from Pages.base_page import BasePage
from Pages.locators import MainPageLocators, PetCardLocator, CreatePetPageLocators


class MainPage(BasePage):
    def type_pet_name(self, pet_name):
        pet_input = self.browser.find_element(*MainPageLocators.PET_NAME_INPUT)
        pet_input.send_keys(pet_name)
        time.sleep(1)
        pyautogui.hotkey('shift', 'enter')
        time.sleep(1)

    def select_pet_type(self, pet_type):
        choose_pet_button = self.browser.find_element(*MainPageLocators.PET_TYPE_DROPDOWN_TRIGGER)
        choose_pet_button.click()
        if pet_type == "cat":
            self.browser.find_element(*CreatePetPageLocators.CAT_OPTION).click()
        elif pet_type == "dog":
            self.browser.find_element(*CreatePetPageLocators.DOG_OPTION).click()
        time.sleep(1)

    def pet_card_type_is_displayed(self, pet_type):
        pet_cards = self.browser.find_elements(By.XPATH, PetCardLocator.PET_CARD_LABEL_TEMPLATE.format(pet_type))
        assert len(pet_cards) > 0, "Pet card is not displayed."

    def pet_card_type_is_not_displayed(self, pet_type):
        pet_cards = self.browser.find_elements(By.XPATH, PetCardLocator.PET_CARD_LABEL_TEMPLATE.format(pet_type))
        assert len(pet_cards) == 0, "Pet card is displayed."

    def pet_card_name_is_displayed(self, pet_name):
        pet_cards = self.browser.find_elements(By.XPATH, PetCardLocator.PET_CARD_NAME_TEMPLATE.format(pet_name))
        assert len(self.browser.find_elements(*PetCardLocator.PET_CARD)) == 1, (
            "Pet card with {} is displayed.".format(pet_name))
        assert len(pet_cards) == 1, "Pet card is not displayed."

    def go_to_main_page(self):
        WaitElement.wait_until_element_be_visible(self.browser, MainPageLocators.MAIN_PAGE_BUTTON)
        self.browser.find_element(*MainPageLocators.MAIN_PAGE_BUTTON).click()

    def pet_card_name_is_not_displayed(self, pet_name):
        pet_cards = self.browser.find_elements(By.XPATH, PetCardLocator.PET_CARD_NAME_TEMPLATE.format(pet_name))
        assert len(self.browser.find_elements(*PetCardLocator.PET_CARD)) == 0, "Pet card is displayed."
        assert len(pet_cards) == 0, "Pet card is displayed."

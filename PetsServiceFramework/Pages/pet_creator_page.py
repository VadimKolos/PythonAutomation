from Core.Waiter import WaitElement
from Pages.base_page import BasePage
from Pages.locators import EditPetPageLocators, AccountPageLocators, CreatePetPageLocators


class CreatePetPage(BasePage):

    def create_pet(self, name, age, pet_type, gender):
        pet_name_input = self.browser.find_element(*CreatePetPageLocators.PET_NAME_INPUT)
        pet_age_input = self.browser.find_element(*CreatePetPageLocators.PET_AGE_INPUT)
        pet_name_input.send_keys(name)
        pet_age_input.send_keys(age)
        self.select_type(pet_type)
        self.select_gender(gender)

    def select_type(self, pet_type):
        self.browser.find_element(*CreatePetPageLocators.PET_TYPE_DROPDOWN_TRIGGER).click()
        if pet_type == "cat":
            self.browser.find_element(*CreatePetPageLocators.CAT_OPTION).click()
        elif pet_type == "dog":
            self.browser.find_element(*CreatePetPageLocators.DOG_OPTION).click()

    def select_gender(self, pet_gender):
        self.browser.find_element(*CreatePetPageLocators.PET_GENDER_DROPDOWN_TRIGGER).click()
        if pet_gender == "male":
            self.browser.find_element(*CreatePetPageLocators.MALE_GENDER).click()
        elif pet_gender == "female":
            self.browser.find_element(*CreatePetPageLocators.FEMALE_GENDER).click()

    def submit_added_pet(self):
        self.browser.find_element(*CreatePetPageLocators.SUBMIT_BUTTON).click()
        WaitElement.wait_until_element_be_visible(self.browser, CreatePetPageLocators.CHOOSE_BUTTON)

    def cancel_added_pet(self):
        self.browser.find_element(*CreatePetPageLocators.CANCEL_BUTTON).click()

    def open_home_page(self):
        self.browser.find_element(*AccountPageLocators.PROFILE_BUTTON).click()


class EditPetPage(CreatePetPage):
    def save_changes(self):
        self.browser.find_element(*EditPetPageLocators.SAVE_BUTTON).click()

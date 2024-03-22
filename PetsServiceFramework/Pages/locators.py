from selenium.webdriver.common.by import By


class MainPageLocators:
    PET_TYPE_DROPDOWN_TRIGGER = (By.XPATH, "//div[@class='p-dropdown-trigger']")
    MAIN_PAGE_BUTTON = (By.XPATH, "//div[@class='p-menubar-start']")
    PET_NAME_INPUT = (By.ID, "petName")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    GOTO_LOGIN = (By.XPATH, "//a/span[text()='Login']/..")
    REGISTER_BUTTON = (By.XPATH, "//span[text()='Register']/..")
    CONFIRM_PASSWORD = (By.XPATH, "//div[@id='confirm_password']/input")
    ERROR_MESSAGE = (By.CLASS_NAME, 'p-message-wrapper')


class AccountPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//span[text()='Profile']/..")
    PLUS_BUTTON = (By.CLASS_NAME, "pi-plus")
    PET = (By.CLASS_NAME, "product-list-item")
    BUTTON_YES = (By.XPATH, "//button[@aria-label='Yes']")
    QUIT_BUTTON = (By.XPATH, "//span[text()='Quit']/..")

    DELETE_PET_BUTTON_TEMPLATE = "//div[text()='{0} ']/../..//button/span[text()='Delete']/.."
    EDIT_PET_BUTTON_TEMPLATE = "//div[text()='{0} ']/../..//button/span[text()='Edit']/.."
    PET_NAME_TEMPLATE = "//div[text()='{0} ']"
    XPATH = By.XPATH


class CreatePetPageLocators:
    PET_NAME_INPUT = (By.ID, "name")
    PET_AGE_INPUT = (By.XPATH, "//span[@id='age']/input")
    PET_TYPE_DROPDOWN_TRIGGER = (By.ID, "typeSelector")
    CAT_OPTION = (By.XPATH, "//li[@aria-label='cat']")
    DOG_OPTION = (By.XPATH, "//li[@aria-label='dog']")
    PET_GENDER_DROPDOWN_TRIGGER = (By.ID, "genderSelector")
    MALE_GENDER = (By.XPATH, "//li[@aria-label='Male']")
    FEMALE_GENDER = (By.XPATH, "//li[@aria-label='Female']")
    SUBMIT_BUTTON = (By.XPATH, "//span[text()='Submit']/..")
    CANCEL_BUTTON = (By.XPATH, "//span[text()='Cancel']/..")
    CHOOSE_BUTTON = (By.XPATH, "//span[text()='Choose']")


class PetCardLocator:
    PET_CARD_LABEL_TEMPLATE = "//div[@class='product-grid-item card']//span[text()='{0}']"
    PET_CARD_NAME_TEMPLATE = "//div[text()='{0}']"
    PET_CARD = (By.XPATH, "//div[@class='product-grid-item card']")


class EditPetPageLocators:
    SAVE_BUTTON = (By.XPATH, "//button[@aria-label='Save']")

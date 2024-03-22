import os

import pytest

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Pages.pet_creator_page import CreatePetPage, EditPetPage
from Pages.registration_page import RegistrationPage


@pytest.mark.smoke
@pytest.mark.win10
def test_add_pet(browser):
    page = LoginPage(browser)
    home_page = HomePage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    count = home_page.pet_count()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet("testCat1", "3", "cat", "male")
    pet_profile.submit_added_pet()
    pet_profile.open_home_page()
    home_page.pet_is_added(count)


@pytest.mark.smoke
@pytest.mark.win10
def test_cancel_pet(browser):
    page = LoginPage(browser)
    home_page = HomePage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    count = home_page.pet_count()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet("testCat3", "2", "cat", "female")
    pet_profile.cancel_added_pet()
    pet_profile.open_home_page()
    home_page.pet_is_not_added(count)


@pytest.mark.smoke
@pytest.mark.win10
def test_delete_pet(browser):
    name = "testPet"
    page = LoginPage(browser)
    home_page = HomePage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    count = home_page.pet_count()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet(name, "3", "cat", "male")
    pet_profile.submit_added_pet()
    pet_profile.open_home_page()
    home_page.delete_pet(name)
    home_page.pet_is_not_added(count)


@pytest.mark.xfail
@pytest.mark.win10
def test_edit_pet(browser):
    first_name = "Name1"
    second_name = "Name2"
    page = LoginPage(browser)
    home_page = HomePage(browser)
    edit_pet_page = EditPetPage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet(first_name, "3", "cat", "male")
    pet_profile.submit_added_pet()
    pet_profile.open_home_page()
    home_page.open_edit_pet_mode(first_name)
    edit_pet_page.create_pet(second_name, "1", "dog", "female")
    edit_pet_page.save_changes()
    home_page.pet_name_is_changed(first_name, second_name)


@pytest.mark.xfail
@pytest.mark.win10
def test_edit_pet_without_submit(browser):
    first_name = "Name3"
    second_name = "Name4"
    page = LoginPage(browser)
    home_page = HomePage(browser)
    edit_pet_page = EditPetPage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet(first_name, "3", "cat", "male")
    pet_profile.submit_added_pet()
    pet_profile.open_home_page()
    home_page.open_edit_pet_mode(first_name)
    edit_pet_page.create_pet(second_name, "1", "dog", "female")
    pet_profile.open_home_page()
    home_page.pet_name_is_not_changed(first_name, second_name)


@pytest.mark.xfail
@pytest.mark.win10
def test_sort_by_pet_type(browser):
    cat = "cat"
    dog = "dog"
    page = LoginPage(browser)
    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    main_page = MainPage(browser)
    main_page.go_to_main_page()
    main_page.select_pet_type(cat)
    main_page.pet_card_type_is_displayed(cat)
    main_page.pet_card_type_is_not_displayed(dog)
    main_page.select_pet_type(dog)
    main_page.pet_card_type_is_displayed(dog)
    main_page.pet_card_type_is_not_displayed(cat)


@pytest.mark.xfail
@pytest.mark.win10
def test_sort_by_pet_name(browser):
    name_pet = "testPet"
    page = LoginPage(browser)
    home_page = HomePage(browser)
    main_page = MainPage(browser)

    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet(name_pet, "3", "cat", "male")
    pet_profile.submit_added_pet()
    main_page.go_to_main_page()
    main_page.type_pet_name(name_pet)
    main_page.pet_card_name_is_displayed(name_pet)


@pytest.mark.regress
@pytest.mark.win10
def test_sort_by_deleted_pet_name(browser):
    name_pet = "testPet"
    page = LoginPage(browser)
    home_page = HomePage(browser)
    main_page = MainPage(browser)

    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    pet_profile = CreatePetPage(browser)
    home_page.add_pet()
    pet_profile.create_pet(name_pet, "3", "cat", "male")
    pet_profile.submit_added_pet()
    pet_profile.open_home_page()
    home_page.delete_pet(name_pet)
    main_page.go_to_main_page()
    main_page.type_pet_name(name_pet)
    main_page.pet_card_name_is_not_displayed(name_pet)


@pytest.mark.smoke
@pytest.mark.win10
def test_quit_from_profile(browser):
    page = LoginPage(browser)
    home_page = HomePage(browser)

    page.open(os.getenv("Base_URL"))
    page.login_to_account()
    home_page.quit_account()
    page.login_page_is_displayed()


@pytest.mark.regress
@pytest.mark.win10
def test_second_register_created_account(browser):
    page = LoginPage(browser)
    page.open(os.getenv("Base_URL"))
    page.go_to_registration()
    registration_page = RegistrationPage(browser)
    registration_page.register_account()
    registration_page.error_message_is_displayed()

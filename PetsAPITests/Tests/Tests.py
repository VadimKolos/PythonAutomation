from APISteps.PetServiceSteps import Pets
from TestSettings import valid_email

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_list_users():
    status, amount = pt.get_list_users()

    assert amount
    assert status == 200


def test_add_pet():
    pet_id, status = pt.add_pet("test6", "w", "3")

    assert status == 200
    assert pet_id


def test_get_token_with_invalid_creds():
    status = pt.get_token_with_invalid_creds(valid_email, "1234")
    assert status == 400


def test_get_pet_after_adding():
    pet_name = "test3"
    pet_id, status = pt.add_pet(pet_name, "wolf", "4")
    created_name = pt.get_pet(str(pet_id))
    assert status == 200
    assert pet_name == created_name


def test_delete_pet_after_adding():
    pet_name = "deletePet"
    pet_id, status = pt.add_pet(pet_name, "eagle", "4")
    created_name = pt.get_pet(str(pet_id))
    assert pet_name == created_name
    status_code = pt.delete_pet(str(pet_id))
    assert status_code == 404


def test_update_pet_after_adding():
    pet_name = "updatePet"
    new_pet_name = "newName"
    pet_id, status = pt.add_pet(pet_name, "eagle", "4")
    created_name = pt.get_pet(str(pet_id))
    assert pet_name == created_name
    new_name = pt.update_pet_name(new_pet_name, "eagle", "4", str(pet_id))[0]
    assert new_name == new_pet_name
    pt.delete_pet(str(pet_id))


def test_get_pet_with_invalid_creds():
    pet_name = "test3"
    pt.add_pet(pet_name, "wolf", "4")
    not_authorized_code = pt.add_pet_with_invalid_password("1", "a", "cat", "2")
    assert not_authorized_code == 401
